// Filtro
var filtro = ''
$('input').on('input', function (e) {
    e.preventDefault();
    filtro = String(e.target.value).toLowerCase()
    const all_cards = Array(...$('.artigo_container_mini'))
    all_cards.forEach( (card) => {
        console.log(card);
        if (card.children[0].innerText.toLowerCase().includes(filtro)) {
            card.classList.remove("d-none");
        } else{
            card.classList.add("d-none");
        }
    })
});

$('.carousel-item')[0].classList.add("active")
const indicators = $('.carousel-indicators button')
indicators[0].classList.add("active")
for (let indicator = 0 ;  indicator < indicators.length ; indicator++) {
    indicators[indicator].dataset['bsSlideTo'] = indicator
}



