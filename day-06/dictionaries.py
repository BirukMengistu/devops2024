things=[    {"name":"John", "age":30},
        {"name":"Jane", "age":25},
    {"name":"Peter", "age":35},
    {"name":"Emma", "age":40}
]
state={
    "Sweden": "ST",
    "Norway": "OS",
    "Finland": "Hki",
    "Denmark": "CPH"
}
cites={
    "Sweden": ['Stockholm','Göteborg','Malmö','Uppsala','Västerås','Örebro','Linköping','Helsingborg','Jönköping','Norrköping','Lund','Umeå','Gävle','Borås','Eskilstuna','Södertälje','Karlstad','Täby','Växjö','Halmstad','Luleå','Östersund','Borlänge','Trollhättan','Falun','Kalmar','Karlskrona','Kristianstad','Skövde','Skellefteå','Nyköping','Alingsås','Lidingö','Ängelholm','Sandviken','Kungsbacka','Vänersborg','Motala','Lidköping','Enköping','Piteå','Visby','Västervik','Nässjö','Kiruna','Falkenberg','Boden','Katrineholm','Värnamo','Kungälv'],
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen"
}
cites['Sweden']
things[0]["age"] = 31
print(things[0]["age"])
print(things , "\n")
print(cites['Sweden'])
#------------------------------------------------
print('-'*50)
print("Dictionary keys:")
print(state.keys())
print('*'*50)
print("Dictionary values:")
print(state.values())

print('*'*50)
print("Dictionary items: iterates over the dictionary and returns each key-value pair as a tuple:")

for key, value in state.items():
    print(key, value)
print('-'*50)
print("Dictionary items: method like get and setdefault:")

print(state.get("Sweden"))
print(state.get("Norway"))
setdefault = cites.setdefault("Sweden", "Stockholm")  
print(setdefault)
print('-'*50)      