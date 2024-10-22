// thanks https://gist.github.com/dragermrb/6d4b7fda5f183524d0ebe4b0a7d8635c
// TODO: adicionar esta função para todas os forms de imagens
$('#playmat_image').imageUploadResizer({
    max_width: 1280, // Defaults 1000
    max_height: 720, // Defaults 1000
    quality: 0.8, // Defaults 1
    do_not_resize: ['gif', 'svg'], // Defaults []
});

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
