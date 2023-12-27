from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_data = request.form['user_input']
        print(f"Вы ввели значение: {user_data}")
        return f"Вы ввели значение: {user_data}"
    else:
        return "Ошибка сервера"


if __name__ == '__main__':
    app.run(debug=True)