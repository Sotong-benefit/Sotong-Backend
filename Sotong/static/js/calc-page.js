const buttons = document.querySelectorAll('.option-btn');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        buttons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
    });
});

function goToCalcResultPage() {
    window.location.href = '/calc-res-page/calc-res-page.html';
}

function goToPrev() { //지난 결과 다시보기 버튼
    window.location.href = '#'; 
}

function showAlert() { //저장버튼
    alert("저장되었습니다.");
}

