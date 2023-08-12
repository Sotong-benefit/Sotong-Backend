const starContainers = document.getElementsByClassName('star');
const starImages = document.getElementsByClassName('starImage');

for (let i = 0; i < starContainers.length; i++) {
    starContainers[i].addEventListener('click', () => {
        const currentImageSrc = starImages[i].getAttribute('src');
        if (currentImageSrc.includes('Star7.png')) {
            starImages[i].src = '/public/images/Star8.png';
        } else if (currentImageSrc.includes('Star8.png')) {
            starImages[i].src = '/public/images/Star7.png';
        }
    });
}

function changeImage(selectedRadio) {
    const radio1Img = document.getElementsByClassName("radio1")[0].getElementsByTagName("img")[0];
    const radio2Img = document.getElementsByClassName("radio2")[0].getElementsByTagName("img")[0];
    const radio3Img = document.getElementsByClassName("radio3")[0].getElementsByTagName("img")[0];

    if (selectedRadio === "radio1") {
        radio1Img.src = "/public/images/Ellipse 11.png";
        radio2Img.src = "/public/images/Ellipse 10.png";
        radio3Img.src = "/public/images/Ellipse 10.png";

    } else if (selectedRadio === "radio2") {
        radio1Img.src = "/public/images/Ellipse 10.png";
        radio2Img.src = "/public/images/Ellipse 11.png";
        radio3Img.src = "/public/images/Ellipse 10.png";

    }else if (selectedRadio === "radio3") {
        radio1Img.src = "/public/images/Ellipse 10.png";
        radio2Img.src = "/public/images/Ellipse 10.png";
        radio3Img.src = "/public/images/Ellipse 11.png";
    }
    
}




let selectedButton = null;

function highlightButton(btnId) {
    const clickedButton = document.querySelector(`.${btnId}`);
    
    if (clickedButton === selectedButton) {
        // 이미 선택된 버튼을 다시 클릭한 경우
        clickedButton.classList.remove('highlighted');
        selectedButton = null;
    } else {
        // 다른 버튼을 클릭한 경우
        if (selectedButton) {
            selectedButton.classList.remove('highlighted');
        }
        selectedButton = clickedButton;
        selectedButton.classList.add('highlighted');
    }

    // 스타일 변경
    const buttons = document.querySelectorAll('.choice-buttons > input');
    buttons.forEach(button => {
        if (button !== selectedButton) {
            button.style.boxShadow = "";
            button.style.color = "";
        }
    });

    // 선택된 버튼의 스타일 변경
    if (selectedButton) {
        selectedButton.style.boxShadow = "2px 2px 4px 0px rgba(0, 0, 0, 0.25) inset";
        selectedButton.style.color = "#666666";
        
    }
}

let selectedTag = null;

function toggleTag(button) {
    if (button.style.backgroundColor === 'rgb(255, 178, 178)') {
        button.style.backgroundColor = '';
        button.style.boxShadow = '';
        button.style.color = '';
        selectedTag = null;
    } else {
        if (selectedTag) {
            selectedTag.style.backgroundColor = '';
            selectedTag.style.boxShadow = '';
            selectedTag.style.color = '';
        }
        button.style.backgroundColor = '#CECECE';
        button.style.boxShadow = '2px 2px 4px 0px rgba(0, 0, 0, 0.25) inset';
        selectedTag = button;
    }
}

function moveToAlbum() { //앨범형으로 이동
    window.location.href = '/benefit-album-page/benefit-album-page.html';
}

function moveDetailPost() { //게시글 내용으로 이동
    window.location.href = '/Bulletin-pages/Post-content/Bulletin-post-content.html';
}