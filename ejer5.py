# Nicolas Plaza
"""
Tres personas deciden inver=r su dinero para fundar una empresa. Cada una de ellas 
invierte una can=dad dis=nta. Obtener el porcentaje que cada quien invierte con 
respecto a la can=dad total inver=d
"""
print("ingresar el dinero de las inverciones")
person1 = int(input("Primera invercion: "))
person2 = int(input("segunda inverción: "))
person3 = int(input("Tercera inverción: "))
total = person1 + person2 + person3
p_person1 = (100 / total) * person1
p_person2 = (100 / total) * person2
p_person3 = (100 / total) * person3
print("inverciones que hicieron en porcentaje:")
print(round(p_person1) , "%")
print(round(p_person2) , "%")
print(round(p_person3) , "%")