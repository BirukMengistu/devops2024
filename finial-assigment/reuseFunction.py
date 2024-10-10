import psutil  # type: ignore
import time
import main as rf
# Functions to monitor system resources
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


# function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent, memory.used, memory.total
    
# function to get disk usage
def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent, disk.used, disk.total


# list active Monitoring
def list_active_monitoring(monitoring_active):
    if not monitoring_active:
        print("\nNo monitoring is active.")
    else:
        cpu_usage = get_cpu_usage()
        memory_usage, memory_used, memory_total = get_memory_usage()
        disk_usage, disk_used, disk_total = get_disk_usage()

        print(f"\nCPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}% ({memory_used / (1024 ** 3):.1f} GB of {memory_total / (1024 ** 3):.1f} GB used)")
        print(f"Disk Usage: {disk_usage}% ({disk_used / (1024 ** 3):.1f} GB of {disk_total / (1024 ** 3):.1f} GB used)")
    
    input("\nPress any key to return to the main menu.")

 #Alarm configuration menu
def alarm_menu():
    while True:
        print("\nConfigure alarms:")
        print("1. CPU usage")
        print("2. Memory usage")
        print("3. Disk usage")
        print("4. Return to main menu")

        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            set_alarm('cpu')
        elif choice == '2':
            set_alarm('memory')
        elif choice == '3':
            set_alarm('disk')
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
# Set alarm
def set_alarm(alarm_type):
    while True:
        try:
            level = int(input(f"\nSet level for {alarm_type} usage (0-100%): "))
            if 0 <= level <= 100:
                rf.alarms[alarm_type] = level
                print(f"Alarm for {alarm_type} usage set to {level}%.")
                break
            else:
                print("The level must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 100.")
def show_alarms():
    print("\nConfigured Alarms:")
    #sorted_alarms = {k: v for k, v in sorted(alarms.items(), key=lambda item: item[0])}
    sorted_alarms = dict(sorted(rf.alarms.items()))

    for alarm, level in sorted_alarms.items():
        if level is not None:
            print(f"{alarm.capitalize()} alarm {level}%")
    
    input("\nPress any key to return to the main menu.")


