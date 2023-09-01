#Nicolas Plaza
"""
1) Una =enda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuánto deberá pagar finalmente por su compra.
"""

compra = int(input("Ingrese el total de su compra, para apricarle el descuento:  "))
descuento = 0.15
p_realizar = int((compra * descuento) + compra)
print("su compra mas el descuento es de:" , p_realizar)