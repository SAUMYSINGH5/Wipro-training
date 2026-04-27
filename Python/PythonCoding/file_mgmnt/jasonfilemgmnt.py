import json
import os

def write_json(filename):
    data = {
        "people": [
            {"name": "Saumy", "age": 21},
            {"name": "Aarav", "age": 23}
        ]
    }
    with open(filename, "w", newline="") as file:
        json.dump(data, file, indent=4)
    print(f"Wrotr {filename} sucessful")

def read_json(filename):
    with open(filename, "r") as file:
     data= json.load(file)
     for person in data["people"]:
         print(f"Name: {person['name']}, Age: {person['age']}")

def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted Sucessfully")
    else:
        print(f"{filename} does not exist")

filename = "myfile.json"
write_json(filename)
print('Data read from JSON file: ')
read_json(filename)
delete_json(filename)
