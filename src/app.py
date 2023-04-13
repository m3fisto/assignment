from flask import Flask, json
import logging
import time
import random
import data
logging.basicConfig(filename='./logs/server_app.log', level=logging.INFO)

api = Flask(__name__)

@api.route('/people/<int:number>/', methods=['GET'])
def get_people(number):
      random_delay()
      if 1<=number<=100:
        return json.dumps(data.people)
      else:
        return json.dumps(data.people_error),404      

@api.route('/planets/<int:number>/', methods=['GET'])
def get_planets(number):
      random_delay()
      if 1<=number<=100:
        return json.dumps(data.planets)
      else:
        return json.dumps(data.planets_error),404  
      

@api.route('/starships/<int:number>/', methods=['GET'])
def get_starships(number):
      random_delay()
      if 1<=number<=100:
        return json.dumps(data.starships)
      else:
        return json.dumps(data.starships_error),404  

def random_delay():
  time.sleep(random.randint(1, 2500)/1000)

if __name__ == '__main__':
    api.run('0.0.0.0',8800,debug=True)