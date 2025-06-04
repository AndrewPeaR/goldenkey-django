const detailedPopup = document.querySelector('#detailedPopup')

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
    detailedPopup.classList.remove('detailed_open')
    detailedPopup.querySelector('#detailed__close').removeEventListener('click', null)
    detailedPopup.removeEventListener('click', null)
}

async function openTeamFilialModal(teamId) {
  // JavaScript отправляет Ajax-запрос к ресурсу Django
  let dataJson = {}
  await fetch(`/filial/team`, {
    method: "POST", // 'GET' тоже подойдёт, но 'POST' позволит использовать куки
    headers: { 
        "X-CSRFToken": getCookie("csrftoken"), // CSRF-токен для Django, это важно помимо использования куки
        'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify({ teamId: teamId }), // Данные, которые отправляются в Django
  })
    .then((response) => response.json()) // Преобразуем полученный ответ в JSON
    .then((data) => dataJson = JSON.parse(data)[0]['fields']) // Обрабатываем данные, полученные в ответе
    .catch((error) => console.error("Ошибка:", error)); // Если возникли ошибки, выводим их в консоль

    detailedPopup.getElementsByClassName('detailed__image-file')[0].src = '/media/' + dataJson.image   
    detailedPopup.getElementsByClassName('detailed__lastname')[0].textContent = dataJson.lastname
    detailedPopup.getElementsByClassName('detailed__firstname')[0].textContent = dataJson.firstname
    detailedPopup.getElementsByClassName('detailed__status')[0].textContent = dataJson.status + ', ' + dataJson.expirience
    detailedPopup.getElementsByClassName('detailed__quote')[0].textContent = "«"+ dataJson.quote + "»"
    detailedPopup.getElementsByClassName('detailed__description')[0].textContent = dataJson.description
    detailedPopup.getElementsByClassName('detailed__сall-to-action')[0].textContent = dataJson.callToAction

    detailedPopup.classList.add('detailed_open')
    detailedPopup.querySelector('#detailed__close').addEventListener('click', () => {
        closeTeamFilialModal()
    })
    detailedPopup.addEventListener( 'click', (e) => {
        const isClickInside = !!event.target.closest('.detailed__wrapper');
        if (!isClickInside) {
            closeTeamFilialModal()
        }
    })
}

document.querySelectorAll(".team__more-button").forEach((item) => {
    item.addEventListener("click", () => {
      openTeamFilialModal(item.getAttribute("data-id"));
    });
  });