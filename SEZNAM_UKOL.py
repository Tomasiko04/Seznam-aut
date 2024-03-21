
seznam_car={"audi":{"palivo":"benzin",
                    "původ":"Německo",
                    "rok":"2010", 
                    "barva":"černá",
                    "max. rychlost:":"250 km/h",
                    "spotřeba":"15/100"},

            "bmw":{"palivo":"nafta",
                    "původ":"Německo",
                    "rok":"2018", 
                    "barva":"modrá",
                    "max. rychlost:":"290 km/h",
                    "spotřeba":"12/100"},

            "skoda":{"palivo":"nafta",
                    "původ":"Česká republika",
                    "rok":"2021", 
                    "barva":"červená",
                    "max. rychlost:":"230 km/h",
                    "spotřeba":"10/100"},

            "bently":{"palivo":"benzin",
                    "původ":"Velká Británie",
                    "rok":"2022", 
                    "barva":"stříbrná",
                    "max. rychlost:":"250 km/h",
                    "spotřeba":"16/100"},

            "mercedes":{"palivo":"benzin",
                    "původ":"Německo",
                    "rok":"2023", 
                    "barva":"zelená",
                    "max. rychlost:":"280 km/h",
                    "spotřeba":"15/100"}}

hodnoty=("palivo","původ","rok","barva","max. rychlost","spotřeba")
oddelovac = "=" * 62
opakovani=True
prvky="ano"


while True:
    menu=input("Co potřebuješ (info/přidat/odebrat/unončit program): ")
    if "info" in menu:
        print("O jakém autě?")

        for i in seznam_car.keys():
            x=i.capitalize()
            print(x.center(62))
        print(oddelovac)



        car=input("Zadej zančku auta: ")
        print("------------------")
        car_male=car.lower()
        
        
        for keys, values in seznam_car[car_male].items():
            print(f"{keys}: {values}")
        print(oddelovac)

    elif "přidat" in menu:

        add_keys=input("Zadejte novou značku auta: ")
        
        add_keys_male=add_keys.lower()
        
        seznam_car[add_keys_male]={}
        print(oddelovac)


        for add_values_hodnoty in hodnoty:
            add_values=input(f"Zadejte {add_values_hodnoty} auta: ")
            seznam_car[add_keys_male][add_values_hodnoty]=add_values

    
    elif "odebrat" in menu:
        odeber=input("Co chctete odebrat vše o autě nebo pouze nekteré informace o něm(auto/informace): ")
        if "auto" in odeber:

            for i in seznam_car.keys():
                x=i.capitalize()
                print(x.center(62))
            print(oddelovac)

            remove_keys=input("Zadejte jaké auto chcete odbrat: ")
            remove_keys_male=remove_keys.lower()
            del seznam_car[remove_keys_male]
        elif "informace" in odeber:
            
            while opakovani:
                
                if "ano" in prvky:

                    for i in seznam_car.keys():
                        x=i.capitalize()
                        print(x.center(62))
                    print(oddelovac)

                    remove_keys=input("Zadejte od jakého auta chcete odbrat informaci: ")


                    car_male=remove_keys.lower()
                    for keys, values in seznam_car[car_male].items():
                        print(f"{keys}: {values}")
                    print(oddelovac)

                    remove_values=input("Zadejte jakou informaci chcete odbrat: ")
                    remove_keys_male=remove_keys.lower()
                    remove_values_male=remove_values.lower()

                    del seznam_car[remove_keys_male][remove_values_male]

                    prvky2=input("Chceš odebrat ještě nějaké prvky (ANO/NE): ")
                    prvky=prvky2.lower()
                elif "ne" in prvky:
                    opakovani=False 
                else:
                    print("Zadal si špatně tvoji hodnotu zkus to znovu.")
                    ##Upravit tak aby se to při chybě neopakovalo###
        else:
            print("Zadal si špatně tvoji hodnotu zkus to znovu.")
        
    elif "unončit program" in menu:
        break  
        
    else:
        print("Zadal si špatně tvoji hodnotu zkus to znovu.")
        
print("Konec programu.")       

### PŘIDAT aby šli přidat i jednotlivé hodnody PŘI PŘIDÁNÍ ###
        
##Upravit tak aby se to při chybě neopakovalo### při špatně zadaném vstupu

## Šlo by přidat ještě upravovaání hodnot v seznamech
## Upravit kód tak aby se psaly jednotky km/h tehdy když nově přidám max. rychlost
        

