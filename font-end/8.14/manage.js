var screen=document.getElementsByClassName("dishlist")[0]

function getdishes(){

    post({},"getdishes").then(res=>{
        console.log(res)
        let data=JSON.parse(res)
        disheslist(data)
    })

}
function getusers(){
    post({},"getusers").then(res=>{
        console.log(res)
        let data=JSON.parse(res)
        userslist(data)
    })
}
function disheslist(data){
    let items=document.getElementsByClassName("dishesitems")[0]
    items.innerHTML=''
	for (let i = 0, length = data.length; i < length; i++) {
		let div = document.createElement("div")
		let name = document.createElement("h2")
		let cost = document.createElement("h2")
        let costchange=document.createElement("input")
        let ok =document.createElement("button")
        let del =document.createElement("button")
		name.innerText = data[i]['name']
		cost.innerText = data[i]['cost']
        ok.innerText='确认'
        del.innerText='删除'

        ok.onclick=cost_change
        del.onclick=del_dish
		div.appendChild(name)

		div.appendChild(cost)
        div.appendChild(costchange)
        div.appendChild(ok)
        div.appendChild(del)
		items.appendChild(div)
        
	}
    screen.style.display='none'
    screen=document.getElementsByClassName("dishlist")[0]
    screen.style.display='block'
}
function userslist(data){
    let items=document.getElementsByClassName("usersitems")[0]
    items.innerHTML=''
	for (let i = 0, length = data.length; i < length; i++) {
		let div = document.createElement("div")
		let username = document.createElement("h2")
		let passward = document.createElement("h2")
        let passwardchange=document.createElement("input")
        let ok =document.createElement("button")
        let del =document.createElement("button")
		username.innerText = data[i]['username']
		passward.innerText = data[i]['passward']
        ok.innerText='确认'
        del.innerText='删除'

        ok.onclick=passward_change
        del.onclick=del_user
		div.appendChild(username)

		div.appendChild(passward)
        div.appendChild(passwardchange)
        div.appendChild(ok)
        div.appendChild(del)
		items.appendChild(div)
        
	}
    screen.style.display='none'
    screen=document.getElementsByClassName("userlist")[0]
    screen.style.display='block'
}
function add_dish(){
    screen.style.display='none'
    screen=document.getElementsByClassName("adddish")[0]
    screen.style.display='block'
}
function add_user(){
    screen.style.display='none'
    screen=document.getElementsByClassName("adduser")[0]
    screen.style.display='block'
}
function add_dish_back(){
    screen.style.display='none'
    screen=document.getElementsByClassName("dishlist")[0]
    screen.style.display='block'
}
function add_user_back(){
    screen.style.display='none'
    screen=document.getElementsByClassName("userlist")[0]
    screen.style.display='block'
}
function add_dish_post(){
    let inputs=screen.getElementsByTagName("input")
    let name=inputs[0].value
    let cost=inputs[1].value
    let data={
        "name":name,
        "cost":cost
    }
    post(data,"add_dish").then(res=>{
        let status=JSON.parse(res)
        if(status){
            screen.style.display='none'
            screen=document.getElementsByClassName("dishlist")[0]
            screen.style.display='inline-block'
            let div = document.createElement("div")
            let name = document.createElement("h2")
            let cost = document.createElement("h2")   
            let costchange=document.createElement("input")
            let ok =document.createElement("button")  
            let del = document.createElement("button")
            name.innerText = data.name
            cost.innerText = data.cost
            ok.innerText='确认'
            del.innerText='删除'
            ok.onclick=cost_change
            del.onclick=del_dish
            div.appendChild(name)

            div.appendChild(cost)
            div.appendChild(costchange)
            div.appendChild(ok)
            div.appendChild(del)
            screen.getElementsByClassName("dishesitems")[0].appendChild(div)
        }

    })
}
function add_user_post(){
    let inputs=screen.getElementsByTagName("input")
    let username=inputs[0].value
    let passward=inputs[1].value
    let data={
        "username":username,
        "passward":passward,
        "manager":inputs[2].checked
    }
    post(data,"logon").then(res=>{
    
            screen.style.display='none'
            screen=document.getElementsByClassName("userlist")[0]
            screen.style.display='block'
            let div = document.createElement("div")
            let username = document.createElement("h2")
            let passward = document.createElement("h2")
            let passwardchange=document.createElement("input")
            let ok =document.createElement("button")
            let del =document.createElement("button")
            username.innerText = data['username']
            passward.innerText = data['passward']
            ok.innerText='确认'
            del.innerText='删除'

            ok.onclick=passward_change
            del.onclick=del_user
            div.appendChild(username)

            div.appendChild(passward)
            div.appendChild(passwardchange)
            div.appendChild(ok)
            div.appendChild(del)
            screen.getElementsByClassName("usersitems")[0].appendChild(div)
        }

    )
}
function change_dish(){
    let buttons=document.getElementsByClassName("dishesitems")[0].getElementsByTagName("button")
    for (const button of buttons) {
        button.style.display="inline-block"
    }
    let inputs=document.getElementsByClassName("dishesitems")[0].getElementsByTagName("input")
    for (const input of inputs) {
        input.style.display="inline-block"
    }

    let input=document.getElementsByClassName("selection_")[0].getElementsByTagName("input")

    input[0].style.display="none"
    input[1].style.display="inline-block"


}
function change_user(){
    let buttons=document.getElementsByClassName("usersitems")[0].getElementsByTagName("button")
    for (const button of buttons) {
        button.style.display="inline-block"
    }
    let inputs=document.getElementsByClassName("usersitems")[0].getElementsByTagName("input")
    for (const input of inputs) {
        input.style.display="inline-block"
    }

    let input=document.getElementsByClassName("selection_")[1].getElementsByTagName("input")

    input[0].style.display="none"
    input[1].style.display="inline-block"



}
function change_dish_back(){
    let buttons=document.getElementsByClassName("dishesitems")[0].getElementsByTagName("button")
    for (const button of buttons) {
        button.style.display="none"
    }
    let inputs=document.getElementsByClassName("dishesitems")[0].getElementsByTagName("input")
    for (const input of inputs) {
        input.style.display="none"
    }

    let input=document.getElementsByClassName("selection_")[0].getElementsByTagName("input")

    input[1].style.display="none"
    input[0].style.display="inline-block"


}
function change_user_back(){
    let buttons=document.getElementsByClassName("usersitems")[0].getElementsByTagName("button")
    for (const button of buttons) {
        button.style.display="none"
    }
    let inputs=document.getElementsByClassName("usersitems")[0].getElementsByTagName("input")
    for (const input of inputs) {
        input.style.display="none"
    }

    let input=document.getElementsByClassName("selection_")[1].getElementsByTagName("input")

    input[1].style.display="none"
    input[0].style.display="inline-block"


}
function cost_change(){
    let node=this.parentNode
    let h2=node.getElementsByTagName("h2")
    let new_cost=node.getElementsByTagName('input')[0]
    let data=[
        {
            "name":h2[0].innerText,
            "cost":h2[1].innerText
        },
        {
            "name":h2[0].innerText,
            "cost":new_cost.value
        }
    ]
    console.log(data)
    data=JSON.stringify(data)
    post(data,"update_dish").then(res=>{
            let data=JSON.parse(res)
            console.log(data)
            h2[0].innerText=data.name
            h2[1].innerText=data.cost
            new_cost.value=''

    })
}
function passward_change(){
    let node=this.parentNode
    let h2=node.getElementsByTagName("h2")
    let new_passward=node.getElementsByTagName('input')[0]
    let data=[
        {
            "username":h2[0].innerText,
            "passward":h2[1].innerText
        },
        {
            "username":h2[0].innerText,
            "passward":new_passward.value
        }
    ]
    console.log(data)
    data=JSON.stringify(data)
    post(data,"update_user").then(res=>{
            let data=JSON.parse(res)
            console.log(data)
            h2[0].innerText=data.username
            h2[1].innerText=data.passward
            new_passward.value=''

    })
}
function del_dish(){
    let node=this.parentNode
    let h2=node.getElementsByTagName("h2")
    let data ={
        "name":h2[0].innerText,
        "cost":h2[1].innerText
    }
    data=JSON.stringify(data)
    post(data,"del_dish").then(res=>{
        node.parentNode.removeChild(node)
    })
}
function del_user(){
    let node=this.parentNode
    let h2=node.getElementsByTagName("h2")
    let data ={
        "username":h2[0].innerText,
        "passward":h2[1].innerText
    }
    data=JSON.stringify(data)
    post(data,"del_user").then(res=>{
        node.parentNode.removeChild(node)
    })
}
function addlistener(){
    let ret=document.getElementsByClassName("selection")[0]
    ret.addEventListener("click",(e)=>{
        if(e.target.innerText==="菜品管理"){
            let div=e.target.parentNode.getElementsByTagName("div")
            div[0].id="select"
            div[1].id="unselect"
            getdishes()
        }
        else if(e.target.innerText==="客户管理"){
            let div=e.target.parentNode.getElementsByTagName("div")
            div[1].id="select"
            div[0].id="unselect"
            getusers()
        }
    })
}
addlistener()
window.onload=getdishes