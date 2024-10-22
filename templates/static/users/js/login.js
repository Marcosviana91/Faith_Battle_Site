const login_bg_list = $('#login_bg')[0].dataset['src'].split(';')
var current_bg_index = 0

setInterval(function() {
    if (current_bg_index < login_bg_list.length-1) {
        current_bg_index +=1
    } else {
        current_bg_index = 0
    }
    console.log(login_bg_list[current_bg_index])
    $('#login_bg')[0].src = login_bg_list[current_bg_index]
}
,10000)