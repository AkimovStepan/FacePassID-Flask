from flask import Flask, render_template, request, redirect, url_for
import System

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_algorithm', methods=['POST'])
def run_algorithm():
    System.detect_person()
    return 'Алгоритм запущен успешно!'

@app.route('/add_photos', methods=['GET', 'POST'])
def add_photos():
    if request.method == 'POST':
        # Обработка загрузки фотографий
        # Код для обработки загрузки фотографий
        return redirect(url_for('add_photos'))  # Перенаправляем на эту же страницу после загрузки фотографий
    return render_template('add_photos.html')

if __name__ == '__main__':
    app.run(debug=True)
