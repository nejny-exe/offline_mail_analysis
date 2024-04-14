from flask import Flask, render_template, request, redirect, url_for, session
import logging

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Секретный ключ для подписи сессии

# Настройка логгера
logging.basicConfig(filename='app.log', level=logging.INFO)

# Предположим, что у вас есть некоторая база данных пользователей
# Здесь мы создаем простой словарь пользователей для демонстрации
users = {
    'user1': 'password1',
    'user2': 'password2'
}


vulnerabilities_data = [
    {'id': 1, 'name': 'Уязвимость 1', 'severity': 'Высокая', 'direct':'c:/programmfiles/'},
    {'id': 2, 'name': 'Уязвимость 2', 'severity': 'Средняя'},
    {'id': 3, 'name': 'Уязвимость 3', 'severity': 'Низкая'}
]


@app.route('/')
def index():
    if 'username' in session:
        return render_template('menu.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            logging.info(f'Пользователь {username} вошел в систему')
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error_message='Неверное имя пользователя или пароль')
    return render_template('login.html')

@app.route('/logout')
def logout():
    if 'username' in session:
        logging.info(f'Пользователь {session["username"]} вышел из системы')
        session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/vulnerabilities')
def vulnerabilities():
    # Обработка нажатия кнопки "Уязвимости"
    logging.info('Кнопка "Уязвимости" нажата')
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('vulnerabilities.html', vulnerabilities=vulnerabilities_data)


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
