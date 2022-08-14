var screen=document.getElementsByClassName("dishesitems")[0]
function getdishes(){
    post({},"getdishes").then(res=>{
        console.log(res)
        let data=JSON.parse(res)
        disheslist(data)
    })
}
function disheslist(data){
    let items=document.getElementsByClassName("dishesitems")[0]
    items.innerHTML=''
	for (let i = 0, length = data.length; i < length; i++) {
		let div = document.createElement("div")
		let name = document.createElement("h2")
		let cost = document.createElement("h2")
        let add =document.createElement("button")
  
		name.innerText = data[i]['name']
		cost.innerText = data[i]['cost']
        add.innerText="加入"
        add.onclick=addorder
		div.appendChild(name)
		div.appendChild(cost)
        div.appendChild(add)
		items.appendChild(div)
        
	}
    screen.style.display="none"
    screen=document.getElementsByClassName("dishesitems")[0]
    screen.style.display="block"
}
function addorder(){
    let orderlist=document.getElementsByClassName("items")[0]
    let node=this.parentNode
    let h2=node.getElementsByTagName("h2")
    let div = document.createElement("div")
    let name = document.createElement("h2")
    let cost = document.createElement("h2")
    let del=document.createElement("button")
    del.innerHTML="删除"
    del.onclick=remove
    name.innerText=h2[0].innerText
    cost.innerText=h2[1].innerText
    div.appendChild(name)
    div.appendChild(cost)
    div.appendChild(del)
    orderlist.appendChild(div)

}
function remove(){
    let node=this.parentNode
    node.parentNode.removeChild(node)
}
function show_order(){
    screen.style.display="none"
    screen=document.getElementsByClassName("selected")[0]
    screen.style.display="block"
}
function clear_order(){

    screen.getElementsByClassName("items")[0].innerHTML=''
}
function ensure_order(){
    let orderlist=document.getElementsByClassName("items")[0]
    let h2=orderlist.getElementsByTagName("h2")

    let dishes=''
    for(let i=0,length=h2.length;i<length;i+=2){
        dishes+=(h2[i].innerText+" "+h2[i+1].innerText+" ")
    }
    
    let data={
        "dishes":dishes,
        "date":(new Date()).toTimeString()
    }
    console.log(data)

    post(data,"save_order").then(res=>{
        clear_order()
    })
}
function show_history_order(){
    screen.style.display="none"
    screen=document.getElementsByClassName("history")[0]
    screen.style.display="block"
    screen.innerHTML=''
    post({},"getorders").then(res=>{
        let data=JSON.parse(res)
        for (const order of data) {
            let dishes=order.dishes.split(" ")
            let item=document.createElement("div")
            for(let i=0,length=dishes.length;i<length-2;i+=2){
                let item_=document.createElement("div")
                let h2=document.createElement("h2")
                h2.innerText=dishes[i]
                item_.appendChild(h2)
                h2=document.createElement("h2")
                h2.innerText=dishes[i+1]
                item_.appendChild(h2)
                item.appendChild(item_)
            }
            screen.appendChild(item)
        }
    })



}

function addlistener(){
    let ret=document.getElementsByClassName("selection")[0]
    ret.addEventListener("click",(e)=>{
        if(e.target.innerText==="全部菜品"){
            let div=e.target.parentNode.getElementsByTagName("div")
            div[0].id="select"
            div[1].id="unselect"
            div[2].id="unselect"
            getdishes()
        }
        else if(e.target.innerText==="订单"){
            let div=e.target.parentNode.getElementsByTagName("div")
            div[1].id="select"
            div[0].id="unselect"
            div[2].id="unselect"
            show_order()
        }
        else if(e.target.innerText==="历史订单"){
            let div=e.target.parentNode.getElementsByTagName("div")
            div[2].id="select"
            div[1].id="unselect"
            div[0].id="unselect"
            show_history_order()
        }
    })
}
addlistener()
window.onload=getdishes