# Podemos tener listas anidadas:

# Podríamos tener una lista con las calificaciones de cada estudiante

students = ["Seba", "Gonza", "Gaby"]
grades = [[5,6,4,5,6,7],[6,7,6,5,6,4],[6,6,5,6,7,7]]

# Se pide hacer un programa que imprima algo similar a:
# El estudiante Seba tiene promedio XX
# El estudiante Gonza tiene promedio YY
# El estudiante Gay tiene promedio ZZ
averages = []
for student_grades in grades:
  average = sum(student_grades)/len(student_grades)
  averages.append(average)

for num in range(len(students)):
  print("El estudiante", students[num], "tiene promedio",averages[num])