document.addEventListener("DOMContentLoaded", function () {
    // Загружаем первое задание при старте страницы
    loadNewTask();

    // Обработчик клика на кнопку "новое задание"
    document.getElementById("new-task").addEventListener("click", loadNewTask);

    // Обработчик клика на кнопку "проверить ответ"
    document.getElementById("check-answer").addEventListener("click", checkAnswer);

    // Добавляем обработчик изменения сложности
    document.getElementById("difficulty").addEventListener("change", loadNewTask);
});

// Функция для загрузки нового задания
function loadNewTask() {
    let difficulty = document.getElementById("difficulty").value; // Получаем текущую сложность

    fetch(`/get_task?difficulty=${difficulty}`) // Передаем сложность в запросе
        .then(response => response.json())
        .then(data => {
            document.getElementById("task-text").textContent = data.task;
            document.querySelector("input[name='text']").value = "";
            document.getElementById("explanation").classList.add("hidden");
        })
        .catch(error => {
            console.error("Ошибка загрузки задания:", error);
        });
}

// Функция для проверки ответа
function checkAnswer() {
    let userAnswer = document.querySelector("input[name='text']").value.trim();

    // Отправляем ответ на сервер
    fetch("/check_answer", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ answer: userAnswer })  // Отправляем ответ пользователя
    })
    .then(response => response.json())
    .then(data => {
        let explanation = document.getElementById("explanation");
        explanation.classList.remove("hidden");

        // Обработка ответа от сервера
        if (data.status === "error") {
            explanation.textContent = data.message;
            return;
        }

        // Если ответ правильный
        if (data.is_correct) {
            explanation.textContent = "✅ Ответ верный!";
        } else {
            explanation.textContent = `❌ Неправильно. Правильный ответ: ${data.right_answer}`;
        }
    })
    .catch(error => {
        console.error("Ошибка при проверке ответа:", error);
    });
}
