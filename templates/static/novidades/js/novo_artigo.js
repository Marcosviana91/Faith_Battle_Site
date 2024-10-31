// Thanks https://stackoverflow.com/questions/5802580/html-input-type-file-get-the-image-before-submitting-the-form
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            image = e.target.result;
        };
        reader.onloadend = function () {
            // console.log(image)
        }
        reader.readAsDataURL(input.files[0])
    }
}

// Preview
const preview_titulo = $('#preview_titulo')[0]
const img_preview = $('#img_preview')[0]
const preview_conteudo = $('#preview_conteudo')[0]
const preview_tag = $('#preview_tag')[0]
const preview_data_publicacao = $('#preview_data_publicacao')[0]

var title = ''
var tag = ''
var image = ''
var content = ''

$('#titulo').on('input', function (e) {
    title = e.target.value
    if (title == '') {
        title = 'Insira um Título'
    }
    preview_titulo.innerHTML = title
});
$('#tag_version').on('input', function (e) {
    tag = e.target.value
    if (tag == '') {
        tag = 'nome-do-jogo_1.2.3'
    }
    preview_tag.innerHTML = tag
});

$('#img_capa').on('change', function (evt) {
    readURL(this)
});

$('#btn_salvar').on('click', function () {
    var summernoteStr = $('#summernote').summernote('code');
    if (summernoteStr) {
        for (var element of $('.preview_conteudo')) {
            element.innerHTML = summernoteStr
            element.innerHTML = summernoteStr
        }
    }
    if (image) {
        img_preview.src = image
    }
    preview_data_publicacao.innerText = new Date().toLocaleDateString()
})

$('#btn_preview').on('click', function () {
    var summernoteStr = $('#summernote').summernote('code');
    if (summernoteStr) {
        for (var element of $('.preview_conteudo')) {
            element.innerHTML = summernoteStr
            element.innerHTML = summernoteStr
        }
    }
})

