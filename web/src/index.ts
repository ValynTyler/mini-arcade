const count_btn = document.querySelector("button")

let count = 0

count_btn?.addEventListener('click', () => {
  count += 1
  count_btn.textContent = count.toString()
})