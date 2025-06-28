# Flask + Celery + Redis

A simple demo application that uses 🔥 **Flask** for the web API, **Celery** for asynchronous background tasks, and **Redis** as the message broker & result backend.

---

## 🚀 Stack

- [Flask](https://flask.palletsprojects.com/)
- [Celery](https://docs.celeryq.dev/)
- [Redis](https://redis.io/)

---

## 🧩 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/amine-tahri/flask-celery-redis.git
   cd flask-celery-redis

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
├── app.py           # Flask web application
├── tasks.py         # Celery task definitions
├── requirements.txt # Project dependencies
└── templates/
    └── async_example.html  # Sample UI template
```

# 🔧 How It Works

**Flask** renders a page (e.g., /async-task-template) to let users trigger a background process.

**Celery** sends the task you define to a worker, which runs it asynchronously.

**Redis** acts as both the broker (queues tasks) and the result backend (stores task outcomes).

# API Endpoints
POST /async-task-template

Dispatches a background job — returns a task_id.

GET /result/<task_id>

Polls the Celery backend to check task status: returns { state, result }.