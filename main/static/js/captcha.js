const sendBookForm = document.getElementById("sendbookForm");

let inviseCaptcha;

function onloadFunction() {
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.render("captcha-container", {
    sitekey: "ysc1_bLt1HCJIeeQIuEEPSlh8jii8T7oWcqx2Fgwyylbl5cc0517f",
  });

  inviseCaptcha = window.smartCaptcha.render("captcha-container2", {
    sitekey: "ysc1_8F4Jz9Qk4yDpa9hURE9l6W2Pm14pEgGKm9ONDEYic04cb95b",
    invisible: true, // Сделать капчу невидимой
    callback: callback,
    hideShield: true,
  });

}

function callback(token) {
  sendBookForm.submit();
}

function handleSubmit(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha);
}
