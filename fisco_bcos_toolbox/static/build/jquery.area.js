

/*定义三级省市区数据*/


/*关闭省市区选项*/
function clockArea() {
	$("#areaMask").fadeOut();
	$("#areaLayer").animate({"right": "-100%"});
	$('#remen').show();

}

$(function() {

	$("#expressArea").click(function() {
		var body="<br><br><br>";
		for(var i=0; i<localStorage.length;i++){
			body=body+"<li class=\"list\" >"+"Privkey: "+localStorage.key(i)+"</li>"+"<li class=\"list\" >"+"Address: "+localStorage.getItem(localStorage.key(i))+"</li>";

		}
		document.getElementById("remen").innerHTML=body;
		$("#areaMask").fadeIn();
		$("#areaLayer").animate({"right": 0});
	});

	$("#areaMask, #closeArea").click(function() {
		clockArea();
	});

	
});