const downloadEye = document.querySelectorAll("#eye");

downloadEye.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const id = e.target.dataset.id;
    const DownloadAndDeleteBtn = document.querySelector(`#${id}`);

    DownloadAndDeleteBtn.classList.toggle("show");
  });
});

