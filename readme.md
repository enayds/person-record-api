# Person API

The Person API is a Flask-based web service that allows you to perform CRUD (Create, Read, Update, Delete) operations on person records in a database. This README provides instructions on how to set up, run, and use the API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Validation](#validation)
- [Project Structure](#project-structure)
- [UML Diagrams](#uml-diagrams)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up and run the Person API, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/person-api.git
   ```

2. Change to the project directory:

   ```bash
   cd person-api
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Create the SQLite database:

   ```bash
   python
   from app import db
   with app.app_context():
       db.create_all()
   ```

7. Run the application:

   ```bash
   python app.py
   ```

By default, the API will run on `http://127.0.0.1:5000/`.

## Usage

The Person API provides the following endpoints for interacting with person records:

### Endpoints

- **Create a New Record**:

  - Endpoint: `/api`
  - HTTP Method: POST

- **Retrieve All Records or Filter by Parameters**:

  - Endpoint: `/`
  - HTTP Method: GET

- **Retrieve a Specific Record**:

  - Endpoint: `/api/<int:user_id>`
  - HTTP Method: GET

- **Update a Specific Record**:

  - Endpoint: `/api/<int:user_id>`
  - HTTP Method: PUT

- **Update Records Based on Parameters**:

  - Endpoint: `/api/`
  - HTTP Method: PUT

- **Delete a Specific Record**:

  - Endpoint: `/api/<int:user_id>`
  - HTTP Method: DELETE

- **Delete Records Based on Parameters**:

  - Endpoint: `/api/`
  - HTTP Method: DELETE

For detailed information on how to use each endpoint, refer to the [API Documentation](https://github.com/enayds/person-record-api/blob/master/documentation.md).

## Validation

The API includes data type validation to ensure that fields have the correct types. It validates that:

- The name is a string.
- The age is an integer.
- The email is a string.
- The address is a string.
- The other_details is a string.

## Project Structure

The project structure is organized as follows:

- `app.py`: The main Flask application.
- `models.py`: Defines the database schema using SQLAlchemy.
- `README.md`: This documentation file.
- `requirements.txt`: Lists the project dependencies.
- `venv/`: The virtual environment (optional but recommended).

## UML Diagrams

UML diagrams can be found via this [link](https://github.com/enayds/person-record-api/blob/master/Untitled%20Diagram.drawio.svg).

## Known Limitations

- The API assumes that the database is SQLite and the database file is named `mydatabase.db`. You may need to configure the database URI to match your environment.
- Error handling is minimal and can be improved for production use.
- The API does not include authentication or authorization mechanisms, so access control is not enforced.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for using the Person API! If you have any questions or need further assistance, please don't hesitate to reach out.

---

**Note**: Replace the placeholders (`<...>`) with actual values, such as your project's repository URL and the appropriate endpoints and descriptions based on your API design. Additionally, if you have UML diagrams, you can provide links to view them online or include them as image files in your repository.
