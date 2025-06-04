const newsModal = document.querySelector('#newsModal')

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
    newsModal.classList.remove('news-modal_open')
    newsModal.removeEventListener('click', null)
}

async function openTeamFilialModal(newsId) {
  // JavaScript отправляет Ajax-запрос к ресурсу Django
  let dataJson = {}
  await fetch(`/news`, {
    method: "POST", // 'GET' тоже подойдёт, но 'POST' позволит использовать куки
    headers: { 
        "X-CSRFToken": getCookie("csrftoken"), // CSRF-токен для Django, это важно помимо использования куки
        'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({ newsId: newsId }), // Данные, которые отправляются в Django
  })
    .then((response) => response.json()) // Преобразуем полученный ответ в JSON
    .then((data) => dataJson = JSON.parse(data)[0]['fields']) // Обрабатываем данные, полученные в ответе
    .catch((error) => console.error("Ошибка:", error)); // Если возникли ошибки, выводим их в консоль

    // TODO: сделать обработку фотография или видео
    newsModal.getElementsByClassName('news-modal__image-file')[0].src = '/media/' + dataJson.image   
    newsModal.getElementsByClassName('news-modal__title')[0].textContent = dataJson.title
    newsModal.getElementsByClassName('news-modal__text')[0].textContent = dataJson.description

    newsModal.classList.add('news-modal_open')
    
    newsModal.addEventListener( 'click', (e) => {
        const isClickInside = !!event.target.closest('.news-modal__wrapper');
        if (!isClickInside) {
            closeTeamFilialModal()
        }
    })
}

document.querySelectorAll(".news__card").forEach((item) => {
    item.addEventListener("click", () => {
      openTeamFilialModal(item.getAttribute("data-newsId"));
    });
  });