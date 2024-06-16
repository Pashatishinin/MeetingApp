// switch beetwen weeks

const buttons = document.querySelectorAll('.week_buttons button');
const contents = document.querySelectorAll('.content');

buttons.forEach((button, index) => {
    button.addEventListener('click', () => {
        contents.forEach(content => content.style.display = 'none');
        contents[index].style.display = 'block';
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});

function myPassword() {
    var a = document.getElementById("password")
    var b = document.getElementById("eye")
    var c = document.getElementById("eye-slash")

    if(a.type === "password"){
        a.type = 'text'
        b.style.opacity = '0';
        c.style.opacity = "1";
    }else{
        a.type = "password"
        b.style.opacity = '1';
        c.style.opacity = "0";

    }
}

function myPassword2() {
    var a = document.getElementById("confirm_password")
    var b = document.getElementById("eye-2")
    var c = document.getElementById("eye-slash-2")

    if(a.type === "password"){
        a.type = 'text'
        b.style.opacity = '0';
        c.style.opacity = "1";
    }else{
        a.type = "password"
        b.style.opacity = '1';
        c.style.opacity = "0";

    }
}


document.addEventListener('DOMContentLoaded', function () {
    var popupBtn = document.getElementById('popup-btn');
    var closeBtn = document.getElementById('close-btn');
    var popup = document.getElementById('popup');
    var overlay = document.getElementById('overlay');

    popupBtn.addEventListener('click', function () {
        popup.style.display = 'block';
        overlay.style.display = 'block';
    });

    closeBtn.addEventListener('click', function () {
        popup.style.display = 'none';
        overlay.style.display = 'none';
    });

    overlay.addEventListener('click', function () {
        popup.style.display = 'none';
        overlay.style.display = 'none';
    });
});
