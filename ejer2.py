# Author: Nicolas Plaza
"""
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el 
vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las 
tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta 
su sueldo base y comisiones.
"""

sueldo_n = int(input("ingresar sueldo fijo: "))
Bono = 0.1 + 0.1 + 0.1
pago_mes = sueldo_n * Bono
pago_mes = int(pago_mes)
print("su sueldo mas los bono seria un total de" , pago_mes)