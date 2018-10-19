class AABB {
	constructor(x, y, w, h) {
		this.x = x;
		this.y = y;
		this.h = h;
		this.w = w;
	}
	within(n) { return (n.x >= this.x && n.y >= this.y && n.x+n.w <= this.x+this.w && n.y+n.h <= this.y+this.h) }
	colliding(n) {
		if (n.x < this.x + this.w &&
			n.x + n.w > this.x &&
			n.y < this.y + this.h &&
			n.h + n.y > this.y)
			return true;
		else
			return false;
	}
	get volume() { return this.h*this.w }
	union (n) {
		let x = (n.x < this.x ? n.x : this.x);
		let y = (n.y < this.y ? n.y : this.y);
		let w = (n.x+n.w < this.x+this.w ? this.x+this.w : n.x+n.w) - x;
		let h = (n.y+n.h < this.y+this.h ? this.y+this.h : n.y+n.h) - y;
		return new AABB(x, y, w, h);
	}
}
class Branch extends AABB {
	constructor(aabb, left, right, parent, level) {
		super(aabb.x, aabb.y, aabb.w, aabb.h);
		this.l = left;
		this.r = right;
		left.parent = this;
		right.parent = this;
		this.parent = parent;
		this.level = level;	
	}
	insert(n) {
		let il = this.l.within(n);
		let ir = this.r.within(n);
		if (il && !ir) {
			this.l = this.l.insert(n);
			return this;
		}
		else if (ir && !il) {
			this.r = this.r.insert(n);
			return this;
		}
		else {
			let lr = this.l.union(this.r).volume;
			let ln = this.l.union(n).volume;
			let nr = this.r.union(n).volume;
			if (lr < nr && lr < ln) {
				let b = new Branch(this.l.union(this.r), this.l, this.r, undefined, this.level);	
				let bp = new Branch(n.union(b), b, n, this.parent, this.level);
				b.parent = bp;
				return bp;
			}
			else if (ir && il) {
				if (nr < lr && nr < ln) this.r = this.r.insert(n);
				else this.l = this.l.insert(n);
				return this;
			}
			else if (nr < lr && nr < ln) {
				let b = new Branch(n.union(this.r), n, this.r, undefined, this.level);	
				let bp = new Branch(this.l.union(b), b, this.l, this.parent, this.level);
				b.parent = bp;
				return bp;
			}
			else {
				let b = new Branch(this.l.union(n), this.l, n, undefined, this.level);	
				let bp = new Branch(this.r.union(b), b, this.r, this.parent, this.level);
				b.parent = bp;
				return bp;
			}
		}
	}
	draw() {
		if (this.l != undefined) this.l.draw();
		if (this.r != undefined) this.r.draw();
		if (this.level.debug == true) {
			this.level.ctx.rect(this.x, this.y, this.w, this.h);
			this.level.ctx.stroke();
		}
	}
	add(e, res) {
		if (this.colliding(e)) {
			if (this.l != undefined) this.l.add(e, res);
			if (this.r != undefined) this.r.add(e, res);
		}
	}
	get sibling() { return (this.parent.l != this ? this.parent.l : this.parent.r); }
	fit() {
		let aabb = this.l.union(this.r);
		this.x = aabb.x;
		this.y = aabb.y;
		this.w = aabb.w;
		this.h = aabb.h;
		if (this.parent != undefined) this.parent.fit();
	}
}
class Leaf extends AABB {
	constructor(e, level, margin) {
		super(e.x + (e.velocity_x > 0 ? 0 : e.velocity_x*margin), e.y + (e.velocity_y > 0 ? 0 : e.velocity_y*margin), e.w + Math.abs(e.velocity_x*margin), e.h + Math.abs(e.velocity_y*margin));
		e.parent = this;
		e.level = level;
		this.entity = e;
		this.level = level;
		this.parent = undefined;
	}
	insert(n) { return new Branch(this.union(n), this, n, this.parent, this.level) }
	draw() {
		if (this.level.debug == true) {
			this.level.ctx.rect(this.x, this.y, this.w, this.h);
			this.level.ctx.stroke();
		}
		this.entity.draw();
	}
	add(e, res) { if (this.entity != e) res.push(this.entity) }
	get sibling() { return (this.parent.l != this ? this.parent.l : this.parent.r); }
	fit() { if (this.parent != undefined) this.parent.fit(); }
}
class Entity extends AABB {
	constructor(x, y, w, h, active, name) {
		super(x, y, w, h);
		this.active = active;
		this.name = name;
		this.parent = undefined;
		this.level = undefined;
		this.velocity_x = 0;
		this.velocity_y = 0;
	}
	draw() {
		this.level.ctx.beginPath();
		this.level.ctx.arc(this.x+25, this.y+25, 25, 0, 2 * Math.PI, false);
		this.level.ctx.stroke();
		this.level.ctx.font = "30px Arial";
		this.level.ctx.fillText(this.name, this.x+16, this.y+35);
	}
	getState() {
		let e = this.query();
		return e.length;
	}
	updateState(){
		if(this.parent.within(this) == false) {
			this.remove();
			this.level.insert(this);
		}
	}
	query() {
		let result = [];
		this.level.root.add(this, result)
		return result;
	}
	remove() {
		if (this.parent == this.level.root) this.level.root = undefined;
		else {
			let parentp = this.parent.parent;
			let sibling = this.parent.sibling;
			if (parentp == this.level.root) {
				sibling.parent = undefined;
				this.level.root = sibling;
			}
			else {
				sibling.parent = parentp.parent;
				if (parentp.parent.l == parentp) parentp.parent.l = sibling;
				else if (parentp.parent.r == parentp) parentp.parent.r = sibling;
				//sibling.fit();
			}
		}
	}
}
class Tree {
	constructor (ctx) {
		this.root = undefined;
		this.debug = false;
		this.activeEntities = [];
		this.ctx = ctx;
		if (ctx == undefined) this.visualize = false;
		else this.visualize = true;
	}
	insert(e) {
		if (e.level == undefined && e.active == true) this.activeEntities.push(e);
		let ep = new Leaf(e, this, 10); 
		if (this.root == undefined) this.root = ep;
		else this.root = this.root.insert(ep);
	}
	draw() {
		if (this.visualize = false) console.error("No canvas to draw provided");
		else {
			this.ctx.clearRect(0,0,this.ctx.canvas.width,this.ctx.canvas.height);
			this.ctx.beginPath();
			if (this.root == undefined) console.error("level is empty");
			else this.root.draw();
		}
	}
	update() {
		let t = 0;
		this.activeEntities.forEach((e)=> { t += e.getState() });
		this.activeEntities.forEach((e)=> { e.updateState() });
		return t;
	}
}