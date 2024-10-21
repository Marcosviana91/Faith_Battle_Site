// Filtro
var filtro = ''

$('input').on('input', function (e) {
    e.preventDefault();
    filtro = String(e.target.value).toLowerCase()
    const meus_artigos = Array(...$('.meus_artigos'))
    meus_artigos.forEach((artigo) => {
        if (artigo.children[0].innerText.toLowerCase().includes(filtro)) {
            // artigo.classList.remove("d-none");
            $(artigo).slideDown();
        } else {
            $(artigo).fadeOut();
            // artigo.classList.add("d-none");
        }
    })
});