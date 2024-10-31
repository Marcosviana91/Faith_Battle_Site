// Transform o conteúdo de um elemento .toInnerHtml
const toInnerHtml = $('.toInnerHtml')
for (element of toInnerHtml) {
    element.innerHTML = element.innerText
}