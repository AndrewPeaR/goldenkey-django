const sendBookForm = document.getElementById("sendbookForm");
const excursionFilialForm = document.getElementById("filialForm");

let inviseCaptcha;
let inviseCaptcha2;

function onloadFunction() {
  if (!window.smartCaptcha) {
    return;
  }
  if (window.location.pathname === "/") {
    window.smartCaptcha.render("captcha-container", {
      sitekey: "ysc1_bLt1HCJIeeQIuEEPSlh8jii8T7oWcqx2Fgwyylbl5cc0517f",
    });

    inviseCaptcha = window.smartCaptcha.render("captcha-container2", {
      sitekey: "ysc1_8F4Jz9Qk4yDpa9hURE9l6W2Pm14pEgGKm9ONDEYic04cb95b",
      invisible: true, // Сделать капчу невидимой
      callback: callback,
      hideShield: true,
    });
  } else if (window.location.pathname.split("/")[1] === "filial") {
    inviseCaptcha2 = window.smartCaptcha.render("captcha-container3", {
      sitekey: "ysc1_a2GwqWPD6T6xZL2mdb1XpU7Q8yOCiDq8oPtiXfLB9cac16db",
      invisible: true, // Сделать капчу невидимой
      callback: excursionFilialFormCallback,
      hideShield: true,
    });
  }
}

function callback(token) {
  sendBookForm.submit();
}
function excursionFilialFormCallback(token) {
  excursionFilialForm.submit();
}

function handleSubmit(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha);
}

function handleSubmit2(event) {
  event.preventDefault();
  if (!window.smartCaptcha) {
    return;
  }
  window.smartCaptcha.execute(inviseCaptcha2);
}
