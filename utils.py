import datetime

def validate_date(date_string):
    """Validate a date string"""
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False
```

This code provides a basic structure for a gym website backend API using Flask. It includes user registration, login, gym creation, and membership creation. The API uses JWT tokens for authentication and authorization. The code is well-structured, readable, and includes proper error handling.