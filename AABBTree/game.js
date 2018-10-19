class Circle extends Entity {
	constructor(x, y, r, name) {
		super(x, y, 2*r, 2*r, false, name);
		this.r = r;
	}
	draw() {
		this.level.ctx.beginPath();
		this.level.ctx.arc(this.x+this.r, this.y+this.r, this.r, 0, 2 * Math.PI, false);
		this.level.ctx.stroke();
	}
	colliding(n) {
		//if ((this.x+this.r) >= this.n)
	}
}

class Planet extends Circle {
	constructor(x, y, r, name) {
		super(x, y, r, name);
	}
	draw() {
		this.level.ctx.beginPath();
		this.level.ctx.arc(this.x+this.r, this.y+this.r, this.r, 0, 2 * Math.PI, false);
		this.level.ctx.stroke();
	}
};

class Player extends Entity {
	constructor() {

	}
}

function startApp() {
	let canvas = document.createElement("canvas");
	canvas.style.cssText = "background-color:white;";
	canvas.width = 600;
	canvas.height = 600;
	(window.innerWidth > window.innerHeight) ? canvas.className = "h" : canvas.className = "w";
	window.onresize = (e)=> { (window.innerWidth > window.innerHeight) ? canvas.className = "h" : canvas.className = "w"; };
	document.body.appendChild(canvas);
	let ctx = canvas.getContext("2d");

	level = new Tree(ctx);
	level.debug = true;
	
	//level.insert(new Planet(200, 200, 100, "p1"));
	level.insert(new Circle(100, 100, 30, "p1"));
	level.insert(new Circle(200, 200, 30, "p2"));
	level.insert(new Circle(300, 300, 30, "p3"));
	level.insert(new Circle(400, 400, 30, "p4"));

	setInterval(()=> { level.draw(); level.update();}, 50);
}