travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "counrty": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]
def new_countries(new_country, num_of_visits, places):
    new_entry = {}
    new_entry["country"] = new_country
    new_entry["visits"] = num_of_visits
    new_entry["cities"] = places
    travel_log.append(new_entry)

new_countries("Russia", 4, ["Moscow," "Saint Petersburg"])
print(travel_log)