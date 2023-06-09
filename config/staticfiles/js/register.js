let slideIndex = 1;
showSlides(slideIndex)

function plusSlides(n) {
    showSlides(slideIndex += n)
}
function currentSlide(n) {
    showSlides(slideIndex = n)
}
function showSlides(n) {
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none"
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "")
    }
    slides[slideIndex - 1
    ].style.display = "flex";
    dots[slideIndex - 1].className += " active"
}

const months = [
    "yanvar",
    "fevrel",
    "mart",
    "aprel",
    "may",
    "iyun",
    "iyul",
    "avgust",
    "sentabr",
    "oktabr",
    "noyabr",
    "dekabr",
];
function load() {
    let nowDay = document.querySelector(".day");
    let nowYear = document.querySelector(".year")
    let nowHour = document.querySelector(".hour");
    let nowMinute = document.querySelector(".minute");
    let nowSecond = document.querySelector(".second");
    let newDate = new Date();

    let day = newDate.getDate();
    let monthNumber = newDate.getMonth();
    let year = newDate.getFullYear();
    let hour = newDate.getHours();
    let minute = newDate.getMinutes();
    let second = newDate.getSeconds();

    nowDay.textContent = `${day}-${months[monthNumber]}`;
    nowYear.textContent = `${year}`
    nowHour.textContent = `${hour = (hour < 10) ? "0" + hour : hour} :`;
    nowMinute.textContent = `${minute = (minute < 10) ? "0" + minute : minute} :`;
    nowSecond.textContent = `${second = (second < 10) ? "0" + second : second}`;
}

setInterval(load, 999);