const cards = document.querySelectorAll(".card");

if (cards.length > 0) {
    cards.forEach((card) => {
        card.addEventListener("click", () => {
            if (card.getAttribute("flipped") == "false") {
                card.setAttribute("flipped", "true")
            } else {
                card.setAttribute("flipped", "false")
            }
        })
    })
}