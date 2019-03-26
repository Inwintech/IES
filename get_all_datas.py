from webapp import create_app
from webapp.bac0_serv import get_datas

app = create_app()
with app.app_context():
    get_datas()