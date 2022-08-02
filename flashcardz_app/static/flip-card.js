const cards = document.querySelectorAll(".card");

function handleFlip(e, card) {
    if (card.getAttribute("flipped") == "false") {
        card.setAttribute("flipped", "true")
    } else {
        card.setAttribute("flipped", "false")
    }
}

if (cards.length > 0) {
    cards.forEach((card) => {
        const flip_btn = card.querySelector(".flip-btn");
        if (flip_btn) {
            flip_btn.addEventListener("click", (e) => handleFlip(e, card));
        } else {
            card.addEventListener("click", (e) => handleFlip(e, card));
        }
    })
}