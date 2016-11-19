/*------------create dropdowns---------------*/
function dropDownInteractivity() {

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            this.classList.toggle("active");
            this.nextElementSibling.classList.toggle("show");
        }
    }
}

dropDownInteractivity();

/*------------------Populate dropdowns---------------------*/
var data = {"dummyinfo":42}
populateResults(data);
function populateResults(data) {
    $.ajax({
        type: "POST",
        url: "/getResults",
        contentType: "application/json; charset=utf-8",
        dataType: 'json',
        data: JSON.stringify(data),
        success: function(response) {
        	console.log(response);

        }
    });
}
/*----------------get user input-------------------------*/
function getUserInput(){
	var data = {}
	data["weight"]=$("#weight").val();
	data["height"]=$("#height").val();
	data["age"] = $("#age").val();
	data["gender"] = $("#gender").val();
	return data;
}

function sendInputToBackend(data){
	
}

$("#go").click(function(){
	var data = getUserInput();
})
