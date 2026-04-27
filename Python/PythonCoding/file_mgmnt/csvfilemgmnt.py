import csv
import os

def write_csv(filename):
    data = [
        {"name": "Saumy", "age": 21},
        {"name": "Aarav", "age": 23}
    ]
    columnnames = ["name","age"]
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)
    print('CSV file Written Susessfully')

def read_csv(filename):
    with open(filename, "r", newline="\n") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}, Age: {row['age']}")
def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted Sucessfully")
    else:
        print(f"{filename} does not exist")

filename = "myfile.csv"
write_csv(filename)
print('Data read from CSV file: ')
read_csv(filename)
delete_csv(filename)