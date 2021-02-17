countries = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin", "Hamburg"],
}

for country in countries :
    print(countries[country])
countries_cities = [
    {
      "country": "France",
      "cities_visited": ["Paris","Lille","Dijon"],
      "total_visits":0
    },
    {"country": "Germany",
     "cities_visited":["Berlin", "Hamburg"],
     "total_visits":0
     },
]
for travel_log in countries_cities:
    print(travel_log)
