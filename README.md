# Django-FlowerShop
```
pre-commit run --all-files
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

4. **Run Migrations:** 
```bash
python manage.py migrate
```

5. **Create .env file with environment variables:** 
```
SECRET_KEY=changeme
DEBUG=False
# DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>
# ALLOWED_HOSTS=127.0.0.1, localhost
```

6. **Start the Development Server:** 
```bash
python manage.py runserver
```

7. **Access the Application:** 

Open your browser and navigate to http://127.0.0.1:8000/