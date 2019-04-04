from flask import Flask, render_template
from ies_app.model import db, Data_controller


def create_app():
    app = Flask(__name__)                   # создание Flask приложения 
    app.config.from_pyfile('config.py')     # получение конфиг данных из config.py
    db.init_app(app)                        # инициализация БД

    @app.route('/')
    def index():
        title='BAC0 данные'
        datas_list=Data_controller.query.all()                                      #чтение данных из БД
        return render_template('index.html',page_title=title,datas_list=datas_list)   #отображение данный в web через шаблон jinja

    return app
    

