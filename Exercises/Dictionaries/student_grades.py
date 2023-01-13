student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    scores = student_scores[student]
    if scores > 90:
      student_grades[student] = "Outstanding"
    elif scores > 80:
        student_grades[student] = "Exceeds expectations"
    elif scores > 70:
        student_grades[student] = "Acceptable"

    else:
        student_grades[student] = "Fail"

print(student_grades)

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille"], "places_visited": ["beach, palace"]},
    "Germany": {"cities_visited" :["Hamburg", "Berlin"], "places_visited": ["bars, restaurants"]}
}

# Nesting a dictionary in a list
travel_vlog = [
    {
        "country": "France",
         "cities_visited": ["Paris", "Marseille"],
         "num_of_places": 10
    },
    {
        "country": "Germany",
         "cities_visited": ["Berlin", "Munich"],
         "num_of_places": 7
    }
]

print(travel_log)
print(travel_vlog)

    
    
    