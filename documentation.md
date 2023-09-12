## Person API Documentation

This API allows you to perform CRUD (Create, Read, Update, Delete) operations on person records in a database.

### Introduction

The Person API is designed to manage person records with the following attributes:

- **id**: Unique identifier for each person.
- **name**: The person's name (string).
- **age**: The person's age (integer).
- **email**: The person's email address (string).
- **address**: The person's address (string).
- **other_details**: Additional details about the person (string).

### Standard Formats for Requests and Responses

#### Request Format

All requests to the API should be in JSON format. The JSON structure should match the attributes of the person record.

Example Create Request:
```json
{
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": "123 Main St",
    "other_details": "Some details about John"
}
```

#### Response Format

The API will respond with JSON objects for most operations. The response format includes a message and, in some cases, the retrieved or modified data.

Example Success Response:
```json
{
    "message": "Insertion successful"
}
```

Example Error Response:
```json
{
    "message": "Invalid insertion. Check data integrity."
}
```

### Endpoints

#### Create a New Record

- **Endpoint**: `/api`
- **HTTP Method**: POST
- **Description**: Creates and inserts a new person record into the database.
- **Request Format**: JSON
- **Response Format**: JSON
- **Possible Responses**:
  - 201 Created: The record was successfully created.
  - 400 Bad Request: Invalid data types in the request.

#### Retrieve All Records or Filter by Parameters

- **Endpoint**: `/`
- **HTTP Method**: GET
- **Description**: Retrieves all person records in the database or filters records based on query parameters (e.g., name, age, email, user_id).
- **Request Format**: None (query parameters are used for filtering)
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: Records were successfully retrieved.
  - 404 Not Found: No matching records found.

#### Retrieve a Specific Record

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: GET
- **Description**: Retrieves a specific person record by user ID.
- **Request Format**: None
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: The record was successfully retrieved.
  - 404 Not Found: Person not found.

#### Update a Specific Record

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: PUT
- **Description**: Updates a specific person record by user ID.
- **Request Format**: JSON
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: The record was successfully updated.
  - 400 Bad Request: Invalid data types in the request.
  - 404 Not Found: Person not found.

#### Update Records Based on Parameters

- **Endpoint**: `/api/`
- **HTTP Method**: PUT
- **Description**: Updates person records based on query parameters (e.g., name, age, email).
- **Request Format**: JSON
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: Records were successfully updated.
  - 400 Bad Request: Invalid data types in the request.
  - 404 Not Found: No matching records found.

#### Delete a Specific Record

- **Endpoint**: `/api/<int:user_id>`
- **HTTP Method**: DELETE
- **Description**: Deletes a specific person record by user ID.
- **Request Format**: None
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: The record was successfully deleted.
  - 404 Not Found: Person not found.

#### Delete Records Based on Parameters

- **Endpoint**: `/api/`
- **HTTP Method**: DELETE
- **Description**: Deletes person records based on query parameters (e.g., name, age, email).
- **Request Format**: JSON
- **Response Format**: JSON
- **Possible Responses**:
  - 200 OK: Records were successfully deleted.
  - 400 Bad Request: Invalid data types in the request.
  - 404 Not Found: No matching records found.

### Known Limitations and Assumptions

- The API assumes that the database is SQLite and the database file is named `mydatabase.db`. You may need to configure the database URI to match your environment.
- Data type validation is performed to ensure that fields are of the correct types (e.g., name is a string, age is an integer).
- The API does not perform validation for other constraints like email format.
- Error handling is minimal and can be improved for production use.
- The API does not include authentication or authorization mechanisms, so access control is not enforced.
- The API runs in debug mode by default. In a production environment, you should disable debug mode and use a production-ready database.
