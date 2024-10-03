import psutil 
import time

def get_cpu_usage():
    """Get the current CPU usage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Get the current memory usage."""
    memory_info = psutil.virtual_memory()
    return memory_info.percent

def get_disk_usage():
    """Get the current disk usage."""
    disk_info = psutil.disk_usage('/')
    return disk_info.percent

def print_menu():
    """Print the console menu."""
    print("\nSystem Information Menu:")
    print("1. CPU Usage")
    print("2. Memory Usage")
    print("3. Disk Usage")
    print("4. Exit")

def handle_menu_selection():
    """Handle user input from the menu."""
    while True:
        print_menu()
        choice = input("\nSelect an option (1-4): ")

        if choice == '1':
            print(f"Current CPU Usage: {get_cpu_usage()}%")
        elif choice == '2':
            print(f"Current Memory Usage: {get_memory_usage()}%")
        elif choice == '3':
            print(f"Current Disk Usage: {get_disk_usage()}%")
        elif choice == '4':
            print("Exiting the application...")
            break
        else:
            print("Invalid option, please try again.")

def monitor_system():
    """Monitor the system and trigger alarms if thresholds are exceeded."""
    cpu_threshold = 80  # Set CPU threshold for alarms (example)
    memory_threshold = 80  # Set memory threshold for alarms (example)
    disk_threshold = 90  # Set disk threshold for alarms (example)

    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()

        if cpu_usage > cpu_threshold:
            print(f"ALARM: CPU usage is too high! ({cpu_usage}%)")
        if memory_usage > memory_threshold:
            print(f"ALARM: Memory usage is too high! ({memory_usage}%)")
        if disk_usage > disk_threshold:
            print(f"ALARM: Disk usage is too high! ({disk_usage}%)")

        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    print("Welcome to the System Monitoring Application.")

    # First show the interactive menu
    handle_menu_selection()

    # After the user interacts, start monitoring the system
    print("Starting system monitoring for alarms...")
    monitor_system()
