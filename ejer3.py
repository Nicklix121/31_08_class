# Authore: Nicolas Plaza
"""
Un profesor conoce la cantidad de hombres y mujeres del curso de Algoritmos, 
desea saber qué porcentaje de hombres y que porcentaje de mujeres hay en su 
grupo de estudiantes
"""
hombres = int(input(" Ingresar la cantidad de hombres: "))
mujeres = int(input(" Ingresar la cantidad de mujeres: "))
t_personas = hombres + mujeres 
p_hombres = (100 / t_personas) * hombres
p_mujeres = (100 / t_personas) * mujeres
print("hombres son", round(p_hombres), "%")
print("mujeres son",round(p_mujeres), "%")