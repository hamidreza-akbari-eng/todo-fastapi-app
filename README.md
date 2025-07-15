# Todo FastAPI Application

A modern, RESTful todo application built with FastAPI and SQLAlchemy, featuring user management and todo operations with a clean, scalable architecture.

## 🚀 Features

- **User Management**: Create, read, update, and delete users
- **Todo Operations**: Full CRUD operations for todos
- **Database Integration**: SQLAlchemy ORM with SQLite database
- **RESTful API**: Clean REST endpoints with proper HTTP methods
- **Data Validation**: Pydantic models for request/response validation
- **Auto Documentation**: Interactive API docs with Swagger UI

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM)
- **SQLite**: Lightweight database for data persistence
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

## 📁 Project Structure

```
todo-app/
├── database/
│   └── database.py          # Database models and configuration
├── models/
│   └── models.py            # Pydantic models for API
├── routers/
│   ├── todo_routers.py      # Todo-related endpoints
│   └── user_routers.py      # User-related endpoints
├── main.py                  # Application entry point
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

## 🚦 API Endpoints

### User Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/user/create_user` | Create a new user |
| GET | `/users` | Get all users |
| GET | `/user/{user_id}` | Get specific user by ID |
| PUT | `/user/{user_id}` | Update user information |
| DELETE | `/user/{user_id}` | Delete a user |

### Todo Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todo/{user_id}` | Create a new todo for a user |
| GET | `/todos` | Get all todos |
| GET | `/todo/{todo_id}` | Get specific todo by ID |
| PUT | `/todo/{todo_id}` | Update todo information |
| DELETE | `/todo/{todo_id}` | Delete a todo |

## 🔧 Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/todo-fastapi-app.git
   cd todo-fastapi-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

## 📦 Dependencies

```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-email-validator==2.1.0
```

## 🔍 API Usage Examples

### Create a User
```bash
curl -X POST "http://localhost:8000/user/create_user" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Create a Todo
```bash
curl -X POST "http://localhost:8000/todo/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Learn FastAPI", "description": "Complete the FastAPI tutorial"}'
```

### Get All Todos
```bash
curl -X GET "http://localhost:8000/todos"
```

### Update a Todo
```bash
curl -X PUT "http://localhost:8000/todo/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Master FastAPI", "description": "Become an expert in FastAPI"}'
```

## 🗄️ Database Schema

### Users Table
- `user_id` (Primary Key): Integer
- `name`: String
- `email`: String (validated email format)
- `todos`: Relationship to Todo table

### Todos Table
- `todo_id` (Primary Key): Integer
- `title`: String
- `description`: String
- `user_id` (Foreign Key): Integer

## 🔒 Data Models

### User Models
- `UserCreate`: Name and email fields for user creation
- `UserResponse`: User data with ID and associated todos

### Todo Models
- `TodoCreate`: Title and description for todo creation
- `TodoResponse`: Todo data with ID and user association

## 🛡️ Error Handling

The API includes comprehensive error handling:
- **404 Not Found**: When requested resource doesn't exist
- **422 Validation Error**: When request data is invalid
- **500 Internal Server Error**: For unexpected server errors

## 🎯 Future Enhancements

- [ ] User authentication and authorization
- [ ] Todo categories and tags
- [ ] Due dates and reminders
- [ ] Search and filtering capabilities
- [ ] Pagination for large datasets
- [ ] Unit and integration tests
- [ ] Docker containerization
- [ ] PostgreSQL database option

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Contact

Hamidreza Akbari - hamidreza.akbari1001@gmail.com
Project Link: https://github.com/hamidreza-akbari-eng/todo-fastapi-app

---

⭐ If you found this project helpful, please give it a star!
