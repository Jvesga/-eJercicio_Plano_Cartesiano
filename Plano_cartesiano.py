"""Programa para saber en que cuadrente del plano se ubica el punto dado"""

print("---------------------------------")
print("---Cuadrante del plano cartesiano")
print("---------------------------------")

# input
X=int(input(" Digite el valor de X: "))
Y=int(input(" Digite el valor de Y: "))
# processing
if((X > 0) and (Y > 0)):
    msj = "UNO";

elif((X < 0) and (Y > 0)):
    msj = "DOS";

elif((X < 0) and (Y < 0)):
    msj = "TRES";

elif((X > 0) and (Y < 0)):
    msj = "CUATRO";

else:
    msj = "Cero u Origen del Plano"

# output

print(" El punto se ubica en el cuadrante: " + msj)