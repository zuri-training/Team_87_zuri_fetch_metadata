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

const dashBoardHamburgerClose = document.querySelector("#sm-hamburger-close");
const dashBoard = document.querySelector(".content-section-sm");
const dashBoardHamburger = document.querySelector("#sm-hamburger");

let navIsOpen = false;

dashBoardHamburgerClose.addEventListener("click", () => {
  dashBoard.classList.remove("show-content-section");
  dashBoardHamburger.classList.remove("hide-sm-hamburger");
});
dashBoardHamburger.addEventListener("click", () => {
  navIsOpen = true;
  dashBoard.classList.add("show-content-section");
  dashBoardHamburger.classList.add("hide-sm-hamburger");
});

if (navIsOpen) {
  console.log(dashBoardHamburger);
}

