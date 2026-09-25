# My Flask Project

This is a simple Flask web application.

## Project Structure

```
my-flask-project
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   flask run
   ```

## Usage

Visit `http://127.0.0.1:5000` in your web browser to access the application.

## License

This project is licensed under the MIT License.