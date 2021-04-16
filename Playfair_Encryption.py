# Playfair Encryption
# Caden Johnson - CNA 438
# This program will allow the user to encrypt (and possibly decrypt)
# plaintext via Playfair Encryption and a keyword

from string import ascii_lowercase

def getmatrix():
    keyword = input("What is the keyword? : ").lower()
    matrix = ""
    for i in keyword:
        if i not in matrix:
            matrix += i
    for c in ascii_lowercase:
        if c == "i" or c == "j":
            if "i" not in matrix and "j" not in matrix:
                matrix += "i"
        else:
            if c not in matrix:
                matrix += c
    print(matrix)
    return matrix



def alternate(column, first, second):
    cipher1 = ""
    cipher2 = ""
    if column.index(first) == 4:
        cipher1 = column[0]
    else:
        cipher1 = column[column.index(first)+1]
        
    if column.index(second) == 4:
        cipher2 = column[0]
    else:
        cipher2 = column[column.index(second)+1]
    return cipher1, cipher2


def alternate2(columns, first, second, row): ##########error with up/down matrix
    cipher1 = ""
    cipher2 = ""
    temp = 0
    if first in columns[4]:
        cipher1 = columns[0][row]
    else:
        for i in columns:
            if first in i:
                cipher1 = columns[columns.index(i)+1][row]
    if second in columns[4]:
        cipher2 = columns[0][row]
    else:
        for j in columns:
            if second in i:
                cipher2 = columns[columns.index(j)+1][row]
    return cipher1, cipher2


def encrypt():
    temp = input("Enter the plain text : ").lower()
    temp.replace(" ", "")
    plaintext = ""
    ciphertext = ""
    for i in temp:
        if i in ascii_lowercase:
            plaintext += i
    matrix = ""
    matrix = getmatrix()
    m1 = matrix[0:5]
    m2 = matrix[5:10]
    m3 = matrix[10:15]
    m4 = matrix[15:20]
    m5 = matrix[20:25]
    columns = [m1, m2, m3, m4, m5]
    print(columns)
    place = 0
    for i in plaintext:
        place += 1
        if place % 2 != 0:
            if len(plaintext) == plaintext.index(i, (place - 1))+1:
                following = "x"
            else:
                following = plaintext[plaintext.index(i, (place - 1))+1]

            if i == following:
                following = "x"
                place -= 1############################## error with repititions

            for j in columns:
                if i in j:
                    column1 = j
                    row1 = j.index(i)
            for k in columns:
                if following in k:
                    column2 = k
                    row2 = k.index(following)

            if column1 == column2:
                cipher1, cipher2 = alternate(column1, i, following)
                ciphertext += cipher1
                ciphertext += cipher2
            elif row1 == row2:
                cipher1, cypher2 = alternate2(columns, i, following, row1)
                ciphertext += cipher1
                ciphertext += cipher2
            else:
                for k in columns:
                    if i in k:
                        ciphertext += k[row2]
                for j in columns:
                    if following in j:
                        ciphertext += j[row1]

    return ciphertext
            



def main():
    ciphertext = encrypt()
    print("Ciphertext:")
    print(ciphertext)
    


main()








