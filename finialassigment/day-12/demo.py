#Functional Programming
# 1. Pure Functions
# 2. First Class Functions

digit =[2,34,25,6,17,8,9]

sort_digit = sorted(digit)
#display sorted digit
print(sort_digit)

#lambda function

addFunc = lambda a,b: a+b
print(addFunc(2,3))


#Monitor class
class Monitoring:
    def __init__(self ,alarm_level, alarm_type):
        self.alarm_level = alarm_level
        self.alarm_type = alarm_type

        self.monitoring_active = False


list_monitoring = [
    Monitoring(75, "CPU"),
    Monitoring(75, "Memory"),
    Monitoring(45, "Disk"),
]


sorted_monitoring = sorted(list_monitoring, key=lambda x: x.alarm_level)

for monitor in sorted_monitoring:
    print(monitor.alarm_level, monitor.alarm_type)

#Higher Order Functions

def greet():
    return 'Hello'

def call_func(greet):
    return greet()
call_func(greet)