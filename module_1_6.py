my_dict ={"Andre": 2001, "Vitek": 1999, "Olga": 1983}
print(my_dict)
print(my_dict["Vitek"]) #1
print (my_dict.get("Vitek"))#2
print (my_dict.get("Oleg"))
my_dict.update({"Nik": 1993, "Irina": 1962})
print(my_dict)
a = my_dict.pop("Vitek")
print(a)
print(my_dict)