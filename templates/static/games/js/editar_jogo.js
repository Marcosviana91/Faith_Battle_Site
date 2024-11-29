var card_bottom = 0
var card_left = 0
var cardfamily = 0

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

function setDeck(btn_src) {
    pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0
    console.log(btn_src.dataset)
    $('#showCardFamilyModalLabel')[0].innerText = btn_src.dataset['deckName']
    $('#positionCardModal .modal-body span strong')[0].innerText = btn_src.dataset['deckName']
    cardfamily = String(btn_src.dataset['deckUrl']).split('/')[3]
    
    $('#fake_tabuleiro')[0].src = $('.carousel-item.active img.playmat_image')[0].src
    $('#verCartas')[0].src = btn_src.dataset['deckUrl']
    $('#mydivheader')[0].src = btn_src.dataset['deckImg']
    $('#mydivheader')[0].src = btn_src.dataset['deckImg']
    document.getElementById('mydiv').style.left =  Number(btn_src.dataset['deckPosition'].split(',')[0])+'px'
    document.getElementById('mydiv').style.bottom = Number(btn_src.dataset['deckPosition'].split(',')[1])+'px'
}


// Thanks: https://www.w3schools.com/howto/howto_js_draggable.asp
// Make the DIV element draggable:
dragElement(document.getElementById("mydiv"));
var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

function dragElement(elmnt) {
    if (document.getElementById(elmnt.id + "header")) {
        // if present, the header is where you move the DIV from:
        document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
    } else {
        // otherwise, move the DIV from anywhere inside the DIV:
        elmnt.onmousedown = dragMouseDown;
    }

    function dragMouseDown(e) {
        e = e || window.event;
        e.preventDefault();
        // get the mouse cursor position at startup:
        pos3 = e.clientX;
        pos4 = e.clientY;
        document.onmouseup = closeDragElement;
        // call a function whenever the cursor moves:
        document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
        e = e || window.event;
        e.preventDefault();
        // calculate the new cursor position:
        pos1 = pos3 - e.clientX;
        pos2 = pos4 - e.clientY;
        pos3 = e.clientX;
        pos4 = e.clientY;
        // set the element's new position:
        elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
        elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
    }

    function closeDragElement() {
        // stop moving when mouse button is released:
        document.onmouseup = null;
        document.onmousemove = null;
        const BOARD_HEIGHT = 450
        const CARD_HEIGHT = 60
        const END_TOP = (Number(elmnt.style.top.replace('px', '')) + CARD_HEIGHT * 2 / 3)
        card_bottom = (1 - (END_TOP / BOARD_HEIGHT)) * BOARD_HEIGHT
        card_left = Number(elmnt.style.left.replace('px', ''))
    }
}

function salvarPosicao() {
    const csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]')[0].value
    const form = new FormData()
    form.append('csrfmiddlewaretoken', csrfmiddlewaretoken)
    form.append('deck_id', cardfamily)
    form.append('card_bottom', card_bottom.toFixed(0))
    form.append('card_left', card_left.toFixed(0))
    fetch("/games/deck_position", {
        method: "POST",
        body: form
    }).then(
        (response) => {
            window.location.reload()

        }
    )
}
