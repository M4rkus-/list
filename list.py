import pickle

def process_command(command, data):
    if command == "save":
        save_data(data)
    elif command == "load":
        return load_data()
    elif command == "add":
        item = input("Enter item to add: ")
        data.append(item)
    elif command == "remove":
        item = input("Enter item to remove: ")
        data.remove(item)
    elif command == "print":
        print(data)

def save_data(data):
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

def load_data():
    with open("data.pkl", "rb") as f:
        return pickle.load(f)

data = []
while True:
    command = input("Enter command (save, load, add, remove, print, exit): ")
    if command == "exit":
        break
    data = process_command(command, data)

