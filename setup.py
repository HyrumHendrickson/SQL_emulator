# setup.py
import json
import os

SETUP_FILE = 'setup.json'

def load_setup():
    if not os.path.exists(SETUP_FILE):
        return {"has_been_setup": False, "name": None}
    with open(SETUP_FILE, 'r') as f:
        return json.load(f)

def save_setup(data):
    with open(SETUP_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def run_setup():
    setup_data = load_setup()
    if not setup_data.get("has_been_setup", False):
        name = input("Enter your name to complete setup: ")
        setup_data["name"] = name
        setup_data["has_been_setup"] = True
        save_setup(setup_data)
        print(f"Setup complete. Welcome, {name}!")
    return setup_data
