import time
import os
os.system('cls')
# Eperiment for loop in cronometrare
start: float = time.time()
print(f"Startul este de: {start} secunde\n")
sum: int = 0
for _ in range(1_000_000_0):
    sum += 1
end: float = time.time()
print(f"End-ul este de: {end} secunde\n\nAm ajuns cu sum la: {sum} in timp de {round(end - start, 2)} secunde\n")
# os.system("shutdown/r")