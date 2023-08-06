#10. Write a program to Multiply Two matrices

rows1 = int(input("Enter number of rows  for the first matrix :: "))
cols1 = int(input("Enter number of cols for the first matrix :: "))

rows2 = int(input("Enter number of rows  for the second matrix :: "))
cols2 = int(input("Enter number of cols for the second matrix :: "))

if cols1 != rows2:
    print("Matrix Multiplication is not possible")
else:
    matrix1 = []
    matrix2 = []
    res_matix = []

    print("Enter elements of first matrix :: ")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            element = int(input(f"Eneter elemnts at position ({i+1},{j+1}) ::"))
            row.append(element)
        matrix1.append(row)

    print("Enter elements of second matrix :: ")
    for i in range(rows2):
        row = []
        for j in range(cols2):
            element = int(input(f"Eneter elemnts at position ({i+1},{j+1}) ::"))
            row.append(element)
        matrix2.append(row)

    for i in range(rows1):
        row = []
        for j in range(cols2):
            element = 0
            for k in range(cols1):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        res_matix.append(row)

    print("Resultant matrix after multiplication :: ")
    for row in res_matix:
        print(row)