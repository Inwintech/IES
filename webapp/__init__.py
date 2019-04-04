from flask import Flask, render_template
from webapp.model import db, Datas


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title='BAC0 данные'
        datas_list=Datas.query.all()
        return render_template('index.html',page_title=title,datas_list=datas_list)


    return app