const button = document.querySelector('#sendReview')
const buttonClose = document.querySelector('#sendReviewClose')
const sendReviewPopup = document.querySelector('#sendReviewPopup')

button.addEventListener('click', () => {
    sendReviewPopup.classList.add('popup_open')
});

buttonClose.addEventListener('click', () => {
    sendReviewPopup.classList.remove('popup_open')
});