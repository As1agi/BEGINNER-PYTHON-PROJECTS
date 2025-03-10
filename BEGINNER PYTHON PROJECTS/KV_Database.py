import os

KV_database = {}

def clear_screen():
    # Clear the screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        choice = input(" press (P) to post a value \n press (G) to get a value \n press (V) to view all values and key \n press (D) to delete a key \n press (E) to exit \n")

        if choice.upper() == "P":
            key = input("KEY::")
            value = input("VALUE::")
            KV_database[key] = value
            print(f'{key} with the value {value} has been added')

        elif choice.upper() == "G":
            key = input("KEY::")
            value = KV_database.get(key, "Key not found")
            print(f'KEY::{key}\tVALUE::{value}')

        elif choice.upper() == "V":
            print("All key-value pairs:")
            for key, value in KV_database.items():
                print(f"KEY::{key}\tVALUE::{value}")

        elif choice.upper() == "D":
            key = input("KEY::")
            if key in KV_database:
                del KV_database[key]
                print(f'the KEY::{key} has been deleted')
            else:
                print(f'Key {key} not found')

        elif choice.upper() == "E":
            print("Exiting...")
            break

        else:
            print("INPUT A VALID KEY\n")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()