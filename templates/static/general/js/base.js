var staff_menu_is_open = false;
var nav_isopen = false

// thanks https://gist.github.com/dragermrb/6d4b7fda5f183524d0ebe4b0a7d8635c
$('.imageUploadResizer').imageUploadResizer({
    max_width: 1281, // Defaults 1000
    max_height: 1281, // Defaults 1000
    quality: 0.8, // Defaults 1
    do_not_resize: ['gif', 'svg'], // Defaults []
});

// clicar para navegar
$('.btn_link').on('click', function () {
    window.location.href = this.dataset['link'];
});

function toggleNavMenu() {
    if (staff_menu_is_open) {
        toggleStaffMenu()
    }
    $(nav_mobile).slideToggle('fast');
    nav_isopen = !nav_isopen
}

$('#btn_menu').on('click', toggleNavMenu );

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

function toggleStaffMenu(){
    if (nav_isopen) {
        toggleNavMenu()
    }
    var positionX = !staff_menu_is_open ? -WIDTH : 0;

    const slide_left = setInterval(function () {
        $('#staff_menu')[0].style.left = positionX + "px";

        if (staff_menu_is_open) {
            positionX -= WIDTH / FPS * 8;
            if (positionX < -WIDTH) {
                clearInterval(slide_left);
                staff_menu_is_open = false
                $('#staff_menu')[0].style.left = -WIDTH + "px";
                $('#btn_staff_menu i')[0].classList.remove('bxs-arrow-from-right')
                $('#btn_staff_menu i')[0].classList.add('bxs-arrow-from-left')
                $('#btn_staff_menu')[0].classList.remove('open')
            }
        } else {
            positionX += WIDTH / FPS * 8;
            if (positionX > 0) {
                clearInterval(slide_left);
                staff_menu_is_open = true
                $('#staff_menu')[0].style.left = "0px";
                $('#btn_staff_menu i')[0].classList.remove('bxs-arrow-from-left')
                $('#btn_staff_menu i')[0].classList.add('bxs-arrow-from-right')
                $('#btn_staff_menu')[0].classList.add('open')
            }
        }
    }, 1000 / FPS)
}

$('#btn_staff_menu').on("click", toggleStaffMenu )


