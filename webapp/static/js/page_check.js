window.onload = function() {
	switch(flag) {
		case "first":
			document.querySelector("a[name=previous]").style.display = "none";
			break;
		case "last":
			document.querySelector("a[name=next]").style.display = "none";
			break;
	}
}
