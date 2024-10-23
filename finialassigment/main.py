import psutil
import time
import json
import os
from constant import bcolors

file_path = "data.txt"
json_objects = []

class PcAlarmMonitor:
    def __init__(self):
        self.alarms = {
            "cpu": [],
            "memory": [],
            "disk": []
        }
        self.monitoring_active = False

    # Methods to retrieve system information
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent, memory.used, memory.total

    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        return disk.percent, disk.used, disk.total

    # Main menu
    def main_menu(self):
        while True:
            print(bcolors.OKGREEN+"\nMain Menu:")
            print("1. Start Monitoring")
            print("2. List Active Monitoring")
            print("3. Create Alarm")
            print("4. Show Alarms")
            print("5. display Previous Alarms set")
            print("6. Exit"+bcolors.ENDC)

            choice = input(bcolors.CYAN+"\nSelect an option (1-5): "+bcolors.ENDC)

            if choice == '1':
                self.start_monitoring()
            elif choice == '2':
                self.list_active_monitoring()
            elif choice == '3':
                self.alarm_menu()
            elif choice == '4':
                self.show_alarms()
            elif choice == '5':
                self.show_previous_alarms()
            elif choice == '6':
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    # Start monitoring
    def start_monitoring(self):
        if self.monitoring_active:
            print(bcolors.OKGREEN+"\nMonitoring is already active."+bcolors.ENDC)
        else:
            self.monitoring_active = True
            print(bcolors.OKGREEN+"\nMonitoring started."+bcolors.ENDC)
        input("Press any key to return to the main menu.")

    # List active monitoring
    def list_active_monitoring(self):
        if not self.monitoring_active:
            print(bcolors.WARNING+"\nNo active monitoring."+bcolors.ENDC)
        else:
            cpu_usage = self.get_cpu_usage()
            memory_usage, memory_used, memory_total = self.get_memory_usage()
            disk_usage, disk_used, disk_total = self.get_disk_usage()
            print(bcolors.BOLD+"\n Active Monitoring from System:")
            print(f"\nCPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage}% ({memory_used / (1024 ** 3):.1f} GB out of {memory_total / (1024 ** 3):.1f} GB used)")
            print(f"Disk Usage: {disk_usage}% ({disk_used / (1024 ** 3):.1f} GB out of {disk_total / (1024 ** 3):.1f} GB used)")
            print(bcolors.ENDC)
        input(bcolors.CYAN+"\nPress any key to return to the main menu."+bcolors.ENDC)

    # Alarm configuration menu
    def alarm_menu(self):
        while True:
            print(bcolors.BOLD+"\nConfigure Alarm:"+bcolors.ENDC)
            print(bcolors.OKGREEN+"1. CPU Usage")
            print("2. Memory Usage")
            print("3. Disk Usage")
            print("4. Return to Main Menu"+bcolors.ENDC)
            print('-' * 30)
            choice = input(bcolors.CYAN+"\nSelect an option (1-4): "+bcolors.ENDC)

            if choice == '1':
                self.set_alarm('cpu')
            elif choice == '2':
                self.set_alarm('memory')
            elif choice == '3':
                self.set_alarm('disk')
            elif choice == '4':
                break
            else:
                print(bcolors.FAIL+"Invalid choice. Please try again."+bcolors.ENDC)

    # Set an alarm
    def set_alarm(self, alarm_type):
        while True:
            try:
                level = int(input(f"\nSet alarm level for {alarm_type} usage (0-100%): "))
                if 0 <= level <= 100:
                    self.alarms[alarm_type].append(level)
                    print(f"Alarm for {alarm_type} usage set to {level}%.")
                    break
                else:
                    print("Level must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 100.")

    # Show all alarms
    def show_alarms(self):
        print("\nConfigured Alarms:")
        """  sorted_alarms = sorted(
                    [(k, v) for k, values in self.alarms.items() for v in values],
                    key=lambda x: x[0]
                ) """
            
        sorted_alarms = []
        for k, values in self.alarms.items(): # k = cpu, memory, disk , values = [10, 20, 30]
         for v in values:
           sorted_alarms.append((k, v))

        sorted_alarms.sort(key=lambda x: x[0]) #(parameter) key: (Any) -> SupportsRichComparison
        # Print alarms and save them to a file
        if not sorted_alarms:
            print(bcolors.MAGENTA+"No alarms configured."+bcolors.ENDC)
        else:
            for alarm, level in sorted_alarms:
                print(f"{alarm.capitalize()} Alarm: {level}%")
            current_id = sum(1 for line in open(file_path)) + 1 if os.path.exists(file_path) else 1
            new_data = {
                    "id": current_id,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
                    "alarms": sorted_alarms
                }
            with open(file_path, "a") as file:
                    file.write(json.dumps(new_data, indent=2) + "\n" )
        input(bcolors.CYAN+"\nPress any key to return to the main menu."+bcolors.ENDC)

    # Show previous alarms
    def show_previous_alarms(self):
     print("\nPrevious Alarms:")
     if not os.path.exists(file_path):
            print(bcolors.MAGENTA+"No previous alarms."+bcolors.ENDC)
     else:
      try:
         with open(file_path, "r") as file:
          for line in file:
            # Parse each line as a JSON object and add it to the list
            json_objects.append(json.loads(line))
            print(json.dumps(json_objects, indent=2))
      except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
     
     input(bcolors.CYAN+"\nPress any key to return to the main menu."+bcolors.ENDC)
    # Run the application
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    app = PcAlarmMonitor()
    app.run()
