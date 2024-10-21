// clicar para navegar
$('.btn_link').on('click', function () {
    window.location.href = this.dataset['link'];
});

var nav_isopen = false

$('#btn_menu').on('click', function () {
    $(nav_mobile).slideToggle('fast');
    nav_isopen = !nav_isopen
});

var top_position = $(document).scrollTop()
$(document).on('scroll', function (e) {
    if (top_position > $(document).scrollTop()) {
        // console.log("SUBINDO");
        if (nav_isopen) {
            $(nav_mobile).fadeIn();
        }
        $(btn_go_up).fadeIn();
    } else {
        // console.log("DESCENDO");
        $(nav_mobile).fadeOut();
        $(btn_go_up).fadeOut();
    }

    top_position = $(document).scrollTop()
    if (top_position == 0) {
        $(btn_go_up).fadeOut();
    }
});

$(btn_go_up).on("click", function () {
    $(document).scrollTop(0);
})

const FPS = 60
const WIDTH = 300

var is_opened = false;


$(btn_staff_menu).on("click", function() {
    console.log("is_opened", is_opened);
    var positionX = !is_opened ? -WIDTH : 0;
    console.log("positionX", positionX);

    const slide_left = setInterval(function() {
        $('#staff_menu')[0].style.left = positionX + "px";

        if (is_opened) {
            positionX -= WIDTH/FPS*8;
            if (positionX < -WIDTH) {
                clearInterval(slide_left);
                is_opened = !is_opened
                $('#staff_menu')[0].style.left = -WIDTH + "px";
                $('#btn_staff_menu i')[0].classList.remove('bxs-arrow-from-right')
                $('#btn_staff_menu i')[0].classList.add('bxs-arrow-from-left')
            }
        } else {
            positionX += WIDTH/FPS*8;
            if (positionX > 0) {
                clearInterval(slide_left);
                is_opened = !is_opened
                $('#staff_menu')[0].style.left = "0px";
                $('#btn_staff_menu i')[0].classList.remove('bxs-arrow-from-left')
                $('#btn_staff_menu i')[0].classList.add('bxs-arrow-from-right')
            }
        }
    }, 1000/FPS)
})


