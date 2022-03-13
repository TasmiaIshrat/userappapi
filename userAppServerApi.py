from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin

import pickle

registeredUsers = []

with open('registeredUsers.pkl', 'wb') as f:
  pickle.dump(registeredUsers, f)
  
  
print('$$$$$$: ',registeredUsers)



"""

with open('registeredUsers.pkl', 'rb') as f:
    
   registeredUsers = pickle.load(f)
   
"""
   


app = Flask(__name__)

CORS(app)



@app.route('/getUsers', methods=["GET"])
@cross_origin()
def getUsers():
    
    
    return jsonify(error=False, message='All Registered Users', data=registeredUsers), 200



@app.route('/registerUser', methods=["POST"])
@cross_origin()
def get_answer():
    
    if request.method == 'POST':
        
        userDictionary = {}
        
        userDictionary['position'] = len(registeredUsers)+1
        
        userDictionary['firstName'] = request.form.get('firstName')
        
        userDictionary['lastName'] = request.form.get('lastName')
        
        userDictionary['gender'] = request.form.get('gender')
        
        userDictionary['dateOfBirth'] = request.form.get('dateOfBirth')
        
        userDictionary['city'] = request.form.get('city')
        
        userDictionary['phone'] = request.form.get('phone')
        
        userDictionary['email'] = request.form.get('email')
        
        registeredUsers.append(userDictionary)
        
        with open('registeredUsers.pkl', 'wb') as f:
            
                pickle.dump(registeredUsers, f)    
                                
       
        return jsonify(error=False, message='answer to the posted question', data="Registration Success"), 200
    

if __name__ == '__main__':
    app.run()
