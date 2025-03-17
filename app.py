from flask import Flask, render_template, request, jsonify
from generators import generate_ip, generate_mask
from solution import find_address_net

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_task', methods=['GET'])
def generate_task():
    ip = generate_ip()
    mask = generate_mask(23)
    return jsonify({"ip": ip, "mask": mask})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get("answer")
    ip = data.get("ip")
    mask = data.get("mask")
 
    correct_answer = find_address_net(ip, mask)
    is_correct = user_answer == correct_answer

    return jsonify({"correct": is_correct, "right_answer": correct_answer})

if __name__ == '__main__':
    app.run(debug=True)
