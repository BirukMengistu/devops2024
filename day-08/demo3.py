# lesseon 8: class and object
# 3. class with constructor
# 4. class with method
# 5. class with multiple objects

# date 07 10 2024

import constant as store
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
print(bcolors.HEADER+"Class of Bil"+bcolors.ENDC)
print(bcolors.OKBLUE+'*'*50+bcolors.ENDC)
Toyota = store.Toyota('Toyota','Corolla',2022 ,'blue')

Toyota.bil_info()

print(bcolors.OKBLUE+'*'*100+bcolors.ENDC)

Volvo = store.Volvo('Volvo','V60',2021,'red')
Volvo.bil_info()
Volvo.__str__()
print(bcolors.OKBLUE+'*'*100+bcolors.ENDC)

BMW = store.BMW('BMW','X5',2020,'black')
BMW.bil_info()
BMW.__str__()