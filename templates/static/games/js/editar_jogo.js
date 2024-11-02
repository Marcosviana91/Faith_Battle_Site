

$('.carousel-item')[0].classList.add("active")
// const indicators = $('.carousel-indicators button')
// indicators[0].classList.add("active")
// for (let indicator = 0 ;  indicator < indicators.length ; indicator++) {
//     indicators[indicator].dataset['bsSlideTo'] = indicator
// }

for (let carousel_item of $('#carouselPalymat .carousel-item')) {
    carousel_item.addEventListener("click", () => {
        $('#showPlaytmatModalLabel')[0].innerText = $('#carouselPalymat .carousel-item.active')[0].querySelector('p').innerText.toUpperCase()

        $('#showPlaytmatModalImage')[0].src = $('#carouselPalymat .carousel-item.active')[0].querySelector('img').src
    })
}

function setIframeSrc(btn_src) {
    console.log(btn_src.dataset['deckName'])
    $('#showCardFamilyModalLabel')[0].innerText = btn_src.dataset['deckName']
    $('#verCartas')[0].src = btn_src.href
}
