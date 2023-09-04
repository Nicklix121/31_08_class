# Authore: Nicolas Plaza 
"""
En un hospital existen tres áreas: Ginecología, Pediatría, Traumatología. El 
presupuesto anual del hospital se reparte conforme a la siguiente manera: 
Ginecología un 50%, Traumatología un 20% y Pediatría un 30%. Obtener la can=dad 
de dinero que recibirá cada área, para cualquier monto presupuestado.
"""
p = int(input("ingresar presupuesto: "))
p1 = p * 0.5
p2 = p * 0.2
p3 = p * 0.3
print("El area de ginecologia: " , round(p1))
print("El area de traumatogia: " , round(p2))
print("El area de pediatria: " , round(p3))