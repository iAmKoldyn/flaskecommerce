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
    document.body.style.opacity = ".8";
};
sign_up_text.onclick = function() {
    sign_up_popup.style.display = "flex";
    login_popup.style.display = "none";
};
login_text.onclick = function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "flex";
};

close_btns = document.querySelectorAll(".popup_img img");
close_btns[0].addEventListener("click", function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "none";
    popup_all.style.display = "none";
    popup_all.style.zIndex = "0";
    document.body.style.opacity = "1";
});

close_btns[1].addEventListener("click", function() {
    sign_up_popup.style.display = "none";
    login_popup.style.display = "none";
    popup_all.style.display = "none";
    popup_all.style.zIndex = "0";
    document.body.style.opacity = "1";
});
