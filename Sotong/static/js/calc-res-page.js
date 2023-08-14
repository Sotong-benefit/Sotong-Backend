// calc-res-page.js

const resultValue = parseInt(document.querySelector('.result').textContent);

const resSection = document.querySelector('.res-section');

if (resultValue === 1) {
    resSection.style.backgroundColor = 'rgba(255, 178, 178, 0.5)';
}
else if (resultValue === 2) {
    resSection.style.backgroundColor = 'rgba(255, 210, 178, 0.5)';
}
else if (resultValue === 3) {
    resSection.style.backgroundColor = 'rgba(255, 243, 178, 0.5)';
}
else if (resultValue === 4) {
    resSection.style.backgroundColor = 'rgba(204, 242, 180, 0.5)';
}
else if (resultValue === 5) {
    resSection.style.backgroundColor = 'rgba(184, 241, 214, 0.5)';
}
else if (resultValue === 6) {
    resSection.style.backgroundColor = 'rgba(178, 236, 255, 0.5)';
}
else if (resultValue === 7) {
    resSection.style.backgroundColor = 'rgba(178, 204, 255, 0.5)';
}
else if (resultValue === 8) {
    resSection.style.backgroundColor = 'rgba(217, 203, 255, 0.5)';
}
else if (resultValue === 9) {
    resSection.style.backgroundColor = 'rgba(240, 199, 255, 0.5)';
}
else if (resultValue === 10) {
    resSection.style.backgroundColor = 'rgba(255, 200, 236, 0.5)';
}
else {
    resSection.style.backgroundColor = '#B2EDFF';
}


const communitySections = document.getElementsByClassName('reco-num');
console.log(communitySections)
Array.from(communitySections).forEach(communitySection => {

    if (resultValue === 1) {
        communitySection.style.backgroundColor = 'rgba(255, 178, 178, 0.5)';
    }
    else if (resultValue === 2) {
        communitySection.style.backgroundColor = 'rgba(255, 210, 178, 0.5)';
    }
    else if (resultValue === 3) {
        communitySection.style.backgroundColor = 'rgba(255, 243, 178, 0.5)';
    }
    else if (resultValue === 4) {
        communitySection.style.backgroundColor = 'rgba(204, 242, 180, 0.5)';
    }
    else if (resultValue === 5) {
        communitySection.style.backgroundColor = 'rgba(184, 241, 214, 0.5)';
    }
    else if (resultValue === 6) {
        communitySection.style.backgroundColor = 'rgba(178, 236, 255, 0.5)';
    }
    else if (resultValue === 7) {
        communitySection.style.backgroundColor = 'rgba(178, 204, 255, 0.5)';
    }
    else if (resultValue === 8) {
        communitySection.style.backgroundColor = 'rgba(217, 203, 255, 0.5)';
    }
    else if (resultValue === 9) {
        communitySection.style.backgroundColor = 'rgba(240, 199, 255, 0.5)';
    }
    else if (resultValue === 10) {
        communitySection.style.backgroundColor = 'rgba(255, 200, 236, 0.5)';
    }
    else {
        communitySection.style.backgroundColor = '#B2EDFF';
    }
});



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


function showAlert() { //저장버튼
    alert("저장되었습니다.");
}

function showMore() { //더보기버튼
    window.location.href = '/benefit-album-page/benefit-album-page.html';
}

function actDetail() { //복지혜택 추천 상세
    window.location.href = '/find-benefit-detail/find-benefit-bulletin.html';
}


function postDetail() { //게시글추천 상세
    window.location.href = '/Bulletin-pages/Post-content/Bulletin-post-content.html';
}