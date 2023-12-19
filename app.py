# app.py
from flask import Flask, request
from src.controller.encounter_controller import EncounterController

app = Flask(__name__)
controller = EncounterController()

@app.route('/encounter', methods=['GET'])
def get_data():
    return controller.get_encounter()

@app.route('/encounter', methods=['PUT'])
def update_data():
    data = request.json
    return controller.update_encounter(data)

if __name__ == "__main__":
    app.run(debug=True)
