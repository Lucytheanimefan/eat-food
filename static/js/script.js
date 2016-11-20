/*------------create dropdowns---------------*/
function dropDownInteractivity() {

    var acc = document.getElementsByClassName('accordion');
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            this.classList.toggle('active');
            this.nextElementSibling.classList.toggle('show');
        }
    }
}

dropDownInteractivity();

/*------------------Populate dropdowns---------------------*/
function populateResults(data) {
    $.ajax({
        type: 'POST',
        url: '/getResults',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        processData: false,
        success: function(response) {
            console.log('in ajax');
            console.log(response);

        }
    });
}
/*----------------get user input-------------------------*/
var data = {}
data["restrictions"] = [];
data["feelings"] = [];

$(document).on('click', '.dropdown-menu li a', function() {
    console.log($(this).text());
    data['activity'] = $(this).text();
});

function getUserInput() {
    data['username'] = username;
    data['weight'] = $('#weight').val();
    data['height_ft'] = $('#height_ft').val();
    data['height_in'] = $('#height_in').val();
    data['age'] = $('#age').val();
    data['gender'] = $('#gender').val();
    return data;
}

$('#go').click(function() {
    var data = getUserInput();
    console.log(data);
    populateResults(data);
});

$('input:checkbox.restriction').each(function() {
    data["restrictions"].push((this.checked ? $(this).val() : ""));
});

var d = document
var feelingsButton = d.getElementById('submit')
var feelings = d.getElementById('feelingsForm')

feelingsButton.onclick = function () {
    var feelingsArray = feelingsToArray(feelings.children)
    //console.log(feelings.children[0]);
}

function feelingsToArray (inputs) {
    var array = [];
    for (var i = 0; i < inputs.length; i++) {
        var label = $(inputs[i].id);
        console.log(inputs[i].children.children)
        if (inputs[i].checked)
            arraya.push(inputs[i].value);
    }
    return array;
}

$('label.myClass select').each(function(){
    var inputVal = $(this).val();
});

/*-----------------user----------------------*/
function createUser(username, password) {
	console.log("Username: "+username);
	console.log("password: "+password);
    $.ajax({
        type: 'POST',
        url: '/createaccount',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log('in ajax create user');
            console.log(response);
            alert(response);

        }
    });
}

function login(username, password) {
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log('in ajax login user');
            console.log(response);
            alert(response);

        }
    });

}

function enterFeelings(feelings) {
    console.log(feelings)
    data["feelings"] = feelings;

}
