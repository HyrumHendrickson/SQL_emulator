# main.py
from setup import run_setup
from sql import SQLDatabase

def parse_insert_fields(fields_str):
    fields = {}
    for pair in fields_str.split():
        if '=' in pair:
            key, value = pair.split('=', 1)
            fields[key] = value
    return fields

def main():
    run_setup()
    db = SQLDatabase('app_database')

    print("Simple SQL Emulator. Type 'EXIT' to quit.")
    while True:
        query = input(">> ").strip()

        if not query:
            continue
        if query.upper() == 'EXIT':
            print("Session ended.")
            break

        parts = query.split()
        command = parts[0].upper()

        try:
            if command == 'CREATE' and parts[1].upper() == 'TABLE':
                db.create_table(parts[2])
                print(f"Table '{parts[2]}' created.")

            elif command == 'INSERT' and parts[1].upper() == 'INTO':
                table = parts[2]
                fields = parse_insert_fields(" ".join(parts[3:]))
                db.insert(table, fields)
                print(f"Inserted into '{table}': {fields}")

            elif command == 'SELECT' and parts[1] == '*' and parts[2].upper() == 'FROM':
                table = parts[3]
                rows = db.select_all(table)
                if not rows:
                    print(f"No data in '{table}'.")
                else:
                    for i, row in enumerate(rows, 1):
                        print(f"{i}: {row}")

            elif command == 'DELETE' and parts[1].upper() == 'FROM':
                table = parts[2]
                db.delete_all(table)
                print(f"All records deleted from '{table}'.")

            elif command == 'DROP' and parts[1].upper() == 'TABLE':
                table = parts[2]
                db.drop_table(table)
                print(f"Table '{table}' dropped.")

            else:
                print("Unknown or malformed command.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
