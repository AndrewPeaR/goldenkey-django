const excursionForm = document.querySelector("#excursionForm");

function openFilialModal(slug) {
  excursionForm.classList.add("excursion-form_open");
    excursionForm.addEventListener("click", (e) => {
    const isClickInside = !!event.target.closest(".excursion-form__wrapper");
    if (!isClickInside) {
      closeFilialModal();
    }
  });
  document.forms.filialForm.action = `/filial/${slug}`
}

function closeFilialModal(){
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