from flask import Flask


from ies_app.model import db, Data_controller


def create_app():
    app = Flask(__name__)                   # создание Flask приложения 
    app.config.from_pyfile('config.py')     # получение конфиг данных из config.py
    db.init_app(app)                        # инициализация БД

    @app.route('/')
    def index():
        title='BAC0 данные'

    return app
    

