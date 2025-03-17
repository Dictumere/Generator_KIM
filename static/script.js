document.getElementById("check-answer").addEventListener("click", function() {
    document.getElementById("explanation").classList.remove("hidden");
    document.getElementById("explanation").textContent = "Здесь будет пояснение к вашему ответу.";
});

document.getElementById("new-task").addEventListener("click", function() {
    document.getElementById("task-text").textContent = "Новое случайное задание...";
    document.getElementById("answer").value = "";
    document.getElementById("explanation").classList.add("hidden");
});
