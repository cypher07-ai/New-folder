n = int(input())
readings = []

for i in range(n):
    readings.append(int(input()))

readings = tuple(readings)

even_readings = readings[0::2]
odd_readings = readings[1::2]

print("Even readings:", even_readings)
print("Odd readings:", odd_readings)