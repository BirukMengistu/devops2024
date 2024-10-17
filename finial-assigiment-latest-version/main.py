import psutil 
import json
import time
from constant import bcolors
file_path = "Note.txt"
class MonitoringApp:
    def __init__(self):
        self.alarms = {
            "cpu": [],
            "memory": [],
            "disk": []
        }
        self.monitoring_active = False

    # Funktioner för att hämta systeminformation
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        memory = psutil.virtual_memory()
        return memory.percent, memory.used, memory.total

    def get_disk_usage(self):
        disk = psutil.disk_usage('/')
        return disk.percent, disk.used, disk.total

    # Huvudmeny
    def main_menu(self):
        while True:
            print(bcolors.HEADER+"\nHuvudmeny:")
            print("1. Starta övervakning")
            print("2. Lista aktiv övervakning")
            print("3. Skapa larm")
            print("4. Visa larm")
            print("5. Avsluta"+bcolors.ENDC)

            choice = input("\nVälj ett alternativ (1-5): ")

            if choice == '1':
                self.start_monitoring()
            elif choice == '2':
                self.list_active_monitoring()
            elif choice == '3':
                self.alarm_menu()
            elif choice == '4':
                self.show_alarms()
            elif choice == '5':
                print("Avslutar applikationen.")
                break
            else:
                print("Felaktigt val. Försök igen.")

    # Starta övervakning
    def start_monitoring(self):
        if self.monitoring_active:
            print("\nÖvervakning är redan aktiv.")
        else:
            self.monitoring_active = True
            print(bcolors.OKCYAN+"\nÖvervakning startad.")
        input("Tryck valfri tangent för att gå tillbaka till huvudmenyn."+bcolors.ENDC)

    # Lista aktiv övervakning
    def list_active_monitoring(self):
        if not self.monitoring_active:
            print("\nIngen övervakning är aktiv.")
        else:
            cpu_usage = self.get_cpu_usage()
            memory_usage, memory_used, memory_total = self.get_memory_usage()
            disk_usage, disk_used, disk_total = self.get_disk_usage()

            print(f"{bcolors.WARNING}\nCPU Användning: {cpu_usage}%")
            print(f"Minnesanvändning: {memory_usage}% ({memory_used / (1024 ** 3):.1f} GB av {memory_total / (1024 ** 3):.1f} GB använt)")
            print(f"Diskanvändning: {disk_usage}% ({disk_used / (1024 ** 3):.1f} GB av {disk_total / (1024 ** 3):.1f} GB använt)")
        input("\nTryck valfri tangent för att gå tillbaka till huvudmenyn."+bcolors.ENDC)

    # Meny för att konfigurera larm
    def alarm_menu(self):
        while True:
            print(bcolors.OKGREEN+"\nKonfigurera larm:")
            print("1. CPU användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("4. Tillbaka till huvudmenyn" +bcolors.ENDC)

            choice = input("\nVälj ett alternativ (1-4): ")

            if choice == '1':
                self.set_alarm('cpu')
            elif choice == '2':
                self.set_alarm('memory')
            elif choice == '3':
                self.set_alarm('disk')
            elif choice == '4':
                break
            else:
                print("Felaktigt val. Försök igen.")

    # Ställa in ett larm
    def set_alarm(self, alarm_type):
        while True:
            try:
                level = int(input(f"\nStäll in nivå för {alarm_type}-användning (0-100%): "))
                if 0 <= level <= 100:
                    self.alarms[alarm_type].append(level)
                    print(f"Larm för {alarm_type}-användning satt till {level}%.")

                    break
                else:
                    print("Nivån måste vara mellan 0 och 100.")
            except ValueError:
                print("Felaktig inmatning. Ange en siffra mellan 0 och 100.")

    # Visa alla larm
    def show_alarms(self):
        print("\nKonfigurerade larm:")
        sorted_alarms = sorted(
            [(k, v) for k, values in self.alarms.items() for v in values],
            key=lambda x: x[0]
        )

        if not sorted_alarms:
            print("Inga larm konfigurerade.")

        else:
            for alarm, level in sorted_alarms:
                print(f"{alarm.capitalize()} larm {level}%")
                
                # Create a new JSON object with id and timestamp
            new_data = {
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),
                    "alarms": self.alarms
                }

                # Open the file in append mode and write the new JSON object
            with open('Note.txt', "a") as file:
                    file.write(json.dumps(new_data , indent=4) + "\n")
                    input("\nTryck valfri tangent för att gå tillbaka till huvudmenyn.")

    # Starta applikationen
    def run(self):
        self.main_menu()

if __name__ == "__main__":
    app = MonitoringApp()
    app.run()
