// 이미지 업로드 js
function DropFile(dropAreaId, fileListId) {
  let dropArea = document.getElementById(dropAreaId);
  let fileList = document.getElementById(fileListId);

  function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  }

  function highlight(e) {
    preventDefaults(e);
    dropArea.classList.add("highlight");
  }

  function unhighlight(e) {
    preventDefaults(e);
    dropArea.classList.remove("highlight");
  }

  function handleDrop(e) {
    unhighlight(e);
    let dt = e.dataTransfer;
    let files = dt.files;

    handleFiles(files);

    const fileList = document.getElementById(fileListId);
    if (fileList) {
      fileList.scrollTo({ top: fileList.scrollHeight });
    }
  }

  function handleFiles(files) {
    files = [...files];
    // files.forEach(uploadFile);
    files.forEach(previewFile);
  }

  function previewFile(file) {
    console.log(file);
    renderFile(file);
  }

  function renderFile(file) {
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = function () {
      let img = dropArea.getElementsByClassName("preview")[0];
      img.src = reader.result;
      img.style.display = "block";
    };
  }

  dropArea.addEventListener("dragenter", highlight, false);
  dropArea.addEventListener("dragover", highlight, false);
  dropArea.addEventListener("dragleave", unhighlight, false);
  dropArea.addEventListener("drop", handleDrop, false);

  return {
    handleFiles,
  };
}

const dropFile = new DropFile("drop-file", "files");

// 블러처리
document
  .getElementById("registrationFile")
  .addEventListener("click", function () {
    var uploadBox = document.getElementById("drop-file");
    var uploadCompleteMessage = document.getElementById(
      "uploadCompleteMessage"
    );

    // 블러 처리
    uploadBox.style.filter = "blur(5px)";

    // 등록 완료 메시지 표시
    uploadCompleteMessage.style.display = "block";

    // 3초 후에 블러 해제 및 메시지 숨김
    setTimeout(function () {
      uploadBox.style.filter = "none";
      uploadCompleteMessage.style.display = "none";
    }, 2000);
  });

// 헤택받기 블러처리
// 클릭 이벤트 리스너를 등록
document.getElementById("benefitItem1").addEventListener("click", function () {
  showConfirmationPopup();
});

document.getElementById("benefitItem2").addEventListener("click", function () {
  showConfirmationPopup();
});

function showConfirmationPopup() {
  var benefitWrap = document.querySelector(".TongTong-benefit-wrap");
  var confirmationPopup = document.createElement("div");
  confirmationPopup.className = "confirmation-popup";

  var confirmationText = document.createElement("p");
  confirmationText.textContent =
    "통통이 5개를 사용하여 이 혜택을 받으시겠습니까?";
  confirmationText.className = "confirmation-text";
  confirmationPopup.appendChild(confirmationText);

  var buttonContainer = document.createElement("div");
  buttonContainer.className = "button-container";

  var yesButton = document.createElement("button");
  yesButton.textContent = "네";
  yesButton.className = "confirmation-button";
  yesButton.addEventListener("click", function () {
    var completeText = document.createElement("p");
    completeText.textContent = "혜택 받기가 완료되었습니다";
    completeText.className = "complete-text";
    confirmationPopup.innerHTML = ""; // 내용 초기화
    confirmationPopup.appendChild(completeText);

    setTimeout(function () {
      benefitWrap.style.filter = "none"; // 블러 해제
      confirmationPopup.style.display = "none"; // 팝업 숨김
    }, 2000); // 2초 후에 블러 해제 및 팝업 숨김
  });

  var noButton = document.createElement("button");
  noButton.textContent = "아니오";
  noButton.className = "confirmation-button";
  noButton.addEventListener("click", function () {
    benefitWrap.style.filter = "none"; // 블러 해제
    confirmationPopup.style.display = "none"; // 팝업 숨김
  });

  buttonContainer.appendChild(yesButton);
  buttonContainer.appendChild(noButton);

  confirmationPopup.appendChild(buttonContainer);

  document.body.appendChild(confirmationPopup);

  // 블러 처리
  benefitWrap.style.filter = "blur(5px)";
}

// 통통이 구매
// 통통이 구매 부분 클릭 시 블러 처리와 메시지 표시
document.getElementById("buyItem1").addEventListener("click", function () {
  showCustomPurchasePopup("3개", "2000원");
});

document.getElementById("buyItem2").addEventListener("click", function () {
  showCustomPurchasePopup("5개", "3000원");
});

// 통통이 구매 확인 팝업 보여주는 함수
function showCustomPurchasePopup(itemCount, itemPrice) {
  var buyContainer = document.querySelector(".TongTong-buy-container");
  var purchasePopup = document.createElement("div");
  purchasePopup.className = "purchase-popup custom-buy-popup";

  var purchaseText = document.createElement("p");
  purchaseText.textContent = "통통이 " + itemCount + "를 구매하시겠습니까? ";
  purchaseText.className = "purchase-text";
  purchasePopup.appendChild(purchaseText);

  var buttonContainer = document.createElement("div");
  buttonContainer.className = "button-container";

  var yesButton = document.createElement("button");
  yesButton.textContent = "네";
  yesButton.className = "purchase-button";
  yesButton.addEventListener("click", function () {
    var completeText = document.createElement("p");
    completeText.textContent = "구매 완료하였습니다";
    completeText.className = "complete-text";
    purchasePopup.innerHTML = ""; // 내용 초기화
    purchasePopup.appendChild(completeText);

    setTimeout(function () {
      buyContainer.style.filter = "none"; // 블러 해제
      purchasePopup.style.display = "none"; // 팝업 숨김
    }, 2000); // 2초 후에 블러 해제 및 팝업 숨김
  });

  var noButton = document.createElement("button");
  noButton.textContent = "아니오";
  noButton.className = "purchase-button";
  noButton.addEventListener("click", function () {
    buyContainer.style.filter = "none"; // 블러 해제
    purchasePopup.style.display = "none"; // 팝업 숨김
  });

  buttonContainer.appendChild(yesButton);
  buttonContainer.appendChild(noButton);

  purchasePopup.appendChild(buttonContainer);

  document.body.appendChild(purchasePopup);

  // 블러 처리
  buyContainer.style.filter = "blur(5px)";
}
