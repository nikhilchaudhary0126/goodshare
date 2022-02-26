const left = document.querySelector(".left");
const container = document.querySelector(".middle");
const right = document.querySelector(".right");
const container = document.querySelector(".container");

left.addEventListener("mouseenter", () => {
  container.classList.add("hover-left");
});

left.addEventListener("mouseleave", () => {
  container.classList.remove("hover-left");
});

middle.addEventListener("mouseenter", () => {
  container.classList.add("hover-middle");
});

middle.addEventListener("mouseleave", () => {
  container.classList.remove("hover-middle");
});