const reviewPopup = document.querySelector('#reviewPopup')

function getCookie(name) {
  let matches = document.cookie.match(
    new RegExp(
      "(?:^|; )" +
        name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, "\\$1") +
        "=([^;]*)"
    )
  );
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function closeTeamFilialModal(){
    reviewPopup.classList.remove('review_open')
    reviewPopup.removeEventListener('click', null)
}

async function openTeamFilialModal(reviewId) {
  // JavaScript отправляет Ajax-запрос к ресурсу Django
  let dataJson = {}
  await fetch(`/review`, {
    method: "POST", // 'GET' тоже подойдёт, но 'POST' позволит использовать куки
    headers: { 
        "X-CSRFToken": getCookie("csrftoken"), // CSRF-токен для Django, это важно помимо использования куки
        'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({ reviewId: reviewId }), // Данные, которые отправляются в Django
  })
    .then((response) => response.json()) // Преобразуем полученный ответ в JSON
    .then((data) => dataJson = JSON.parse(data)[0]['fields']) // Обрабатываем данные, полученные в ответе
    .catch((error) => console.error("Ошибка:", error)); // Если возникли ошибки, выводим их в консоль

    // TODO: сделать обработку фотография или видео
    reviewPopup.getElementsByClassName('review__content-file')[0].src = '/media/' + dataJson.fileUrl   
    reviewPopup.getElementsByClassName('review__content')[0].href = '/media/' + dataJson.fileUrl
    reviewPopup.getElementsByClassName('review__name')[0].textContent = dataJson.name
    reviewPopup.getElementsByClassName('review__parent')[0].textContent = dataJson.parent + ', ' + dataJson.childAge
    reviewPopup.getElementsByClassName('review__text')[0].textContent = dataJson.review

    const cnt = reviewPopup.getElementsByClassName('review__content')[0]
    cnt.classList.add(`glighbox${reviewId}`)

    let lightbox2 = GLightbox({
        selector: `.glighbox${reviewId}`
    });

    reviewPopup.classList.add('review_open')
    // reviewPopup.querySelector('#detailed__close').addEventListener('click', () => {
    //     closeTeamFilialModal()
    // })
    reviewPopup.addEventListener( 'click', (e) => {
        const isClickInside = !!event.target.closest('.review__wrapper');
        if (!isClickInside) {
            closeTeamFilialModal()
        }
    })
}

document.querySelectorAll(".reviews__content").forEach((item) => {
    item.addEventListener("click", () => {
      openTeamFilialModal(item.getAttribute("data-reviewId"));
    });
  });