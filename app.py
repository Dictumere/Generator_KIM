from flask import Flask, render_template, jsonify, request
from main import execute_random_method  # Убедись, что эта функция существует

app = Flask(__name__)

current_task = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_task", methods=["GET"])
def get_task():
    global current_task
    current_task = execute_random_method()  # Возвращает случайное задание
    print(f"Задание: {current_task}")  # Логируем
    return jsonify({"task": current_task["task"]})


@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    user_answer = data.get("answer", "").strip()

    if not user_answer:
        return jsonify({"status": "error", "message": "Ответ не должен быть пустым!"})

    is_correct = str(user_answer) == str(current_task["answer"])

    return jsonify({
        "status": "ok",
        "is_correct": is_correct,
        "right_answer": current_task["answer"] if not is_correct else None
    })


if __name__ == "__main__":
    app.run(debug=True)
