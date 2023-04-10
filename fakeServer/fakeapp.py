from flask import Flask, json
import logging
import time
import random

logging.basicConfig(filename='record.log', level=logging.INFO)

people = [{"name": "Obi Wan Kenobi","force":"Light Side"}]
people_error = [{"message": "Person Not Found"},{"Status Code": "404"}]
planets = [{"planet_name": "Dagobah"}]
planets_error = [{"message": "Planet Not Found"},{"Status Code": "404"}]
starships = [{"starship_name": "Millennium Falcon"}]
starships_error = [{"message": "StarShip Not Found"},{"Status Code": "404"}]

api = Flask(__name__)

@api.route('/people/<int:number>/', methods=['GET'])
def get_people(number):
      if 1<=number<=100:   
        time.sleep(random.randint(1, 2500)/1000)
        return json.dumps(people)
      else:
        return json.dumps(people_error),404      

@api.route('/planets/<int:number>/', methods=['GET'])
def get_planets(number):
      if 1<=number<=100:
        return json.dumps(planets)
      else:
        return json.dumps(planets_error),404  
      

@api.route('/starships/<int:number>/', methods=['GET'])
def get_starships(number):
      if 1<=number<=100:
        return json.dumps(starships)
      else:
        return json.dumps(starships_error),404  

if __name__ == '__main__':
    api.run('0.0.0.0',8085,debug=True)