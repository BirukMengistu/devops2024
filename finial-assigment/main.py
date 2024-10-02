import psutil # type: ignore
import time

# Globala variabler
alarms = {
    "cpu": None,
    "memory": None,
    "disk": None
}
# monitoring status 
monitoring_active = False

# Main menu
def main_menu():
    print("\nMain Menu:")
    print("1. Start monitoring")
    print("2. List active monitoring")
    print("3. Create alarm")
    print("4. Show alarms")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")
    return choice

def run():
    while True:
        choice = main_menu()
        
        if choice == '1':
            print('start_monitoring()')
        elif choice == '2':
            print('list_active_monitoring()')
        elif choice == '3':
            print('alarm_menu()')
        elif choice == '4':
            print('show_alarms()')
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()