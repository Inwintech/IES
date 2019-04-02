from ies_app import create_app
from ies_app.core.bac0_serv import get_datas  # из папки core импортируется функция 
                                              # get_datas отвечающий за пуск BAC0 чтение точек контроллера 

app = create_app()
with app.app_context():
    get_datas()