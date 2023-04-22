### Инструкция по настройке проекта

1) Открыть папку, в которую будете клонировать репозиторий
2) Открыть эту папкку в консоли и прописать команду \
   
git clone https://github.com/nishebrodsky/controlwork_9_alima_utkelbayeva.git
3) Открыть появившуюся папку -controlwork_9_gleb_alima_utkelbayeva и создать виртуальное окружение
с помощью команды 
virtualenv -p python venv
4) . 
. venv/bin/activate
4) 
pip install -r requirements.txt
5) перемещаемся в source 
cd source 
6) настраиваем в файле source/app/settings.py в
5) перемещаемся в source 
cd source 
6) настраиваем в файле source/app/settings.py на свою базу данных
7) прописываем в консоли ./manage.py migrate
8) прописываем ./manage.py loaddata fixtures/auth.json
9) прописываем ./manage.py loaddata fixtures/webapp.json
10) прописываем ./manage.py runserver
11) Пароли для всех юзеров root root
root2 root2
admin 12345