#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in matrix:
        count = 1
        for j in i:
            if count < len(i):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
            count += 1
