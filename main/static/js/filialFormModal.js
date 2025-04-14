const excursionForm = document.querySelector("#excursionForm");

function openTeamFilialModal(slug) {
  excursionForm.classList.add("excursion-form_open");
    excursionForm.addEventListener("click", (e) => {
    const isClickInside = !!event.target.closest(".excursion-form__wrapper");
    if (!isClickInside) {
      closeTeamFilialModal();
    }
  });
  document.forms.excursionForm.action = `/filial/${slug}`
}

function closeTeamFilialModal(){
    excursionForm.classList.remove('excursion-form_open')
    excursionForm.action = `/filial/`
    // excursionForm.querySelector('#excursion-form__close').removeEventListener('click')
    excursionForm.removeEventListener('click', null)
}

// document.querySelectorAll('.filials__contacts').forEach(item => {
//     item.addEventListener('click', () => {
//         openTeamFilialModal(slug)
//     })
// })