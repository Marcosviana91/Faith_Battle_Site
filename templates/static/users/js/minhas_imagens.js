
for (let image of $('.imagem_container')) {
    image.addEventListener('click', (event) => {
        $('.modal-title')[0].innerHTML = $(image)[0].children[1].innerHTML
        $(modal_image)[0].src = $(image)[0].children[0].src
        $(modal_input)[0].value = $(image)[0].children[0].src
        $('#btn_apagar_imagem.btn_link')[0].dataset['link'] = '?del='+$(image)[0].children[1].innerHTML
        // console.log($('#btn_apagar_imagem.btn_link')[0].dataset)
    })
}

function copyInput(element_id) {
    if (!window.isSecureContext) {
        window.alert('Não foi possível acessar a área de transferência.')
    } else {
        var copyText = document.getElementById(element_id);
        copyText.select();
        copyText.setSelectionRange(0, 99999);
        navigator.clipboard.writeText(copyText.value)
        $('#btn_copy_popover').fadeIn()
        setTimeout(() => {
            $('#btn_copy_popover').fadeOut()
        }, 1500)
    }
}

const images_info = JSON.parse($('#images_info')[0].dataset['images_info'])
const imagem_container = $('.imagem_container')
for (let element = 0; element < imagem_container.length; element++) {
    imagem_container[element].lastElementChild.innerHTML ='size: '+images_info[element]['size']+'MB'
}
