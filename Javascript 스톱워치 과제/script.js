let seconds = 0;
let millis = 0;
let intervalId;

const displaySec = document.querySelector('.clock .sec');
const displayMsec = document.querySelector('.clock .msec');
const startBtn = document.querySelector('.buttons .start');
const stopBtn = document.querySelector('.buttons .stop');
const resetBtn = document.querySelector('.buttons .reset');
const lapList = document.querySelector('.laps');

function moveClock(){
    millis++;
    if(millis > 99){
        millis = 0;
        seconds++;
        displaySec.textContent = seconds < 10 ? '0' + seconds : seconds;
    }
    displayMsec.textContent = millis < 10 ? '0' + millis : millis;
}

startBtn.onclick = () => { 
    clearInterval(intervalId);
    intervalId = setInterval(moveClock, 10); 
};

stopBtn.onclick = () => {
    clearInterval(intervalId);
    displayLap();
};

resetBtn.onclick = () => {
    clearInterval(intervalId);
    seconds = 0;
    millis = 0;
    displaySec.textContent = "00";
    displayMsec.textContent = "00";
};

function displayLap(){
    lapList.innerHTML = lapList.innerHTML + `
    <li class="lap">
        <button type="button" class="select selectBtn iconBtn">
            <i class="fa-regular fa-circle"></i>
        </button>
        <span class="sec">${displaySec.textContent}</span>
        <span>:</span>
        <span class="msec">${displayMsec.textContent}</span>
    </li>
    `
    lapList.scrollTop = lapList.scrollHeight;
}

// 전체 선택하면 아이콘 다 바뀜, 전체 선택

// 선택하면 아이콘 바뀜

// clear Button 누르면 선택된 항목 삭제