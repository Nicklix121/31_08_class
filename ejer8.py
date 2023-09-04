# Authores Nicolas Plaza
"""
Un estudiante desea saber cuál será su promedio general en los tres cursos más
difciles que cursa y cuál será el promedio que obtendrá en cada una de ellas
"""
print("ingresar notas según que se le indique")
print("introducir datos de matematica")
e = float(input("Ingresar nota del examen: "))
t_m1 = float(input("Ingresar nota del primer trabajo: "))
t_m2 = float(input("Ingresar nota del primer trabajo: "))
t_m3 = float(input("Ingresar nota del primer trabajo: "))
print("Introducir datos de fisica")
e1 = float(input("Ingresar nota del examen: "))
t_f1 = float(input("Ingresar nota del primer trabajo: "))
t_f2 = float(input("Ingresar nota del primer trabajo: "))
print("Introducir datos de progración")
e2 = float(input("Ingresar nota del examen: "))
t_p1 = float(input("Ingresar nota del primer trabajo: "))
t_p2 = float(input("Ingresar nota del primer trabajo: "))
t_p3 = float(input("Ingresar nota del primer trabajo: "))
o_m = (t_m1 + t_m2 + t_m3) / 3  
o1_m = (e * 0.9) + (o_m * 0.1)   # aquiva el resulta de examen + tarea de m
o_f =((t_f1 + t_f2) / 2)         # aquiva el resulta de examen + tarea de f
o1_f = (e1 * 0.8) + (o_f * 0.2)
o_p =((t_p1 + t_p2 + t_p3) / 3)  # aquiva el resulta de examen + tarea de p
o1_p = (e2 * 0.85) + (o_p * 0.15)
h_fi = ((o1_f * 0.3) + (o1_m * 0.3) + (o1_p * 0.4)) # aqui va el final de las 3 :)
print("El promedio que saco en matematica es de:" , round(o1_m , 1))
print("El promidio que saco en fisica es de: " , round(o1_f , 1))
print("El promedio que saco en programación es de: " , round(o1_p , 1))
print("Y por ultimo el promedio oficial, que seria de:" , round(h_fi , 1))
#de aqui para abajo es para ver los colores, no tiene mucha importancia
print("\033[4;35m"+"El promedio que saco en matematica es de:" , round(o1_m , 1))
print("\033[4;35m"+"El promidio que saco en fisica es de:" ,  round(o1_f , 1))
print("\033[4;35m"+"El promedio que saco en programación es de:" , round(o1_p , 1))
print("\033[4;35m"+"Y por ultimo el promedio oficial, que seria de:" , round(h_fi , 1))