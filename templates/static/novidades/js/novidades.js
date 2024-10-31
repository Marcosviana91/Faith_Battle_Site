// Filtro
var filtro = ''
$('input').on('input', function (e) {
    e.preventDefault();
    filtro = String(e.target.value).toLowerCase()
    const all_cards = Array(...$('aside div.card h5'))
    all_cards.forEach( (card) => {
        console.log(card.parentElement.parentElement);
        if (card.innerText.toLowerCase().includes(filtro)) {
            card.parentElement.parentElement.classList.remove("d-none");
        } else{
            card.parentElement.parentElement.classList.add("d-none");
        }
    })
});

$('.carousel-item')[0].classList.add("active")
const indicators = $('.carousel-indicators button')
indicators[0].classList.add("active")
for (let indicator = 0 ;  indicator < indicators.length ; indicator++) {
    indicators[indicator].dataset['bsSlideTo'] = indicator
}

// Transform o conteúdo de uma elemento .toInnerHtml
const toInnerHtml = $('.toInnerHtml')
for (element of toInnerHtml) {
    console.log(element.innerText)
    element.innerHTML = element.innerText
}


