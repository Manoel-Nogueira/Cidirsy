import database
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initializing the database
database.CreateDataBase()
database.CreateTables()
database.InsertData()

# Function to return all symptoms
@app.route("/list_symptoms", methods=["GET"])
def ListAllSymptoms() :

    try :

        symptoms = database.ShowSymptoms()

        response = [

            {

                "id": symptom[0],
                "snome": symptom[1]

            }
            for symptom in symptoms

        ]

        return jsonify(response) 
    
    except Exception as e :

        return jsonify(str(e))  



# Function to return the disease based on symptoms
@app.route("/disease", methods=["POST"])
def ConsultDisease() :

    data = request.get_json()
    symptoms = list(set(data.get("symptoms", []))) 

    try :
    
        diseases = database.ShowDiseases(symptoms) 

        response = [

            {

                "dnome": disease[0],
                "sn": disease[1]

            }
            for disease in diseases

        ]

        return jsonify(response) 
    
    except Exception as e :

        return jsonify(str(e))  

if __name__ == "__main__" :

    app.run(debug=True)
