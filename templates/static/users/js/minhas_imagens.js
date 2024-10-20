
for (let image of $('.imagem_container')) {
    image.addEventListener('click', (event) => {
        $('.modal-title')[0].innerHTML = $(image)[0].children[1].innerHTML
        $(modal_image)[0].src = $(image)[0].children[0].src
        $(modal_input)[0].value = $(image)[0].children[0].src
        // console.log($(image)[0].children[1].innerHTML)
        // console.log(event.target.src)
    })
}