function process(json)
{
    const words = json.map(l => l.split(' '));
    let starts = [];
    let chain = {};
    for (let i in words){
        starts.push(words[i][0]);
        for (let j = 0; j < words[i].length-1; j++){
            if (chain[words[i][j]] === undefined){
                chain[words[i][j]] = [];
            }
            chain[words[i][j]].push(words[i][j+1]);
        }
    }
    return [starts, chain];
}
function generate(starts, chain)
{
    let cur = starts[Math.floor(Math.random()*starts.length)];
    let result = cur;
    while(result[result.length-1] != '?' && result[result.length-1] != '.'){
        cur = chain[cur][Math.floor(Math.random()*chain[cur].length)];
        result += " " + cur
    }
    return result;
}
class Thonk
{
    constructor(){
        this.x = Math.random()*window.innerWidth-300;
        this.y = Math.random()*window.innerHeight-300;
        this.a = Math.random()*360;
        this.vx = Math.random()*3+1;
        this.vy = Math.random()*3+1;
        this.dx = (Math.floor(Math.random() * 2) === 0) ? 1 : -1;
        this.dy = (Math.floor(Math.random() * 2) === 0) ? 1 : -1;
        this.va = (Math.floor(Math.random() * 2) === 0) ? 1 : -1;
        this.ele = document.createElement('img');
        this.ele.src = 'thonk.png';
        document.body.append(this.ele);
    }
    update(){
        if(this.x > window.innerWidth-300){
            this.dx = -1;
        }else if(this.x < 0){
            this.dx = 1;
        }
        if(this.y > window.innerHeight-300){
            this.dy = -1;
        }else if(this.y < 0){
            this.dy = 1;
        }
        this.x += this.vx*this.dx;
        this.y += this.vy*this.dy;
        this.a += this.va;
        this.ele.style = "position:absolute; height:300px; width:300px; left: "+this.x+"px; top: "+this.y+"px; z-index: -1; transform: rotate("+this.a+"deg);";
    }
}
let thonks = [];
let starts;
let chain;
function refresh(){
  thonks.push(new Thonk());
  document.getElementById("question").innerHTML = generate(starts, chain);
}
async function main()
{
    const res = await fetch('questions.json');
    const data = await res.json();
    const model = process(data);
    starts = model[0];
    chain = model[1];
    document.getElementById("question").innerHTML = generate(starts, chain);
    thonks.push(new Thonk());
    setInterval(()=>{thonks.forEach((t)=>t.update());},100);
}