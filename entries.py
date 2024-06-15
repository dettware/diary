import os

# ANSI color escape sequences
GREEN = '\033[92m'  # Green color
RESET = '\033[0m'   # Reset color

def write_entry():
    entry = input("Write your diary entry:\n")
    entry_name = input("Enter a name for your entry (this will be the filename): ") + '.txt'
    entry_path = os.path.join('entries', entry_name)
    
    with open(entry_path, 'w') as file:
        file.write(entry)
    
    print(f"Entry '{entry_name}' saved successfully in 'entries' folder.\n")

def list_entries():
    entry_files = os.listdir('entries')
    if not entry_files:
        print("No entries found.")
    else:
        print("Available entries:")
        for i, entry_file in enumerate(entry_files, start=1):
            print(f"{i}. {entry_file}")

def read_entry(entry_number):
    entry_files = os.listdir('entries')
    if entry_number <= 0 or entry_number > len(entry_files):
        print("Invalid entry number.")
    else:
        selected_entry = entry_files[entry_number - 1]
        entry_path = os.path.join('entries', selected_entry)
        
        with open(entry_path, 'r') as file:
            entry_content = file.read()
        
        print(f"\n--- {selected_entry} ---\n")
        print(f"{GREEN}{entry_content}{RESET}")  # Print entry content in green

# Main program loop
while True:
    print("\n=== Welcome to Your Diary ===")
    print("1. Write a new entry")
    print("2. List all entries")
    print("3. Read an entry")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        write_entry()
    elif choice == '2':
        list_entries()
    elif choice == '3':
        entry_number = int(input("Enter the number of the entry you want to read: "))
        read_entry(entry_number)
    elif choice == '4':
        print("Exiting the diary. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
