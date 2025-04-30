# sql.py
import os
import json

DATA_FOLDER = 'data'

class SQLDatabase:
    def __init__(self, name):
        self.name = name
        self.path = os.path.join(DATA_FOLDER, f"{name}.json")
        if not os.path.exists(DATA_FOLDER):
            os.makedirs(DATA_FOLDER)
        self._load_or_create()

    def _load_or_create(self):
        if not os.path.exists(self.path):
            self.data = {}
            self._save()
        else:
            with open(self.path, 'r') as f:
                self.data = json.load(f)

    def _save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def create_table(self, table_name):
        if table_name not in self.data:
            self.data[table_name] = []
            self._save()

    def insert(self, table_name, record: dict):
        if table_name in self.data:
            self.data[table_name].append(record)
            self._save()
        else:
            raise ValueError(f"Table '{table_name}' does not exist.")

    def select_all(self, table_name):
        return self.data.get(table_name, [])

    def delete_all(self, table_name):
        if table_name in self.data:
            self.data[table_name] = []
            self._save()

    def drop_table(self, table_name):
        if table_name in self.data:
            del self.data[table_name]
            self._save()
