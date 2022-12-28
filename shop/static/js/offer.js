let b = 0;
function next()
{
    if ((b >= 0) && (b < document.getElementsByClassName("swiper-item").length - 1)){
        document.getElementsByClassName("swiper-item")[b].className = "swiper-item";
        document.getElementsByClassName("list-inline-item")[b].className = "list-inline-item";
        b++;
        document.getElementsByClassName("swiper-item")[b].className += " active";
        document.getElementsByClassName("list-inline-item")[b].className += " item-active";
    }
}
function prev()
{
    if ((b > 0) && (b <= document.getElementsByClassName("swiper-item").length)){
        document.getElementsByClassName("swiper-item")[b].className = "swiper-item";
        document.getElementsByClassName("list-inline-item")[b].className = "list-inline-item";
        b--;
        document.getElementsByClassName("swiper-item")[b].className += " active";
        document.getElementsByClassName("list-inline-item")[b].className += " item-active";
    }
}
