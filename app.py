from flask import Flask, render_template, jsonify, request, session
from main import execute_random_method
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3


app = Flask(__name__)
app.secret_key = "QWERTY"
current_task = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Хешируем пароль
        hashed_password = generate_password_hash(password)

        # Сохраняем в базу данных
        try:
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (username, email, hashed_password)
                )
                conn.commit()
                flash("Регистрация прошла успешно. Теперь войди!", "success")
                return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Пользователь с такой почтой уже зарегистрирован.", "error")
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"]

        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, password FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            flash("Вы успешно вошли!", "success")
            return redirect(url_for("profile"))  # <--- Вот это делает переход
        else:
            flash("Неверная почта или пароль", "error")
            return redirect(url_for("login"))

    return render_template("login.html")



@app.route("/get_task", methods=["GET"])
def get_task():
    global current_task  
    difficulty = request.args.get("difficulty", "easy")  
    current_task = execute_random_method(difficulty)

    print(f"DEBUG: current_task = {current_task}")

    return jsonify({"task": current_task.get("task", "Ошибка: задание не найдено!")})



@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    user_answer = data.get("answer", "").strip()

    if not user_answer:
        return jsonify({"status": "error", "message": "Ответ не должен быть пустым!"})

    if "answer" not in current_task:
        return jsonify({"status": "error", "message": "Ошибка: нет правильного ответа!"})

    is_correct = str(user_answer) == str(current_task["answer"])

    # Сохраняем в БД
    if "user_id" in session:
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO history (user_id, task, user_answer, correct_answer)
                VALUES (?, ?, ?, ?)
            """, (
                session["user_id"],
                current_task.get("task", ""),
                user_answer,
                current_task.get("answer", "")
            ))
            conn.commit()

    return jsonify({
        "status": "ok",
        "is_correct": is_correct,
        "right_answer": current_task["answer"] if not is_correct else None
    })


@app.route("/profile")
def profile():
    if "user_id" not in session:
        flash("Сначала войди в аккаунт.", "error")
        return redirect(url_for("login"))

    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT task, user_answer, correct_answer FROM history
            WHERE user_id = ?
            ORDER BY id DESC
        """, (session["user_id"],))
        rows = cursor.fetchall()

    history = [{"task": row[0], "user_answer": row[1], "correct_answer": row[2]} for row in rows]

    return render_template("profile.html", history=history)


@app.route("/logout")
def logout():
    session.clear()
    flash("Вы вышли из аккаунта.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
