from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_animal', methods=['GET'])
def get_animal():
    #we need to return one of a selection of animals. First we write a 
    # selection of animals and use 'random.choice' to choose a random animal
    return random.choice(['cow', 'pig', 'horse']

@app.route('/get_noise', methods=['POST']) #we need to allow the proper methods!
def get_noise():
    noises = { #define a dictionary called 'noises', where the KEYS are the animals and the noises are the VAALUES
        "cow" : "moo"
        "pig" : "oink"
        "horse" : "neigh"
    }
    return noises[request.data.decode('utf-8')]
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)