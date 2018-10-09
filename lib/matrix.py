#matrix.py

def matrix_add(order):
    alpha = order*order
    elements1 = []
    elements2 = []
    add = []
    for i in range(0, alpha):
        elements1.append([])
        elements2.append([])
        add.append([])
    print("Enter elements in first matrix...\n")
    for i in range(0, alpha):
        elements1[i] = int(input())
    print("Enter elements in second matrix...\n")
    for i in range(0, alpha):
        elements2[i] = int(input())
    for i in range(0, alpha):
        add[i] = elements1[i] + elements2[i]
        #print(add[i], end = ' ')
    print(add)

#matrix_add(3)

def matrix_subtract(order):
    alpha = order*order
    elements1 = []
    elements2 = []
    add = []
    for i in range(0, alpha):
        elements1.append([])
        elements2.append([])
        add.append([])
    print("Enter elements in first matrix...\n")
    for i in range(0, alpha):
        elements1[i] = int(input())
    print("Enter elements in second matrix...\n")
    for i in range(0, alpha):
        elements2[i] = int(input())
    for i in range(0, alpha):
        add[i] = elements1[i] - elements2[i]
        #print(add[i], end = ' ')
    print(add)

#matrix_subtract(2)

