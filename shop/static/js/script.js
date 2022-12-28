let a = 0;
function next()
{
    if ((a >= 0) && (a < document.getElementsByClassName("swiper-wrapper").length - 1)){
        document.getElementsByClassName("swiper-wrapper")[a].className = "swiper-wrapper";
        document.getElementsByClassName("list-inline-item")[a].className = "list-inline-item";
        a++;
        document.getElementsByClassName("swiper-wrapper")[a].className += " active";
        document.getElementsByClassName("list-inline-item")[a].className += " item-active";
    }
}
function prev()
{
    if ((a > 0) && (a <= document.getElementsByClassName("swiper-wrapper").length)){
        document.getElementsByClassName("swiper-wrapper")[a].className = "swiper-wrapper";
        document.getElementsByClassName("list-inline-item")[a].className = "list-inline-item";
        a--;
        document.getElementsByClassName("swiper-wrapper")[a].className += " active";
        document.getElementsByClassName("list-inline-item")[a].className += " item-active";
    }
}
