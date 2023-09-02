#Nicolas Plaza
"""
Calcular el nuevo sueldo de un empleado si obtuvo un incremento del 25% sobre su 
sueldo anterio
"""
sueldo = int(input("ingrese su sueldo actual, para la modificación del 25%: "))
p_t = 0.25
sueldo_act = (sueldo * p_t) + sueldo
print("Su sueldo actual es de:" , round(sueldo_act))