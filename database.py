from pymongo import MongoClient
from datetime import date

ujjawal = MongoClient("localhost", 27017)

db = ujjawal["superhuman"]

diet_collection = db["diet"]
exercise_collection = db["exercise"]
sleep_collection = db["sleep"]

print("Choose what data you want to give: \n1. Diet\n2. Exercise\n3. Sleep\n")
option = int(input("Enter option here: "))


def diet():
    print("Enter your Diet Nutritional value here:\n")
    calorie = int(input("Enter your today total calorie: "))
    protien = int(input("Enter your today total protien: "))
    carbs = int(input("Enter your today total carbs: "))
    fiber = int(input("Enter your today total fiber: "))
    fat = int(input("Enter your today total fat: "))
    diet_doc = {"calorie":calorie,"protien":protien,"carbs":carbs,"fiber":fiber,"fat":fat,"date":date.today().isoformat()}
    diet_collection.insert_one(diet_doc)
    print("Successfully inserted the sleep data")

def exercise():
    print("Enter your Diet Nutritional value here:\n")
    face_ice = int(input("Enter how many minute you have dip face into ice: "))
    pushup = int(input("Enter how many reps done of pushup: "))
    pullup = int(input("Enter how many reps done of pullup: "))
    plank = int(input("Enter how many reps done of plank: "))
    calf_raises = int(input("Enter how many reps done of calf raises: "))
    squat = int(input("Enter how many reps done of squat: "))
    reverse_plank = int(input("Enter how many reps done of reverse_plank: "))
    exercise_doc = {"face_ice":face_ice,"pushup":pushup,"pullup":pullup,"plank":plank,"reverse_plank":reverse_plank,"calf_raises":calf_raises,"squat":squat,"date":date.today().isoformat()}
    exercise_collection.insert_one(exercise_doc)
    print("Successfully inserted the exercise data")

def sleep():
    sleep_hr = float(input("Enter how many hour your sleep:\n"))
    sleep_doc = {"hours": sleep_hr,"date":date.today().isoformat()}
    sleep_collection.insert_one(sleep_doc)
    print("Successfully inserted the sleep data")

def options(option):
    if option == 1:diet()
    elif option == 2:exercise()
    elif option == 3:sleep()

data = options(option)