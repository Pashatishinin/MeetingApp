// active hamburger menu

let menuIcon = document.querySelector(".menu-icon");
let navbar = document.querySelector(".navbar")
menuIcon.addEventListener("click",()=>{
    menuIcon.classList.toggle("active");
    navbar.classList.toggle("active");
    document.body.classList.toggle("open");
});






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

//============================== Restaurant modal window ==============================//
document.getElementById("open-modal-btn").addEventListener("click", function() {
    document.getElementById("my-modal").classList.add("open")
})

document.getElementById("close-my-modal-btn").addEventListener("click", function() {
    document.getElementById("my-modal").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal").classList.remove("open")
    }
});
document.querySelector("#my-modal .modal_box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});

document.getElementById("my-modal").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});

//============================== Coffee Station modal window ==============================//
document.getElementById("open-modal-btn2").addEventListener("click", function() {
    document.getElementById("my-modal2").classList.add("open")
})

document.getElementById("close-my-modal-btn2").addEventListener("click", function() {
    document.getElementById("my-modal2").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal2").classList.remove("open")
    }
});
document.querySelector("#my-modal2 .modal_box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});

document.getElementById("my-modal2").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});

//============================== CoffeeBar Soho modal window ==============================//
document.getElementById("open-modal-btn3").addEventListener("click", function() {
    document.getElementById("my-modal3").classList.add("open")
})

document.getElementById("close-my-modal-btn3").addEventListener("click", function() {
    document.getElementById("my-modal3").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal3").classList.remove("open")
    }
});
document.querySelector("#my-modal3 .modal_box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});

document.getElementById("my-modal3").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});

//============================== CoffeeBar Noho modal window ==============================//
document.getElementById("open-modal-btn4").addEventListener("click", function() {
    document.getElementById("my-modal4").classList.add("open")
})

document.getElementById("close-my-modal-btn4").addEventListener("click", function() {
    document.getElementById("my-modal4").classList.remove("open")
})

window.addEventListener('keydown', (e) => {
    if (e.key === "Escape") {
        document.getElementById("my-modal4").classList.remove("open")
    }
});
document.querySelector("#my-modal4 .modal_box").addEventListener('click', event => {
    event._isClickWithInModal = true;
});

document.getElementById("my-modal4").addEventListener('click', event => {
    if (event._isClickWithInModal) return;
    event.currentTarget.classList.remove('open');
});


//============================== USERS  modal window ==============================//












