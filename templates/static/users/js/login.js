// Change background
const login_bg_list = $('#login_bg')[0].dataset['src'].split(';')
var current_bg_index = 0
setInterval(function () {
    if (current_bg_index < login_bg_list.length - 1) {
        current_bg_index += 1
    } else {
        current_bg_index = 0
    }
    $('#login_bg')[0].src = login_bg_list[current_bg_index]
}
    , 10000)

const form_login = $('#form_login')
const form_create_user = $('#form_create_user')
const avatar_container = $('#avatar_container')

function showLoginForm() {
    form_login.show()
    form_create_user.hide()
    avatar_container.hide()
}

function showCreateForm() {
    form_login.hide()
    form_create_user.show()
    avatar_container.hide()
}

function showAvatarForm() {
    form_login.hide()
    form_create_user.hide()
    avatar_container.show()
}

for (var avatar of $('.avatar_selector')) {
    avatar.firstElementChild.innerHTML = avatar.firstElementChild.innerHTML.split('.')[0]
}

const avatar_hidden_input = $('#avatar_hidden')[0]
$('.avatar_selector').on("click", function (e) {
    avatar_hidden_input.firstElementChild.value = e.currentTarget.dataset['avatar_name']
    avatar_hidden_input.lastElementChild.src = e.currentTarget.dataset['src']
    showCreateForm()
})

// Check tab
const search_params = new URLSearchParams(window.location.search)
const form_tab = search_params.get("form_tab")
if (form_tab === 'cadastrar') {
    showCreateForm()
}