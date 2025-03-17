from flask import Flask, render_template

app = Flask(__name__)

@app.route('/main')
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    print("Flask сервер стартует...")  # Проверяем, выполняется ли код
    app.run(debug=True)
