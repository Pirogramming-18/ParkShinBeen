let seconds = 0;
let millis = 0;
let intervalId;
let selectOneBtn;
let selectCount = 0;
let length = 0;

const displaySec = document.querySelector('.clock .sec');
const displayMsec = document.querySelector('.clock .msec');
const startBtn = document.querySelector('.buttons .start');
const stopBtn = document.querySelector('.buttons .stop');
const resetBtn = document.querySelector('.buttons .reset');
const selectAllBtn = document.querySelector('.navbar .selectAllBtn i');
const clearBtn = document.querySelector('.clear');
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
    selectOneBtn = document.querySelector('.laps');
    selectOneBtn.removeEventListener('click', selectBtnClick);
    selectOneBtn.addEventListener('click', selectBtnClick);
    length++;
    checkFull();
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
        <button type="button" class="selectOne iconBtn">
            <i class="fa-regular fa-circle" id="icon"></i>
        </button>
        <span class="sec">${displaySec.textContent}</span>
        <span>:</span>
        <span class="msec">${displayMsec.textContent}</span>
    </li>
    `
    lapList.scrollTop = lapList.scrollHeight;
}

function selectBtnClick(e){
    if(e.target.closest('i')){
        const selectedLap = e.target.closest('li');
        const selectedIcon = e.target;
        if(selectedLap.classList.contains('.checked')){
            selectedLap.classList.remove('.checked');
            changeCheckIcon(selectedIcon, 0);
            selectCount--;
        }
        else{
            selectedLap.classList.add('.checked');
            changeCheckIcon(selectedIcon, 1);
            selectCount++;
        }
        checkFull();
    }
}

function changeCheckIcon(item, check){
    if (check == 1){
        item.classList.remove('fa-circle');
        item.classList.add('fa-circle-check');
    }
    else{
        item.classList.remove('fa-circle-check');
        item.classList.add('fa-circle');
    }
}

selectAllBtn.onclick = () => {
    let check = 0;
    const allBtnLi = selectAllBtn.closest('button');
    const btnList = document.querySelectorAll('.selectOne i');
    btnList.forEach(target => {
        const oneBtnLi = target.closest('li');
        if(allBtnLi.classList.contains('.checked')){
            check = 0;
            if(oneBtnLi.classList.contains('.checked')){
                oneBtnLi.classList.toggle('.checked');
                changeCheckIcon(target, 0);
                selectCount--;
            }
        }
        else{
            check = 1;
            if(!oneBtnLi.classList.contains('.checked')){
                oneBtnLi.classList.toggle('.checked');
                changeCheckIcon(target, 1);
                selectCount++;
            }
        }
    });
    allBtnLi.classList.toggle('.checked');
    changeCheckIcon(selectAllBtn, check);
}

clearBtn.onclick = () => {
    const allBtnLi = selectAllBtn.closest('button')
    allBtnLi.classList.remove('.checked');
    changeCheckIcon(selectAllBtn, 0);
    let lapLi = document.querySelectorAll('.laps li');
    lapLi.forEach(target => {
        if(target.classList.contains('.checked')){
            target.remove();
            selectCount--;
            length--;
        }
    })
}

function checkFull(){
    if(selectCount == length){
        selectAllBtn.closest('button').classList.add('.checked');
        changeCheckIcon(selectAllBtn, 1);
    }
    else{
        selectAllBtn.closest('button').classList.remove('.checked');
        changeCheckIcon(selectAllBtn, 0);
    }
}