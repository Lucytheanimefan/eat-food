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


/*-----------------user----------------------*/
function createUser(username, password) {
    $.ajax({
        type: 'POST',
        url: '/createaccount',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        processData: false,
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
        processData: false,
        success: function(response) {
            console.log('in ajax login user');
            console.log(response);
            alert(response);

        }
    });

}
