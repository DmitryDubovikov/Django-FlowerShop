# Django-FlowerShop

http://77.105.168.57/


Welcome to the Django Flower Shop project! This web application is built using the Django framework and is designed to provide an elegant online platform for buying and exploring a wide range of beautiful bouquets.

<img src="flowershop.png" alt="Image Alt Text" width="600">

Features
* **Browse Bouquets**: Easily browse through a diverse collection of bouquets, each accompanied by stunning images and detailed descriptions.

* **Search and Filter**: Use the search and filtering options to quickly find the flowers you're looking for based on various criteria such as type, color, and occasion.

* **Orders**: Order your favorite bouquet, and proceed to checkout when you're ready.

* **Telegram notifications for couriers**: enhanced communicationt between a courier team and shop managers.

* **Secure Payments**: Enjoy the peace of mind with secure payment options, ensuring a safe and seamless transaction process.

* **Admin Dashboard**: Admins can manage bouquets listings, orders, and ... through an intuitive admin dashboard.

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
DB_URL=postgresql://<username>:<password>@<host>:<port>/<database>
U_KASSA_TOKEN: // токен платежной системы Ю-КАССА
ACCOUT_ID: идентификатор учетной записи Ю-КАССА
TG_TOKEN: токен чат бота телеграмм
chat_id: идентификатор чата для курьеров
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
