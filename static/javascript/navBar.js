const Hamburger = document.querySelector(".hamburger");
const HamburgerClose = document.querySelector(".hamburger-close");
const navigation = document.querySelector(".sm-navigation");

Hamburger.addEventListener("click", () => {
  navigation.classList.add("show-navigation");
});

HamburgerClose.addEventListener("click", () => {
  navigation.classList.remove("show-navigation");
});

/* ======================================= */
/* ============= DASHBORD JAVASCRIPT ==== */

const profileLinkWrapper = document.querySelector(".sm-profile-link-wrapper");
const dropDownArrow = document.querySelector(".dashboard-arrow");

dropDownArrow.addEventListener("click", () => {
  dropDownArrow.classList.toggle("rotate-drop-down");
  profileLinkWrapper.classList.toggle("show-profile-link");
});

