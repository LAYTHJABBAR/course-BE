
# Course Management Backend

This is the backend for the Course Management application, built using Flask and MongoDB. It provides a RESTful API to manage university courses, including functionalities to create, read, update, and delete course records.

## Project Structure


backend/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── utils.py
├── requirements.txt
└── run.py


### Files and Directories

- `backend/`: Contains the main application package.
  - `__init__.py`: Initializes the Flask application and registers blueprints.
  - `app.py`: Entry point for running the Flask application.
  - `config.py`: Configuration file for the application.
  - `models.py`: Contains data normalization functions.
  - `routes.py`: Defines the API routes.
  - `utils.py`: Utility functions for data handling.
- `requirements.txt`: Lists the dependencies required for the project.
- `run.py`: Script to run the Flask application.

## Setup and Installation

### Prerequisites

- Python 3.x
- MongoDB

### Steps to Run the Application

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>/backend
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application:**

    ```bash
    python run.py
    ```

### Configuration

- **MongoDB URI:**
  The MongoDB URI and database name are configured in `config.py`:

  ```python
  class Config:
      MONGO_URI = 'mongodb://localhost:27017/courses_db'
      MONGO_DBNAME = 'courses_db'
  ```

## API Endpoints

### 1. Get Courses

- **URL:** `/api/get_courses`
- **Method:** `GET`
- **Query Parameters:**
  - `search`: (Optional) Search query string to filter courses.
  - `page`: (Optional) Page number for pagination. Default is `1`.
  - `page_size`: (Optional) Number of items per page. Default is `10`.
- **Response:** JSON array of courses.

### 2. Create Course

- **URL:** `/api/create_course`
- **Method:** `POST`
- **Body:** JSON object representing the course to create.
- **Response:** JSON object containing the ID of the created course.

### 3. Update Course

- **URL:** `/api/update_course/<course_id>`
- **Method:** `PUT`
- **Body:** JSON object representing the updated course data.
- **Response:** JSON object indicating the number of matched and modified documents.

### 4. Delete Course

- **URL:** `/api/delete_course/<course_id>`
- **Method:** `DELETE`
- **Response:** JSON object indicating the number of deleted documents.

## Data Handling

- The application downloads initial data from a specified URL and normalizes it using Pandas.
- The data is stored in MongoDB and is set to expire every 10 minutes.
- If the data expires, the application will reload the data from the URL.

## Running the Application

Ensure MongoDB is running on your system. Then, activate the virtual environment and start the Flask application:

```bash
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate  # On Windows

python run.py
```

Visit `http://127.0.0.1:5000/api/get_courses` to interact with the API.

