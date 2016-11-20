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
        success: function(response) {
            var data = response["result"];
            localStorage.setItem("mealPlan", data);
            $("#bars").remove();



            $("#main").append('<div id = "bars"><div class="col-md-3">' +
                '<button class="accordion"></button>' +
                '<div class="panel" id="panel1"><p></p></div><button class="accordion"></button><div class="panel" id="panel2">' +
                '<p></p></div></div><div class="col-md-3"><button class="accordion"></button><div class="panel" id="panel3">' +
                '<p></p></div><button class="accordion"></button><div class="panel" id="panel4"><p></p></div></div>' +
                '<div class="col-md-3"><button class="accordion"></button><div class="panel" id="panel5"><p></p></div>' +
                '<button class="accordion"></button><div class="panel" id="panel6"><p></p></div></div>' +
                '<div class="col-md-3"><button class="accordion"></button><div class="panel" id="panel7"><p></p></div>' +
                '<button class="accordion"></button><div class="panel" id="panel8"><p></p></div></div></div>')
            for (var i = 0; i < 8; i++) {
                console.log(data[i]);
                for (var j = 0; j < data[i]["meal_plan"].length; j++) {
                    $("#panel" + (i + 1) + " p").append(data[i]["meal_plan"][j] + "<br>");
                }
            }

            dropDownInteractivity();
            $('.accordion').each(function(index) {
                var i = (index % 4) + 1;
                console.log(i)
                this.style["background-image"] = "url('/static/img/drop_down_" + i + ".png')";
                //this.css("background-image", "url('../img/drop_down_" + index + ".png')")
            });

        }
    });
}


function populateDropdown() {
    var data = localStorage.mealPlan;
    for (var i = 0; i < 8; i++) {
        console.log(data[i]);
        for (var j = 0; j < data[i]["meal_plan"].length; j++) {
            $("#panel" + (i + 1) + " p").append(data[i]["meal_plan"][j] + "\n");
        }
    }
}
/*----------------get user input-------------------------*/
var data = {}
data["restrictions"] = [];
data["feelings"] = [];

var restriction_ids = ["gluten", "wheat", 'soybeans', "peanuts", "dairy", "shellfish", "milk", "eggs", "tree_nut"]
$(document).on('click', '.dropdown-menu li a', function() {
    console.log($(this).text());
    data['activity'] = $(this).text();
});

function getUserInput() {
    //data['username'] = username;
    data['weight'] = $('#weight').val();
    data['height_ft'] = $('#height_ft').val();
    data['height_in'] = $('#height_in').val();
    data['age'] = $('#age').val();
    data['gender'] = $('#gender').val();
    for (var i = 0; i < restriction_ids.length; i++) {
        if ($("#" + restriction_ids[i]).is(':checked')) {
            data["restrictions"].push(restriction_ids[i]);
        }
    }
    return data;
}

$('#go').click(function() {
    var data = getUserInput();
    console.log(data);
    populateResults(data);
});

/*-----------------user----------------------*/
function createUser(username, password) {
    console.log("Username: " + username);
    console.log("password: " + password);
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

function edit(username, gender, age, height_feet, height_inches, weight, activity_level, restrictions) {
    $.ajax({
        type: 'POST',
        url: '/edit',
        data: JSON.stringify({ "username": username, "gender": gender, "age": age, "height_ft": height_feet,
        "height_in": height_inches, "weight": weight, "activity_level": activity_level, "restrictions": restrictions}),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log('in ajax edit user');
            console.log(response);
            alert(response);

        }
    });

}

function get() {
    $.ajax({
        type: 'GET',
        url: '/get_info',
        dataType: 'json',
        success: function(response) {
            console.log('in ajax edit user');
            console.log(response);
            var jsonObj = $.parseJSON(response);
            var html = '<table border="1">';
            $.each(jsonObj, function(key, value){
                html += '<tr>';
                html += '<td>' + key + '</td>';
                html += '<td>' + value + '</td>';
                html += '</tr>';
            });
            html += '</table>';

            $('div').html(html);

        }
    });
}

/*-----------------------journal---------------------*/

var feelings_ids = ["happy", "content", "neutral", "excited", "angry", "frustrated", "sick", "sad", "disappointed"];

feelings_ids.map(function(id) {
    $("#" + id).click(function() {
        console.log($("#" + id));
        var val = $("#" + id).attr("value");
        console.log(val);
        $("#" + id).attr("value", -1 * parseInt(val));
    });
})

function feelingsToArray() {
    var data = [];
    for (var i = 0; i < feelings_ids.length; i++) {
        if (parseInt($("#" + feelings_ids[i]).attr("value")) > 0) {
            data.push(feelings_ids[i]);
        }
    }
    return data;
}

function enterFeelings() {
    var feelingsArray = feelingsToArray();
    var notes = $("#notes").val();
    var food = $("#food").val();
    $.ajax({
        type: 'POST',
        url: '/writeEmotions',
        data: JSON.stringify({ "emotions": feelingsArray, "notes": notes, "food": food }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success");
        }
    });
}

function getCalendar() {
    $.ajax({
        type: 'POST',
        url: '/getCalendar',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            var data = response["result"];
            makeCalendar(data);
        }
    });
}

function makeCalendar(data) {
    $("#calendar").append("table");
    for (var i = 0; i < data.length; i++) {
        $("#calendar table").append();
    }
}
