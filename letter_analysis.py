from flask import Flask, render_template, request
import logging

app = Flask(__name__)

# Настройка логгера
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vulnerabilities')
def vulnerabilities():
    # Обработка нажатия кнопки "Уязвимости"
    logging.info('Кнопка "Уязвимости" нажата')
    # Ваш код обработки уязвимостей
    return "Уязвимости"

@app.route('/administration')
def administration():
    # Обработка нажатия кнопки "Администрирование"
    logging.warning('Кнопка "Администрирование" нажата')
    # Ваш код для администрирования
    return "Администрирование"

@app.route('/create_profile')
def create_profile():
    # Обработка нажатия кнопки "Создать профиль"
    logging.info('Кнопка "Создать профиль" нажата')
    # Ваш код для создания профиля
    return "Создать профиль"

@app.route('/check')
def check():
    # Обработка нажатия кнопки "Проверка"
    logging.info('Кнопка "Проверка" нажата')
    # Ваш код для проверки
    return "Проверка"

if __name__ == '__main__':
    app.run(debug=True)
