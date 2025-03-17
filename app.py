from flask import Flask, render_template, jsonify
from main import task_find_address_net

app = Flask(__name__)

@app.route('/main')
def main_page():
    return render_template('index.html')


@app.route('/get_task', methods=['GET'])
def get_task():
    return jsonify(task_find_address_net())


if __name__ == '__main__':
    print("Flask сервер стартует...")  # Проверяем, выполняется ли код
    app.run(debug=True)
