from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Endpoint to submit OTP
@app.route('/generate-otp', methods=['POST'])
def submit_otp():
    # Replace with your actual server URL if different
    url = 'https://sandbox.surepass.io/api/v1/aadhaar-v2/generate-otp'
    
    # Replace with your actual Bearer token
    TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxOTgyNzY2MywianRpIjoiZDNhNmM1YTQtZjUyNS00ZjRiLThlMzUtZjI3ZDYyYTZkMWJjIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LmNvbnNvbGVfMnVsOWRtbnFmMnhmOWFqaGFlY2R0Y3UzcGM5QHN1cmVwYXNzLmlvIiwibmJmIjoxNzE5ODI3NjYzLCJleHAiOjE3MjA0MzI0NjMsImVtYWlsIjoiY29uc29sZV8ydWw5ZG1ucWYyeGY5YWpoYWVjZHRjdTNwYzlAc3VyZXBhc3MuaW8iLCJ0ZW5hbnRfaWQiOiJtYWluIiwidXNlcl9jbGFpbXMiOnsic2NvcGVzIjpbInVzZXIiXX19.fiN7FmCYl4kO-8V0mu5OVZgM3pmASJVyVeq0IOsbS5U'
    
    # Parse JSON data from request
    request_data = request.get_json()
    
    # Extract client_id and otp from JSON payload
    id_number = request_data.get('id_number', '')
    
    
    # Prepare payload and headers
    payload = {
       "id_number": id_number,
    }
    
    headers = {
       'Content-Type': 'application/json',
       'Authorization': f'Bearer {TOKEN}'
    }
    
    # Make POST request to external API
    response = requests.post(url, json=payload, headers=headers)
    
    # Process response from external API
    if response.status_code == 200:
       return jsonify({
           'status': 'success',
           'message': 'OTP generated successful!',
           'response': response.json()
       }), 200
    else:
       return jsonify({
           'status': 'error',
           'message': 'Failed to generate OTP',
           'response_code': response.status_code,
           'response_message': response.text
       }), response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0")
