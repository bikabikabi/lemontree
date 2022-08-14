const url = "http://localhost:3000/"
function post(data, index) {
	return new Promise((resolve, reject) => {
		let xhr = createXMLHttpRequest();
		xhr.open("post", url + index);
		xhr.setRequestHeader("Content-type", "application/json;charset=UTF-8");

		xhr.onreadystatechange = () => {
			if (xhr.readyState === 4) {
				if ((xhr.status >= 200 && xhr.status < 300) || xhr.status == 304) {
					console.log('请求成功');
					resolve(xhr.response)
				} else {
					console.log('请求失败');
					console.log(xhr.status)
				}
			}
		};
		data = JSON.stringify(data)
		console.log(data)
		xhr.send(data)
	})
}
function createXMLHttpRequest() {
	if (window.ActiveXObject) {
		return new ActiveXObject("Microsoft.XMLHTTP");
	} else if (window.XMLHttpRequest) {
		return new XMLHttpRequest();
	}
}