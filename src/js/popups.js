function toggleElement(element){
	$(element).fadeToggle(500);
}

function killOldestChild(parent){
	parent.children().last().remove();
}

function countChildren(children){
	return children.length
}

function checkChildren(){
	parent = $('#tweets').find('ol');
	if(countChildren(parent.children()) > 4){
		console.log("Current childcount: "+countChildren(parent.children()));
		killOldestChild(parent);
	}
}

$(document).ready(function(){
	var inverval = setInterval(function(){
		checkChildren();
	}, 500);
});