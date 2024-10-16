day_of_week = {
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

day = input("Please enter a day of week: ").lower().strip().capitalize()

if day in day_of_week :
    day_number = day_of_week[day]
    print(f"{day} is day {day_number}")
else :
    print("Please enter a valid day")
