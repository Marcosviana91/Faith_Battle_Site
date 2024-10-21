// Thanks https://stackoverflow.com/questions/5802580/html-input-type-file-get-the-image-before-submitting-the-form
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            image = e.target.result;
        };
        reader.onloadend = function () {
            preview_content.innerHTML = renderContent()
        }
        reader.readAsDataURL(input.files[0])
    }
}

const novo_conteudo = $('#novo_conteudo')[0]
const preview_content = $('#preview_content')[0]
const img_preview = $('#img_preview')[0]
const novo_conteudo_titulo = $('#novo_conteudo_titulo')[0]

var title = ''
var image = ''
var content = ''

function renderContent() {
    return `
    <h1 class="text-center">${title}</h1>
    <img id="img_preview" class="w-100 mb-2" style="max-height: 300px;" src="${image}">
    ` + content
}


$('#novo_conteudo_titulo').on('input', function (e) {
    title = e.target.value
    preview_content.innerHTML = renderContent()
});

$('#id_img_capa').on('change', function () {
    readURL(this)
});

$('#novo_conteudo').on('input', function (e) {
    content = e.target.value
    preview_content.innerHTML = renderContent()
});

