from math import*

hitrost = input("hitros m/s ")
hitrostfloat = float(hitrost)


kot = input("kot ")
kotfloat = float(kot)
kotradian = radians(kotfloat)


razdalja = (pow(hitrostfloat, 2) * sin(2 * kotradian)) / 10
print("iztrelek bo letel ", razdalja, "m")
