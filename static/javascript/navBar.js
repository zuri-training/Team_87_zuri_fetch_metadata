const Hamburger = document.querySelector(".hamburger");
const HamburgerClose = document.querySelector(".hamburger-close");
const navigation = document.querySelector(".sm-navigation");

Hamburger.addEventListener("click", () => {
  navigation.classList.add("show-navigation");
});

HamburgerClose.addEventListener("click", () => {
  navigation.classList.remove("show-navigation");
});

