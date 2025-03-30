"""
La precedencia de los operadores es el orden en que se ejecutan las operaciones en una expresión. Los paréntesis () permiten alterar este orden, ya que las operaciones dentro de los paréntesis se realizan primero.
"""
# Sin paréntesis: primero se ejecuta la multiplicación
result1 = 3 + 2 * 4  # 3 + 8 = 11

# Con paréntesis: la adición se ejecuta primero
result2 = (3 + 2) * 4  # 5 * 4 = 20

print(result1)  # Salida: 11
print(result2)  # Salida: 20

#vamos viendo las operaciones por orden de precedencia

print(2+2**3) #esto deberia generar 2**3 y desp sumarle 2 ->teniendo como resultado 10
print(2-2**3) #idem con menos ->-6 <- 2-8
print(2+2-3) #1 #no te precedencia entre + o -, realiza de izq a der(normal)
print(4<<1>>2) #primero lo multiplico una vez y luego lo dividio dos veces
print(4>>1<<2) #primero dividio por 2 y luego multiplico por 2 dos veces
#por ende vemos no tiene orden de precedencia entre >> y << 
print(2+4<<2) #ejecuta de izq a der porque el + tiene precedencia por sobre <<
print(2+(4<<2)) #cambio la precedencia

a={3,4,5}
print(4 in a and 3 in a and True)   #True