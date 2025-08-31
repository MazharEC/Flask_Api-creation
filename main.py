from flask import Flask, jsonify, request
from createTableOperation import createTables
from addOperation import create_user
from readOperation import authenticate_user

app = Flask(__name__)

@app.route('/')
def test_api():
    return 'Hello, World!'

@app.route('/createUser', methods=['POST'])
def create_user(): 
    try:    
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        phoneNumber = request.form['phone_number']
        pinCode = request.form['pin_code']

    
        userId = create_user(
            name=name, 
            password=password, 
            email=email, 
            address=address, 
            phoneNumber=phoneNumber, 
            pinCode=pinCode
        )

        return jsonify({'message' : str(userId), 'status' : 400})
    
    except Exception as error:
        return jsonify({'message' : str(error), 'status' : 400})
    

@app.route('/login', methods = ['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']

        user = authenticate_user(email=email, password=password)
        
        if user:
            return jsonify({'message' : user[1], 'status' : 200})
        else:
            return jsonify({'message': "invalid email or password", 'status' : 400})
    except Exception as error:
        return error

        

if __name__ == '__main__':
    createTables()
    app.run(debug=True)