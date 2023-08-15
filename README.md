# Django-FlowerShop

# ДЛЯ РАЗРАБОТЧИКОВ!

Форматирование с учетом flake8. Создать папку .vscode и в ней файл settings.json:
```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=100"],
    "editor.formatOnSave": true,
}
```
Для PyCharm можно использовать .editorconfig для тех же целей и результатов.

Разработку новых фич ведем:

1. Делаем ветку feature/super-feature от ветки develop
2. Готовую фичу мерджим в develop

Перед каждым коммитом форматируем текст по black и нашей настройке flake8 и запускаем команду:
```
pre-commit run --all-files
```

Settings.py настроен на то, что контейнер с базой будет запущен командой ниже. Можно без докера, тогда запускайте базу сообразно нашей настройке DATABASES в Settings.py.

Run PostgreSQL in Docker:
```bash
docker run --name flowershop_db -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -v pgdata:/var/lib/postgresql/data -d postgres
```



## Getting Started

Follow these steps to get the project up and running on your local machine:

1. **Clone the Repository:**
```bash
git clone https://github.com/DmitryDubovikov/Django-FlowerShop.git
cd Django-FlowerShop
```

2. **Create a Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create .env file with environment variables:**
```
SECRET_KEY=changeme
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
# DB_URL=postgresql://<username>:<password>@<host>:<port>/<database>
DB_URL=postgresql://postgres:mysecretpassword@localhost:5432/postgres
```

5. **Run Migrations:**
```bash
python manage.py migrate
```

6. **Start the Development Server:**
```bash
python manage.py runserver
```

7. **Access the Application:**

Open your browser and navigate to http://127.0.0.1:8000/
