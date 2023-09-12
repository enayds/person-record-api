from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Replace with your database URL
db = SQLAlchemy(app)
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(120))
    address = db.Column(db.String(200))
    other_details = db.Column(db.String(200))

# Validation function to check data types
def validate_data(data):
    # Define the expected data types for each field
    expected_types = {
        'name': str,
        'age': int,
        'email': str,
        'address': str,
        'other_details': str,
    }

    for field, expected_type in expected_types.items():
        if field in data and not isinstance(data[field], expected_type):
            return False  # Data type validation failed for this field
    return True  # Data type validation passed for all fields


# creating function to search for all possible arguments
def search():
    query = Person.query  # Initialize the query without any filters

    name = request.args.get('name')
    age = request.args.get('age')
    email = request.args.get('email')
    user_id = request.args.get('user_id')

    if name:
        query = query.filter_by(name=name)
    if user_id:
        query = query.filter_by(id=user_id)
    if age:
        query = query.filter_by(age=age)
    if email:
        query = query.filter_by(email=email)

    persons = query.all()

    return persons



    
# fetching all records in the database or based on certain arguments
@app.route("/", methods=["GET"])
def show_records():
    persons = search()
    
    # Convert the records to a JSON-serializable format and return
    records = [
        {
            "id": person.id,
            "name": person.name,
            "age": person.age,
            "email": person.email,
            "address": person.address,
            "other_details": person.other_details
        }
        for person in persons
    ]
    return jsonify(records)


# create and insert record into the database
@app.route("/api", methods=["POST"])
def create_record():
    data = request.json

    # Validate data types before proceeding
    if not validate_data(data):
        return jsonify({"message": "Invalid data types in request"}), 400  # HTTP 400 Bad Request
    
    new_person = Person(
        name=data.get('name'),
        age=data.get('age'),
        email=data.get('email'),
        address=data.get('address'),
        other_details=data.get('other_details')
    )

    try:
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"message": "Insertion successful"}), 201  # HTTP 201 Created
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Invalid insertion. Check data integrity."}), 400  # HTTP 400 Bad Request


# Retrieve a specific record from the database
@app.route('/api/<int:user_id>', methods=["GET"])
def get_record(user_id):
    person = Person.query.get(user_id)

    if person:
        # Convert the person object to a dictionary
        person_data = {
            "id": person.id,
            "name": person.name,
            "age": person.age,
            "email": person.email,
            "address": person.address,
            "other_details": person.other_details
        }
        return jsonify(person_data), 200  # HTTP 200 OK
    else:
        return jsonify({"message": "Person not found"}), 404  # HTTP 404 Not Found


# update record in the database
@app.route("/api/<int:user_id>", methods=["PUT"])
def update_record(user_id):
    # Retrieve the person record by user ID
    person = Person.query.get(user_id)

    if person:
        # Update the person's information with the data from the request
        data = request.json
        person.name = data.get('name', person.name)
        person.age = data.get('age', person.age)
        person.email = data.get('email', person.email)
        person.address = data.get('address', person.address)
        person.other_details = data.get('other_details', person.other_details)

        try:
            db.session.commit()
            return jsonify({"message": "Update successful"}), 200  # HTTP 200 OK
        except:
            db.session.rollback()
            return jsonify({"message": "Invalid update. Check data integrity."}), 400  # HTTP 400 Bad Request
    else:
        return jsonify({"message": "Person not found"}), 404  # HTTP 404 Not Found

# update record(s) from database based on parameters
@app.route("/api/", methods=["PUT"])
def update_records():
    persons_to_update = search()

    if persons_to_update:
        data = request.json
         # Validate data types before proceeding
        if not validate_data(data):
            return jsonify({"message": "Invalid data types in request"}), 400  # HTTP 400 Bad Request
        try:
            for person in persons_to_update:
                person.name = data.get('name', person.name)
                person.age = data.get('age', person.age)
                person.email = data.get('email', person.email)
                person.address = data.get('address', person.address)
                person.other_details = data.get('other_details', person.other_details)

            db.session.commit()
            return jsonify({"message": "Update successful"}), 200  # HTTP 200 OK
        except:
            db.session.rollback()
            return jsonify({"message": "Invalid update. Check data integrity."}), 400  # HTTP 400 Bad Request
    else:
        return jsonify({"message": "No matching records found"}), 404  # HTTP 404 Not Found

# deleting record from database
@app.route("/api/<int:user_id>", methods=["DELETE"])
def delete_record(user_id):
    person = Person.query.get(user_id)

    if person:
        try:
            db.session.delete(person)
            db.session.commit()
            return jsonify({"message": "Deletion successful"}), 200  # HTTP 200 OK
        except:
            db.session.rollback()
            return jsonify({"message": "Invalid deletion. Check data integrity."}), 400  # HTTP 400 Bad Request
    else:
        return jsonify({"message": "Person not found"}), 404  # HTTP 404 Not Found

# deleting record(s) from database based on parameters
@app.route("/api/", methods=["DELETE"])
def delete_records():
    persons_to_delete = search()

    if persons_to_delete:
        try:
            for person in persons_to_delete:
                db.session.delete(person)
            db.session.commit()
            return jsonify({"message": "Deletion successful"}), 200  # HTTP 200 OK
        except:
            db.session.rollback()
            return jsonify({"message": "Invalid deletion. Check data integrity."}), 400  # HTTP 400 Bad Request
    else:
        return jsonify({"message": "No matching records found"}), 404  # HTTP 404 Not Found



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
