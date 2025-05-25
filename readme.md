# 🧠 Flask + Celery + Redis

A simple application using **Flask** for the web API, **Celery** for asynchronous background tasks, and **Redis** as the message broker/backend result.

---

## 📦 Stack

- [Flask](https://flask.palletsprojects.com/)
- [Celery](https://docs.celeryq.dev/)
- [Redis](https://redis.io/)

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/amine-tahri/flask-celery-redis.git
cd flask-celery-redis
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Make sure Redis is running
Install Redis if needed and start the server:


```bash
redis-server

```

# 🚀 Running the App
### 1. Start the Flask server
```bash
flask run
```
### 2. Start the Celery worker
```bash
celery -A tasks worker --loglevel=info
```

# 📁 Project Structure

```bash
flask-celery-redis/
├── app.py             # Flask application
├── tasks.py           # Celery tasks
├── requirements.txt   # Python dependencies
└── README.md

```