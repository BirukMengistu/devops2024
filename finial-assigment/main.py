import psutil # type: ignore
import time
import reuseFunction as rf
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




# Globala variabler
alarms = {
    "cpu": None,
    "memory": None,
    "disk": None
}
# monitoring status 
monitoring_active = False

# Monitoring
def start_monitoring():
    global monitoring_active
    monitoring_active = True
    print(bcolors.OKBLUE+"\nMonitoring started.\nPress any key to return to the main menu."+bcolors.ENDC)
    input()




# Main menu
def main_menu():
    print(bcolors.HEADER + "\nMain Menu:")
    print("1. Start monitoring")
    print("2. List active monitoring")
    print("3. Create alarm")
    print("4. Show alarms")
    print("5. Exit" + bcolors.ENDC)
    
    choice = input(bcolors.OKCYAN +"\nChoose an option (1-5): " + bcolors.ENDC)
    return choice

def run():
    while True:
        choice = main_menu()
        
        if choice == '1':
            start_monitoring()
        elif choice == '2':
            print(bcolors.BOLD+"List active monitoring")
            print(bcolors.OKGREEN+"Monitoring active: "+str(monitoring_active))
            rf.list_active_monitoring(monitoring_active)
            print(bcolors.ENDC)
            print(bcolors.ENDC)
        elif choice == '3':
            print(bcolors.WARNING )
            rf.alarm_menu()
            print(bcolors.ENDC)
        elif choice == '4':
            print(bcolors.OKGREEN+'show_alarms()')
            rf.show_alarms()
            print(bcolors.ENDC)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()