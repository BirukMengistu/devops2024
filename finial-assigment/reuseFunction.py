import psutil  # type: ignore
import time

# Functions to monitor system resources
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent, memory.used, memory.total

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent, disk.used, disk.total

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
