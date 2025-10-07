# Django Ecommerce

A complete **E-commerce web application** built with Django.  
It includes product management, shopping cart, user authentication, and order processing, along with a responsive frontend.

---

## 🚀 Features

- **User Authentication**: Register, login, logout, and profile management  
- **Product Management**: Browse products, categories, and search functionality  
- **Shopping Cart**: Add, update, and remove products from the cart  
- **Order Management**: Place and track orders  
- **Admin Panel**: Manage products, users, categories, and orders  
- **Reusable Components**: Common base models and email utilities  
- **Responsive Frontend** with Bootstrap and custom CSS  

---

## 🛠️ Tech Stack

- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL  
- **Authentication**: Django’s built-in user system  
- **Static Assets**: Bootstrap, FontAwesome  

---

## 📂 Project Structure

```
Django-Ecommerce/
│── manage.py
│── Ecommerce/ # Main project configuration (settings, urls, wsgi, asgi)
│── Home/ # Home app (landing, index views)
│── Products/ # Product models, views, categories
│── Cart/ # Shopping cart functionality
│── accounts/ # User authentication and profile management
│── base/ # Base models, utilities (emails, helpers)
│── public/ # Static assets (CSS, JS, Images)
│── templates/ # HTML templates (extendable for each app)
│── requirements.txt # Python dependencies (if available)
│── LICENSE
```

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/RUGVEDADHIKARI/Django-Ecommerce.git
cd Django-Ecommerce
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```
## 🔑 Default Apps

- **Home** → Landing pages, main navigation
- **Products** → Product listing, details, categories
- **Cart** → Add/remove/update items in shopping cart
- **accounts** → User authentication & profile
- **base** → Core reusable modules (emails, models, utilities)

## 🤝 Contributing

Contributions are welcome! Please open issues or pull requests for improvements, bug fixes, or suggestions.

1. Fork the repo
2. Create your feature branch (git checkout -b feature/YourFeature)
3. Commit changes (git commit -m 'Add some feature')
4. Push to branch (git push origin feature/YourFeature)
5. Open a Pull Request

## 📄 License

[MIT License](LICENSE)

---

## 🙋‍♂️ Contact

- **GitHub:** [RUGVEDADHIKARI](https://github.com/RUGVEDADHIKARI)
- **LinkedIn:** [www.linkedin.com/in/rugved-adhikari]

---
