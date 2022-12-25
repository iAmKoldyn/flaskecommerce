let element = document.querySelector(".icons_btn4");
let popup_all = document.querySelector(".popup_all");
let login_popup = document.querySelector(".login_popup");
let sign_up_text = document.querySelector(".sign_up_text");
let login_text = document.querySelector(".login_text");
let sign_up_popup = document.querySelector(".sign_up_popup");
element.onclick = function() {
    popup_all.style.display = "flex";
    login_popup.style.display = "flex";
    popup_all.style.zIndex = "100";
    let divs = document.querySelectorAll('body *');
    for (let i = 0; i < divs.length; i++){
        divs[i].style.opacity = '.8';
    }
    let popup_items = document.querySelectorAll('.popup_all *');
    for (let i = 0; i < popup_items.length; i++){
        popup_items[i].style.opacity = 1;
    }
    document.querySelector('.popup_all').style.opacity = 1;
};
sign_up_text.onclick = function() {
    sign_up_popup.style.display = "flex";
    login_popup.style.display = "none";
};
login_text.onclick = function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "flex";
};

close_btns = document.querySelectorAll(".popup_img");
close_btns[0].addEventListener("click", function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "none";
    popup_all.style.display = "none";
    let divs = document.querySelectorAll('body *');
    for (let i = 0; i < divs.length; i++){
        divs[i].style = undefined;
    }
    let popup_items = document.querySelectorAll('.popup_all *');
    for (let i = 0; i < popup_items.length; i++){
        popup_items[i].style.opacity = 0;
    }
    document.querySelector('.popup_all').style.opacity = 0;
});

close_btns[1].addEventListener("click", function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "none";
    popup_all.style.display = "none";
    let divs = document.querySelectorAll('body *');
    for (let i = 0; i < divs.length; i++){
        divs[i].style = undefined;
    }
    let popup_items = document.querySelectorAll('.popup_all *');
    for (let i = 0; i < popup_items.length; i++){
        popup_items[i].style.opacity = 0;
    }
    document.querySelector('.popup_all').style.opacity = 0;
});
