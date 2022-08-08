const file = document.querySelector("#id_upload_file");
const fileLabel = document.querySelector("#file-label");
const upload = document.querySelector(".upload");
const cloud = document.querySelector(".cloud");
const fileName = document.querySelector(".file-name");

file.addEventListener("change", () => {
  fileName.textContent = file.value.split("\\").pop();
  upload.classList.add("hide-upload");
  cloud.classList.remove("hide-upload");
  metadataBtn.classList.remove("hide-upload");
});

