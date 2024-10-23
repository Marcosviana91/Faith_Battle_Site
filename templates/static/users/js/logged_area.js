
// Get avatar list from API
var avatar_list = []
function getAvatarList() {
    if (avatar_list.length == 0) {
        $('#avatar_list_container')[0].innerHTML = "";
        fetch('/api/avatar_list')
            .then(result => result.json())
            .then(data => {
                avatar_list = data.avatar_list
                for (var avatar of avatar_list) {
                    // console.log(String(avatar).split('.')[0]);
                    const avatar_div = document.createElement("div");
                    avatar_div.id = "avatar_container";
                    avatar_div.classList.add('col-6', 'col-sm-4', 'col-lg-3', 'p-1');
                    avatar_div.dataset["avatar"] = avatar;
                    avatar_div.onclick = () => { setAvatar(avatar_div) }

                    avatar_div.innerHTML = `
                                        <div data-bs-target="#editPlayerDataModal"
                    data-bs-toggle="modal"
                                            class="pointer d-flex flex-row justify-content-between align-items-center bg-dark border border-1 border-black rounded-1 p-1">
                                            <span class="text-light">${avatar.split('.')[0]}</span>
                                            <img class="avatar_image_micro" src="/static/general/img/Avatar/${avatar}">
                                        </div>
                                        `
                    $('#avatar_list_container').first().append(avatar_div)
                }
            })
            .catch(error => {
                $('#avatar_list_container').first().append('<h3 color="#fff">Não foi possível carregar os avatares</h3>')
            })
    }
}

const AVATAR_URL = '/static/general/img/Avatar/'
function setAvatar(element) {
    console.log("Elemento escolhido", element.dataset.avatar)
    $('#avatar_hidden')[0].value = element.dataset.avatar
    $('#avatar_hidden + img')[0].src = AVATAR_URL + element.dataset.avatar
}
