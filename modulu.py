salary = int (input ("enter namber"))
regular_hours = 180
night_bonus = 1.75
night_hours = 17
neto = 0.8
month_regular = salary * regular_hours
month_night = night_bonus * salary * night_hours
month_salary = month_regular + month_night
month_neto = month_salary * neto
tzdaka = month_neto / 10
print (tzdaka)