const mainSection = document.getElementById("main-section")
const sidebar = document.getElementById("sidebar")

function sidebarToggler() {
    mainSection.classList.toggle("active-sidebar")
    sidebar.classList.toggle("active-sidebar")
}




let questions=data;

const questionContainer = document.getElementById("question-container");
const questionElement = document.getElementById("question");
const questionNumberElement = document.getElementById("question-number");
const optionsElement = document.getElementById("options");
const answerForm = document.getElementById("answer-form");
const backBtn = document.getElementById("back-btn");
const nextBtn = document.getElementById("next-btn");
const resultsContainer = document.getElementById("results-container");
const scoreElement = document.getElementById("score");
const reviewElement = document.getElementById("review");

let currentQuestionIndex = 0;
let currentQuestion = null;
let selectedAnswers = [];

function showQuestion(question) {
  questionNumberElement.innerText=question.numb;
  questionElement.innerText = question.question;
  optionsElement.innerHTML = "";
  for (let option of question.options) {
    const optionLabel = document.createElement("label");
    const optionInput = document.createElement("input");
    optionInput.type = "radio";
    optionInput.name = "answer";
    optionInput.value = option;
    optionLabel.appendChild(optionInput);
    optionLabel.append(` ${option}`);

     // add event listener to option input
    optionInput.addEventListener("change", () => {
      if (!optionInput.checked) {
        optionLabel.classList.add("not-selected");
      } else {
        optionLabel.classList.remove("not-selected");
      }
    });
    optionsElement.appendChild(optionLabel);
  }
  const selectedOption = selectedAnswers[currentQuestionIndex];
  if (selectedOption) {
    const optionInput = optionsElement.querySelector(`input[value="${selectedOption}"]`);
    optionInput.checked = true;
  }
}

function showNextQuestion(event) {
  event.preventDefault();
  const selectedOption = document.querySelector('input[name="answer"]:checked');
  selectedAnswers[currentQuestionIndex] = selectedOption ? selectedOption.value : '';
  if (selectedOption && selectedOption.value === currentQuestion.answer) {
    selectedOption.parentElement.classList.add("correct");
  } else if (selectedOption) {
    selectedOption.parentElement.classList.add("incorrect");
  }
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    currentQuestion = questions[currentQuestionIndex];
    showQuestion(currentQuestion);
  } else {
    showResults();
  }
}


function showPreviousQuestion() {
  if (currentQuestionIndex > 0) {
    currentQuestionIndex--;
    currentQuestion = questions[currentQuestionIndex];
    showQuestion(currentQuestion);
  }
}

function showResults() {
  questionContainer.style.display = "none";
  resultsContainer.style.display = "block";
  const correctAnswers = questions.filter((q, i) => selectedAnswers[i] === q.answer).length;
  scoreElement.innerHTML = `You got ${correctAnswers} out of ${questions.length} questions correct.`;
  reviewElement.innerHTML = "";
  for (let i = 0; i < questions.length; i++) {
    const question = questions[i];
    const reviewItem = document.createElement("div");
    reviewItem.innerHTML = `<strong>Question ${i + 1}: ${question.question}</strong>`;
    const selectedOption = selectedAnswers[i];
    const optionLabel = document.createElement("label");
    if (selectedOption === question.answer) {
      optionLabel.classList.add("correct");
    }
if (!selectedOption) {
  optionLabel.classList.add("incorrect");
  optionLabel.append(`You did not answer this question.`);
} else if (selectedOption === question.answer) {
  optionLabel.classList.add("correct");
  optionLabel.append(`Your answer: ${selectedOption}`);
} else {
  optionLabel.classList.add("incorrect");
  optionLabel.append(`Your answer: ${selectedOption}. Correct answer: ${question.answer}`);
}
reviewItem.appendChild(optionLabel);
reviewElement.appendChild(reviewItem);
}
}

currentQuestion = questions[currentQuestionIndex];
showQuestion(currentQuestion);

answerForm.addEventListener("submit", showNextQuestion);
backBtn.addEventListener("click", showPreviousQuestion);


const submitBtn = document.getElementById("submit-btn");
submitBtn.addEventListener("click", function() {
  clearInterval(timerId);
  showResults();
});


const TEST_DURATION = 8; // in seconds
let timerId;

function startTimer() {
  const timerElement = document.getElementById("timer");
  let remainingTime = TEST_DURATION;

  function updateTimer() {
    const minutes = Math.floor(remainingTime / 60);
    const seconds = remainingTime % 60;
    timerElement.innerHTML = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    remainingTime--;
    if (remainingTime < 0) {
      clearInterval(timerId);
      //submitTest();
      submitBtn.click()
    }
  }

  updateTimer();
  timerId = setInterval(updateTimer, 1000);
}

startTimer();


const questionCount = questions.length;

function generateQuestionButtons(numQuestions) {
  const questionButtonsContainer = document.querySelector(".question-buttons");
  questionButtonsContainer.innerHTML = "";
  for (let i = 1; i <= numQuestions; i++) {
    const button = document.createElement("button");
    button.innerText = i;
    button.classList.add("not-visited");
    questionButtonsContainer.appendChild(button);
  }
}

generateQuestionButtons(questionCount)

function visitQuestion(questionIndex) {
  const questionButtonsContainer = document.querySelector(".question-buttons");
  const questionButton = questionButtonsContainer.children[questionIndex];
  questionButton.classList.remove("not-visited");
}
