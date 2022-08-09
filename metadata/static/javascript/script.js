const toggleBtns = document.querySelectorAll(".toggle");
const toggleContent = document.querySelectorAll(".toggle-content");

toggleBtns.forEach((toggleBtn, id) => {
  toggleBtn.addEventListener("click", () => {
    toggleContent[id].classList.toggle("show-faq");
  });
});

