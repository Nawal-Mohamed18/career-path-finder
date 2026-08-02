const views = {
  home: document.getElementById("view-home"),
  path: document.getElementById("view-path"),
  quiz: document.getElementById("view-quiz"),
};

const careerSelect = document.getElementById("career-select");
const otherField = document.getElementById("other-field");
const otherInput = document.getElementById("other-input");
const pathDetail = document.getElementById("path-detail");
const quizPanel = document.getElementById("quiz-panel");

let careers = {};
let questions = [];
let quizCareers = [];
let quizStep = 0;
let quizAnswers = [];
let selectedOption = null;

function showView(name) {
  Object.entries(views).forEach(([key, el]) => {
    const active = key === name;
    el.hidden = !active;
    el.classList.toggle("active", active);
  });
  if (name === "quiz") {
    quizStep = 0;
    quizAnswers = [];
    selectedOption = null;
    renderQuiz();
  }
  if (name === "path") {
    syncOtherField();
    renderPathDetail();
  }
}

function syncOtherField() {
  const isOther = careerSelect.value === "other";
  otherField.hidden = !isOther;
  if (!isOther) otherInput.value = "";
}

function renderCareerDetail(career, { intro, titleOverride } = {}) {
  const title = titleOverride || career.title;
  const steps = career.path
    .map(
      (step, i) =>
        `<div class="step" style="animation-delay:${i * 40}ms"><strong>Step ${i + 1}.</strong> ${step}</div>`
    )
    .join("");

  return `
    ${intro ? `<div class="banner">${intro}</div>` : ""}
    <h2>${title}</h2>
    <p class="tagline">${career.tagline}</p>
    <p class="skills"><strong>Core skills</strong><br>${career.skills.join(" · ")}</p>
    <p><strong>Your path</strong></p>
    ${steps}
  `;
}

function renderPathDetail() {
  const key = careerSelect.value;
  const career = careers[key];
  if (!career) {
    pathDetail.innerHTML = "";
    return;
  }

  let titleOverride;
  if (key === "other") {
    const custom = otherInput.value.trim();
    titleOverride = custom ? `Other: ${custom}` : "Other";
  }

  pathDetail.innerHTML = renderCareerDetail(career, { titleOverride });
}

function scoreAnswers(answers) {
  const totals = Object.fromEntries(quizCareers.map((key) => [key, 0]));
  questions.forEach((q, i) => {
    const idx = answers[i];
    if (idx == null || idx < 0 || idx >= q.options.length) return;
    const scores = q.options[idx].scores || {};
    Object.entries(scores).forEach(([career, points]) => {
      if (career in totals) totals[career] += points;
    });
  });
  return Object.entries(totals).sort((a, b) => b[1] - a[1]);
}

function renderQuiz() {
  if (quizStep >= questions.length) {
    submitQuiz();
    return;
  }

  const q = questions[quizStep];
  const pct = (quizStep / questions.length) * 100;
  const options = q.options
    .map(
      (opt, idx) =>
        `<button type="button" class="option${selectedOption === idx ? " selected" : ""}" data-idx="${idx}">${opt.label}</button>`
    )
    .join("");

  quizPanel.innerHTML = `
    <div class="progress" aria-hidden="true"><span style="width:${pct}%"></span></div>
    <p class="q-meta">Question ${quizStep + 1} of ${questions.length}</p>
    <p class="q-text">${q.text}</p>
    <div class="options">${options}</div>
    <div class="actions">
      <button type="button" class="btn" id="quiz-back" ${quizStep === 0 ? "disabled" : ""}>Back</button>
      <button type="button" class="btn primary" id="quiz-next" ${selectedOption === null ? "disabled" : ""}>Next</button>
    </div>
  `;

  quizPanel.querySelectorAll(".option").forEach((btn) => {
    btn.addEventListener("click", () => {
      selectedOption = Number(btn.dataset.idx);
      renderQuiz();
    });
  });

  document.getElementById("quiz-back").addEventListener("click", () => {
    if (quizStep === 0) return;
    quizStep -= 1;
    quizAnswers = quizAnswers.slice(0, quizStep);
    selectedOption = quizAnswers[quizStep] ?? null;
    renderQuiz();
  });

  document.getElementById("quiz-next").addEventListener("click", () => {
    if (selectedOption === null) return;
    quizAnswers[quizStep] = selectedOption;
    quizStep += 1;
    selectedOption = null;
    renderQuiz();
  });
}

function submitQuiz() {
  const ranked = scoreAnswers(quizAnswers);
  const [bestKey, bestScore] = ranked[0];
  const [secondKey, secondScore] = ranked[1];
  const best = { ...careers[bestKey], key: bestKey, score: bestScore };
  const second = { title: careers[secondKey].title, score: secondScore };

  quizPanel.innerHTML =
    renderCareerDetail(best, {
      intro: `Best match: <strong>${best.title}</strong> (score ${best.score}).`,
    }) +
    `<p class="note"><strong>Also close:</strong> ${second.title} (score ${second.score}). You can open Path to a career to compare roadmaps.</p>
     <div class="actions" style="margin-top:1rem">
       <button type="button" class="btn primary" id="retake">Retake questions</button>
     </div>`;

  document.getElementById("retake").addEventListener("click", () => {
    quizStep = 0;
    quizAnswers = [];
    selectedOption = null;
    renderQuiz();
  });
}

document.querySelectorAll("[data-go]").forEach((el) => {
  el.addEventListener("click", () => showView(el.dataset.go));
});

careerSelect.addEventListener("change", () => {
  syncOtherField();
  renderPathDetail();
});

otherInput.addEventListener("input", renderPathDetail);

function init() {
  const data = window.CAREER_DATA;
  if (!data) {
    quizPanel.innerHTML = `<p class="note">Missing career data. Refresh the page.</p>`;
    return;
  }
  careers = data.careers;
  questions = data.questions;
  quizCareers = data.quizCareers;

  careerSelect.innerHTML = Object.entries(careers)
    .map(([key, c]) => `<option value="${key}">${c.title}</option>`)
    .join("");
}

init();
