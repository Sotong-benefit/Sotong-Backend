// const starContainers = document.getElementsByClassName('star');
// const starImages = document.getElementsByClassName('starImage');

// for (let i = 0; i < starContainers.length; i++) {
//     starContainers[i].addEventListener('click', () => {
//         const currentImageSrc = starImages[i].getAttribute('src');
//         if (currentImageSrc.includes('Star7.png')) {
//             starImages[i].src = '/public/images/Star8.png';
//         } else if (currentImageSrc.includes('Star8.png')) {
//             starImages[i].src = '/public/images/Star7.png';
//         }
//     });
// }






// let selectedButton = null;

// function highlightButton(btnId) {
//     const clickedButton = document.querySelector(`.${btnId}`);
    
//     if (clickedButton === selectedButton) {
//         // 이미 선택된 버튼을 다시 클릭한 경우
//         clickedButton.classList.remove('highlighted');
//         selectedButton = null;
//     } else {
//         // 다른 버튼을 클릭한 경우
//         if (selectedButton) {
//             selectedButton.classList.remove('highlighted');
//         }
//         selectedButton = clickedButton;
//         selectedButton.classList.add('highlighted');
//     }

//     // 스타일 변경
//     const buttons = document.querySelectorAll('.choice-buttons > input');
//     buttons.forEach(button => {
//         if (button !== selectedButton) {
//             button.style.boxShadow = "";
//             button.style.color = "";
//         }
//     });

//     // 선택된 버튼의 스타일 변경
//     if (selectedButton) {
//         selectedButton.style.boxShadow = "2px 2px 4px 0px rgba(0, 0, 0, 0.25) inset";
//         selectedButton.style.color = "#666666";
        
//     }
// }





function writePost() { //글쓰기 버튼
    window.location.href = 'new'; 
}

// function postDetail(){ //게시글상세
//     window.location.href = '/Bulletin-pages/Post-content/Bulletin-post-content.html'; 
// }