# Nicolas Plaza
"""
Un alumno desea saber cuál será su nota final en el curso de Introducción a la 
programación. Dicha nota se compone de los siguientes porcentajes: 55% del 
promedio de sus tres notas parciales, 30% de la nota del examen final y 15% de la 
nota de un trabajo fina
"""
print("ingresar notas como decimal por favor :)")
n_parciales = float(input("nota de el parcial: "))
e_final = float(input("nota del examen final: "))
t_grupal = float(input("Nota del trabajo grupal: "))
pon1 = n_parciales * 0.55
pon2 = e_final * 0.3
pon3 = t_grupal * 0.15
n_final = pon1 + pon2 + pon3
print("su nota de programación final es de" , round(n_final, 1))