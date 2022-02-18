# task2

@База данных PostgreSql  
Создать каталог mkdir rockertdata_django  
Перейти в каталог cd rockertdata_django  
Клонировать каталог проекта с github  
git clone URL  
Устанавливаем виртуальное окружение  
python -m venv .venv  
Активировать виртуальное окружение  
source .venv/bin/activate  
Перейти в каталог проекта который склонировали  
cd parse_github  
Устанавливаем зависимости  
pip install -r requirements.txt  
Создать файл для подключения скрытых настроек из settings.py  
Добавляем в файл такие параметры и сохраняем:  

# Ваш хост 
ALLOWED_HOSTS=127.0.0.1  
# Дебаг режим True/ False  
DEBUG=True  
# Ваш секретный ключ  
SECRET_KEY=django-insecure-t9ao17z9oura90)q)9lm92m6(yra6+bz&x4^_9k85n$w-l5(8f  
# Ваш db engine  
DATABASES_ENGINE=django.db.backends.postgresql_psycopg2  
# Ваше название db  
DATABASES_NAME=postgres  
# User db  
DATABASES_USER=postgres  
# password db  
DATABASES_PASSWORD=  
# Хост db  
DATABASES_HOST=localhost  
# Порт db  
DATABASES_PORT=5432  

Делаем миграции  
./manage.py makemigrations  
./manage.py migrate  
Создаем супер-юзера  
./manage.py createsuperuser  

Выйти из этого каталога и зайти в каталог паука  
cd ..  
cd rocketdata/rocketdata  
Открываем settings.py и прописываем в настройках базы данных то, что прописали и django  
host, port, username, database  
Если есть пароль, то и его - password  
DATABASE = {  
    "drivername": 'postgresql',  
    "host": 'localhost',  
    "port": '5432',  
    "username": 'postgres',  
    # "password": '12345',  
    "database": 'postgres',  
}  
Сохраняем файл и переходим в каталог spiders  
cd spiders  
Запускаем проект  
scrapy crawl git_spider  
Он попросит ввести Логин профиля, допустим scrapy или MariyaSha  

В зависимости от того проект это или юзер, будут работать разные сценарии.  
У проект url выглядит так https://github.com/orgs/NAMEORG  
У юзеров url выглядит так https://github.com/MariyaSha  



Теперь возвращаемся в каталог Django parse_github  
Запускаем Django  
./manage.py runserver  

1)Апи получения ссылок на страницы пользователей (или проектов)  
http://127.0.0.1:8000/gitlink/  
2)Апи получения общей статистики  
http://127.0.0.1:8000/gitoveral/  
3)Сделать апи получения репозиториев пользователя (или проекта)  
Где в конце , вместо - 1 , это айди владельца по pk  
http://127.0.0.1:8000/gitgetrep/1/  
4)Апи получения статистики по одному пользователю (или проекту)  
Где в конце , вместо - 1 , это айди владельца по pk  
http://127.0.0.1:8000/gitindividualstats/1/  

Добавил еще просто список всех-всех репозиториев  
Так-же добавил пагинацию с лимитом в 20 штук  
http://127.0.0.1:8000/gitgetall/  


