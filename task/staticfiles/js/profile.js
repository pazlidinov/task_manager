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

let burger = document.querySelector(".burger");
let sidebar = document.querySelector(".sidebar");
let crossButton = document.querySelector(".cross-button");

burger.addEventListener("click", ()=>{
    sidebar.classList.add("sidebar_active");
    document.body.classList.add("body_active")
})
crossButton.addEventListener("click", ()=>{
    sidebar.classList.remove("sidebar_active");
    document.body.classList.remove("body_active")
})

let container = document.querySelectorAll(".container");

burger.addEventListener("click", ()=>{
    sidebar.classList.add("sidebar_active");
    document.body.classList.add("body_active");
    container.forEach(element => {
        element.classList.add("container_active")
    });
})
crossButton.addEventListener("click", ()=>{
    sidebar.classList.remove("sidebar_active");
    document.body.classList.remove("body_active")
    container.forEach(element => {
        element.classList.remove("container_active")
    });
})

const xValues = [50,60,70,80,90,100,110,120,130,140,150];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      fill: false,
      lineTension: 0,
      backgroundColor: "rgba(0,0,255,1.0)",
      borderColor: "rgba(0,0,255,0.1)",
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    scales: {
      yAxes: [{ticks: {min: 6, max:16}}],
    }
  }
});

let modal = document.querySelector(".modal");
let modalbtn = document.querySelector(".main__projects--button");
let modalRemove = document.querySelector(".modal__button")

modalbtn.addEventListener("click", ()=>{
    modal.classList.add("modal_active");
    document.body.classList.add("body_active");
    container.forEach(element => {
        element.classList.add("container_active")
    });
})
modalRemove.addEventListener("click", ()=>{
    modal.classList.remove("modal_active");
    document.body.classList.remove("body_active");
    container.forEach(element => {
        element.classList.remove("container_active")
    });
})