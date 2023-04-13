baseUrl = 'http://127.0.0.1:8800'
fullUrl = 'http://127.0.0.1:8800/people/12'
people = [{
	"name": "Wilhuff Tarkin",
	"height": "180",
	"mass": "unknown",
	"hair_color": "auburn, grey",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "64BBY",
	"gender": "male",
	"homeworld": "https://swapi.dev/api/planets/21/",
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/6/"
	],
	"species": [],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-10T16:26:56.138000Z",
	"edited": "2014-12-20T21:17:50.330000Z",
	"url": "https://swapi.dev/api/people/12/"
}]
people_error = [{"message": "Person Not Found"},{"Status Code": "404"}]
planets = [{
	"name": "Utapau",
	"rotation_period": "27",
	"orbital_period": "351",
	"diameter": "12900",
	"climate": "temperate, arid, windy",
	"gravity": "1 standard",
	"terrain": "scrublands, savanna, canyons, sinkholes",
	"surface_water": "0.9",
	"population": "95000000",
	"residents": [
		"https://swapi.dev/api/people/83/"
	],
	"films": [
		"https://swapi.dev/api/films/6/"
	],
	"created": "2014-12-10T12:49:01.491000Z",
	"edited": "2014-12-20T20:58:18.439000Z",
	"url": "https://swapi.dev/api/planets/12/"
}]
planets_error = [{"message": "Planet Not Found"},{"Status Code": "404"}]
starships = [{
	"name": "X-wing",
	"model": "T-65 X-wing",
	"manufacturer": "Incom Corporation",
	"cost_in_credits": "149999",
	"length": "12.5",
	"max_atmosphering_speed": "1050",
	"crew": "1",
	"passengers": "0",
	"cargo_capacity": "110",
	"consumables": "1 week",
	"hyperdrive_rating": "1.0",
	"MGLT": "100",
	"starship_class": "Starfighter",
	"pilots": [
		"https://swapi.dev/api/people/1/",
		"https://swapi.dev/api/people/9/",
		"https://swapi.dev/api/people/18/",
		"https://swapi.dev/api/people/19/"
	],
	"films": [
		"https://swapi.dev/api/films/1/",
		"https://swapi.dev/api/films/2/",
		"https://swapi.dev/api/films/3/"
	],
	"created": "2014-12-12T11:19:05.340000Z",
	"edited": "2014-12-20T21:23:49.886000Z",
	"url": "https://swapi.dev/api/starships/12/"
}]
starships_error = [{"message": "StarShip Not Found"},{"Status Code": "404"}]