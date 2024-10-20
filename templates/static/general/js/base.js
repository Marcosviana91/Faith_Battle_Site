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


