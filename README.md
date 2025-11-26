# Django TODO Application

A simple TODO application built with Django with a modern, responsive frontend using Tailwind CSS.

## Features

- Create new TODO items
- View all TODO items
- Delete TODO items
- Responsive web interface with modern styling
- Clean, user-friendly interface

## Requirements

- Python 3.8+
- Django 5.2+

## Installation

1. Clone the repository (if applicable)
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install django
   ```

## Running the Application

1. Make sure you're in the project directory
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open your browser and go to `http://127.0.0.1:8000/`

## Running Tests

To run the application tests:
```bash
python manage.py test todo
```

## Project Structure

```
todo_project/          # Main Django project
└── todo/              # TODO app
    ├── migrations/    # Database migrations
    ├── templates/     # HTML templates
    │   ├── base.html  # Base template with Tailwind CSS
    │   └── todo/
    │       └── index.html  # Main page template with Tailwind styling
    ├── tests.py       # Test cases
    ├── views.py       # View functions
    ├── models.py      # Database models
    └── urls.py        # URL routing for the app
```

## Testing Scenarios Covered

The tests cover the following scenarios:
- Creating a TODO item
- Viewing TODO items
- Adding new TODO items via POST request
- Deleting TODO items
- Handling empty title submissions

## Frontend Enhancements

The frontend has been enhanced with Tailwind CSS to provide:
- Modern, responsive design
- Improved visual hierarchy
- Better user experience
- Clean, intuitive interface
- Consistent styling across all components

## License

This project is licensed under the MIT License.


![AI todo app](/images/todo-app.png)
