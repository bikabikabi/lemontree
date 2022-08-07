
function getall_post(){
	post({},"getall").then(res=>{

		let data=JSON.parse(res)
		let items = document.getElementsByClassName("items")[0]
		items.innerHTML=''
		items.style.display="block"
		for (let i = 0, length = data.length; i < length; i++) {
			let div = document.createElement("div")
			let h2 = document.createElement("h2")
			let p = document.createElement("P")
			h2.innerText = data[i]['title']
			p.innerText = data[i]['content']
			div.appendChild(h2)
			div.appendChild(p)
			items.appendChild(div)
		}
	})
}
function show(data) {
	let show = document.getElementsByClassName("show")[0];
	let title = show.getElementsByTagName("h2")[0]
	let content = show.getElementsByTagName("P")[0]
	title.innerText = data["title"]
	content.innerText = data["content"]
	document.getElementsByClassName("items")[0].style.display = "none"
	document.getElementsByClassName("find")[0].style.display = "none"
	show.style.display = "block"
}
function back_show(){
	document.getElementsByClassName("show")[0].style.display="none"
	document.getElementsByClassName("items")[0].style.display="block"
}
function to_modify(){
	let modify=document.getElementsByClassName("modify")[0]
	modify.style.display="block"

	let show=document.getElementsByClassName("show")[0]
	show.style.display="none"

	document.getElementById("new_title").value=show.getElementsByTagName("h2")[0].innerText;
	document.getElementById("new_text_input").value=show.getElementsByTagName("p")[0].innerText;

}
function back_modify(){
	let modify=document.getElementsByClassName("modify")[0]
	modify.style.display="none"

	let show=document.getElementsByClassName("show")[0]
	show.style.display="block"

}
function modify_post(){
	let show = document.getElementsByClassName("show")[0];
	let title = show.getElementsByTagName("h2")[0].innerText
	let content = show.getElementsByTagName("P")[0].innerText

	let modify=document.getElementsByClassName("modify")[0];
	let new_title=document.getElementById("new_title").value
	let new_content=document.getElementById("new_text_input").value

	data=[
		{
			"title":title,
			"content":content
		},
		{
			"title":new_title,
			"content":new_content
		}
	]
	
	post(data,"modify").then(res=>{
		modify.style.display="none"
		getall_post()
	})
}	
function to_add() {
	let add = document.getElementsByClassName("add")[0];
	let items = document.getElementsByClassName("items")[0];
	add.style.display = "block"
	items.style.display = "none"
	document.getElementsByClassName("find")[0].style.display = "none"
	document.getElementsByClassName("show")[0].style.display="none"
	document.getElementsByClassName("modify")[0].style.display="none"
};
function back_add() {
	let add = document.getElementsByClassName("add")[0];
	let items = document.getElementsByClassName("items")[0];
	items.style.display = "block"
	add.style.display = "none"
};

function add(data) {

	let items = document.getElementsByClassName("items")[0]
	let div = document.createElement("div")
	let h2 = document.createElement("h2")
	let p = document.createElement("P")
	h2.innerText = data['title']
	p.innerText = data['content']
	div.appendChild(h2)
	div.appendChild(p)
	items.appendChild(div)

}
function add_post() {
	let title = document.getElementById("title").value;
	let text = document.getElementById("text_input").value;
	let data = {
		'title': title,
		'content': text
	}
	post(data, 'add').then(res => {
		console.log(res)
		data = JSON.parse(res)
		add(data)
		back_add()
	})
}
function show_find(data) {
	let items = document.getElementsByClassName("find_items")[0]
	items.innerHTML=''
	for (let i = 0, length = data.length; i < length; i++) {
		let div = document.createElement("div")
		let h2 = document.createElement("h2")
		let p = document.createElement("P")
		h2.innerText = data[i]['title']
		p.innerText = data[i]['content']
		div.appendChild(h2)
		div.appendChild(p)
		items.appendChild(div)
	}
	let find = document.getElementsByClassName("find")[0]
	find.style.display = 'block'
	document.getElementsByClassName("add")[0].style.display = "none";
	document.getElementsByClassName("items")[0].style.display = "none";
	document.getElementsByClassName("show")[0].style.display="none"
	document.getElementsByClassName("modify")[0].style.display="none"
}
function back_find() {
	document.getElementsByClassName("items")[0].style.display = "block";
	document.getElementsByClassName("find")[0].style.display = "none"
}
function find_post() {
	let text = document.getElementById("input_find").value;
	let data = {
		'data': text
	}
	post(data, 'find').then(res => {
		console.log(res)
		data = JSON.parse(res)
		show_find(data)
	})
}
function del_post(){
	let show = document.getElementsByClassName("show")[0];
	let title = show.getElementsByTagName("h2")[0].innerText
	let content = show.getElementsByTagName("P")[0].innerText
	let data={
		"title":title,
		"content":content
	}
	post(data,"delete").then(res=>{
		show.style.display="none";
		getall_post()
		
	})
}

function createXMLHttpRequest() {
	if (window.ActiveXObject) {
		return new ActiveXObject("Microsoft.XMLHTTP");
	} else if (window.XMLHttpRequest) {
		return new XMLHttpRequest();
	}
}

const url = "http://localhost:3000/"
function post(data, index) {

	return new Promise((resolve, reject) => {
		let xmlHttpRequest = createXMLHttpRequest();
		xmlHttpRequest.open("post", url + index);
		xmlHttpRequest.setRequestHeader("Content-type", "application/json;charset=UTF-8");

		xmlHttpRequest.onreadystatechange = () => {
			if (xmlHttpRequest.readyState === 4) {
				if ((xmlHttpRequest.status >= 200 && xmlHttpRequest.status < 300) || xmlHttpRequest.status == 304) {
					console.log('请求成功');
					resolve(xmlHttpRequest.response)
				} else {
					console.log('请求失败');
					console.log(xmlHttpRequest.status)
				}
			}
		};
		data = JSON.stringify(data)
		console.log(data)
		xmlHttpRequest.send(data)
	})
}
function addlistener() {
	console.log(1)
	let items = document.getElementsByClassName("items")[0]
	items.addEventListener("click", (e) => {
		if (e.target.tagName.toLowerCase() === "div") {
			let data = {
				"title": e.target.getElementsByTagName("h2")[0].innerText,
				"content": e.target.getElementsByTagName("p")[0].innerText
			}
			show(data)
		}
	})
	let find_items = document.getElementsByClassName("find_items")[0]
	find_items.addEventListener("click", (e) => {
		if (e.target.tagName.toLowerCase() === "div") {
			let data = {
				"title": e.target.getElementsByTagName("h2")[0].innerText,
				"content": e.target.getElementsByTagName("p")[0].innerText
			}
			show(data)
		}
	})
}
addlistener()
window.onload=getall_post
