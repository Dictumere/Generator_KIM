document.getElementById("check-answer").addEventListener("click", function() {
    document.getElementById("explanation").classList.remove("hidden");
    document.getElementById("explanation").textContent = "Здесь будет пояснение к вашему ответу.";
});

document.getElementById("new-task").addEventListener("click", function() {
    fetch("/get_task")
        .then(response => response.json())
        .then(data => {
            document.getElementById("task-text").textContent = data.task;
            document.getElementById("explanation").classList.add("hidden");
        })
        .catch(error => console.error("Ошибка:", error));
});

