function openCard(element) {
    $(element.parentElement.querySelector('.card_body')).slideToggle()
    console.log($(element.parentElement.querySelector('.card_body'))[0])
}