import requests
import json

# Define the base URL of your API
base_url = "http://localhost:5000"  # Replace with your API URL

# Function to print the response in a pretty format
def pretty_print_response(response):
    print(f"Status Code: {response.status_code}")
    print("Response Body:")
    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print(response.text)

# Create a new record
data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "address": "123 Main St",
    "other_details": "Some details about John"
}
response = requests.post(f"{base_url}/api", json=data)
pretty_print_response(response)

# Retrieve all records
response = requests.get(f"{base_url}/")
pretty_print_response(response)

# Retrieve a specific record by ID
user_id = 3  # Replace with the desired user ID
response = requests.get(f"{base_url}/api/{user_id}")
pretty_print_response(response)

# Update a specific record by ID
data = {
    "name": "Updated Name",
    "age": 35,
    "email": "updated@example.com"
}
response = requests.put(f"{base_url}/api/{user_id}", json=data)
pretty_print_response(response)

# Delete a specific record by ID
response = requests.delete(f"{base_url}/api/{user_id}")
pretty_print_response(response)

# Update records based on parameters
update_data = {
    "name": "Updated Name",
    "age": 35,
    "email": "updated@example.com"
}
response = requests.put(f"{base_url}/api/", json=update_data)
pretty_print_response(response)

# Delete records based on parameters
delete_data = {
    "name": "John Doe"
}
response = requests.delete(f"{base_url}/api/", json=delete_data)
pretty_print_response(response)
