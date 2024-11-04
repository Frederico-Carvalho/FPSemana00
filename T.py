'''''
#Tuple

porta = (1, 2)
x, y = porta
print(x)

# Se puser um asterisco numa variavel essa variavel ira ficar com os numeros restantes, logo não é necessario 
# ter a quatidade de numeros = a quantidade de Variaveis 

porta = (1, 2, 4, 5, 7, 9)
x, *y, z = porta
print(x)
print(y)
print(z)
'''
room_description = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["K","L","M","N","O"],
    ["P","Q","R","S","T"],
    ["U","V","W","X","Y"]
]

room_exits = [
    [ (True, False, True, False), (False, True, False, False), (False, True, True, True), (False, True, True, True), (False, True, True, True)],
    [ (True, False, True, False), (False, True, True, False), (True, True, True, True), (True, False, False, True), (True, False, True, False)],
    [ (True, False, True, False), (True, False, False, False), (True, False, True, False), (False, True, False, False), (True, False, True, True)],
    [ (True, False, True, False), (False, True, True, False), (True, True, False, True), (False, True, False, True), (True, False, True, False)],
    [ (True, True, False, False), (True, False, False, True), (False, False, False, False), (True, False, False, False), (True, False, False, False)]
]

position = (2, 2)  


while (True):

    x,y = position
    Description = room_description[y][x]
    print(position, ":", Description)

    print("What now?")
    command = input()

    if (command == "north"):
        print("You have moved north")
        y -= 1
    elif (command == "south"):
        print("You have moved south")
        y += 1
    elif (command == "east"):
        print("You have moved east")
        x += 1
    elif (command == "west"):
        print("You have moved west")
        x -= 1
    elif (command == "leave"):
        break 
    else :
        print("I dont understand " + command + "!")

    position = (x, y) 