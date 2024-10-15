from constant import bcolors
from constant import Alarms
#instantate the class Alarms
start_monitoring = Alarms().start_monitoring
    
class Menu:
    def __init__():
        pass
    def main_menu(self):
        print(bcolors.HEADER + "\nMain Menu:")
        print("1. Start monitoring")
        print("2. List active monitoring")
        print("3. Create alarm")
        print("4. Show alarms")
        print("5. Exit" + bcolors.ENDC)
        
        choice = input(bcolors.OKCYAN +"\nChoose an option (1-5): " + bcolors.ENDC)
        return choice
    def run(self):  
        while True:
            choice = self.main_menu()
            
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