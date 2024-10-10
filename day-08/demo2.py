#dictionary( key value pair)

# dictionary    
import constant as store
#import dictionary as dic
my_dict = store.my_dict
print(my_dict)
print("date 07 10 2024")
print("lecktion list ,tuples,sets, dictionary")
print(type(my_dict))


#print(my_dict["age"])
key =my_dict.keys()
print(key)
values= my_dict.values()

for key,values in my_dict.items():
    print(key,values)
    print(type(values))
    print(type(key))
    print("name:",values["name"])
    print("age:",values["age"])
    print("city:",values["city"])
    print("group:",values["group"])
    print("department:",values["department"])
    print("course:",values["course"])
    print("result:",values["result"])
    print("*"*50)