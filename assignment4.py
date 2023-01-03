import sys
with open(sys.argv[1]) as input_txt:
    matrix = []
    for lines in input_txt.read().splitlines():
        matrix.append(lines.split())
    for i in matrix:
        print(*i)
    print("Your score is 0")
###Weights and scoring
    d = {"B":9, "G":8,  "W":7,  "Y":6,  "R":5,  "P":4,  "O":3   ,"D":2   , "F":1,  "X":0,  " ":0}
    score = 0
### Getting input
    def get_input():
        global a,b,first_position
        coordinates = input("Please enter row and column with a space between them").split()

        try:
            b = int(coordinates[0])  ## raw
            a = int(coordinates[1])  ## column
            if 0 <= a <= len(matrix[0])-1 and 0 <= b <= len(matrix)-1:
                first_position = matrix[b][a]
            else:
                print("Please enter a valid size!")
                get_input()
                first_position = matrix[b][a]
        except ValueError:
            print("\n""Please enter a valid input")
            get_input()
            first_position = matrix[b][a]
        except IndexError:
            print("\n""Please enter a valid input")
            get_input()
            first_position = matrix[b][a]
        except RecursionError:
            print("\n""Please enter a valid input")
            get_input()
            first_position = matrix[b][a]




    def gravity():
        for raw in range(len(matrix)):
            for column in range(len(matrix[0])):
                if raw > 0:
                    if matrix[raw][column] == " ":
                        matrix[raw][column] = matrix[raw-1][column]
                        matrix[raw-1][column] = " "

### Check and remove same colors
    def remove(x,y):
        global score,a,b
        if x != len(matrix[0])-1:
            if first_position != " " and first_position != "X":
                if first_position == matrix[y][x + 1] or matrix[y][x - 1] or matrix[y + 1][x] or matrix[y - 1][x]:
                    try:
                        if first_position == matrix[y][x + 1]:  ##right
                            if matrix[y][x] != " ":
                                score += d[first_position]
                            matrix[y][x] = " "
                            score += d[matrix[y][x+1]]
                            matrix[y][x + 1] = " "
                            remove(x+1,y)
                    except IndexError:pass

                    try:
                        if first_position == matrix[y][abs(x - 1)]:  ## left
                            if matrix[y][x] != " ":
                                score += d[first_position]
                            matrix[y][x] = " "
                            score += d[matrix[y][x-1]]
                            matrix[y][x - 1] = " "
                            remove(x-1,y)
                    except IndexError:pass

                    try:
                        if first_position == matrix[y + 1][x]:  ##down
                            if matrix[y][x] != " ":
                                score += d[first_position]
                            matrix[y][x] = " "
                            score += d[matrix[y+1][x]]
                            matrix[y + 1][x] = " "
                            remove(x,y+1)
                    except IndexError:pass

                    try:
                        if first_position == matrix[(abs(y - 1))][x]:  ## up
                            if matrix[y][x] != " ":
                                score += d[first_position]
                            matrix[y][x] = " "
                            score += d[matrix[y-1][x]]
                            matrix[y - 1][x] = " "
                            remove(x,y-1)
                    except IndexError:pass



        elif x == len(matrix[0]) - 1 and y != len(matrix) - 1:
            if first_position == matrix[y][x - 1] or matrix[y + 1][x] or matrix[y - 1][x]:
                try:
                    if first_position == matrix[y][x - 1]:  ## left
                        if matrix[y][x] != " ":
                            score += d[first_position]
                        matrix[y][x] = " "
                        score += d[matrix[y][x-1]]
                        matrix[y][x - 1] = " "
                        remove(x-1,y)
                except IndexError:pass

                try:
                    if first_position == matrix[(abs(y - 1))][x]:  ## up
                        if matrix[y][x] != " ":
                            score += d[first_position]
                        matrix[y][x] = " "
                        score += d[matrix[y-1][x]]
                        matrix[y - 1][x] = " "
                        remove(x,y-1)
                except IndexError:pass

                try:
                    if first_position == matrix[y + 1][x]:  ##down
                        if matrix[y][x] != " ":
                            score += d[first_position]
                        matrix[y][x] = " "
                        score += d[matrix[y+1][x]]
                        matrix[y + 1][x] = " "
                        remove(x,y+1)
                except IndexError:pass

        elif x == len(matrix[0])-1 and y == len(matrix)-1: ##RIGHT BOTTOM CORNER
            if first_position == matrix[y][x - 1] or matrix[y - 1][x]:
                try:
                    if first_position == matrix[y][x - 1]:  ## left
                        if matrix[y][x] != " ":
                            score += d[first_position]
                        matrix[y][x] = " "
                        score += d[matrix[y][x-1]]
                        matrix[y][x - 1] = " "
                        remove(x-1,y)
                except IndexError:pass

                try:
                    if first_position == matrix[(abs(y - 1))][x]:  ## up
                        if matrix[y][x] != " ":
                            score += d[first_position]
                        matrix[y][x] = " "
                        score += d[matrix[y-1][x]]
                        matrix[y - 1][x] = " "
                        remove(x,y-1)
                except IndexError:pass

        try:
            if matrix[y][x] == "X":
                for i in range(len(matrix[y])): #left right
                    if matrix[y][i] == "X" and i != x:
                        for raw in range(len(matrix)):
                            score += (d[matrix[raw][i]])
                            matrix[raw][i] = " "
                    score += (d[matrix[y][i]])
                    matrix[y][i] = " "
                for j in range(len(matrix)): #up down
                    if matrix[j][x] == "X" and j != y:
                        for column in range(len(matrix[j])):
                            if column !=x:
                                score += (d[matrix[j][column]])
                                matrix[j][column] = " "
                    if j != y:
                        score += d[matrix[j][x]]
                    matrix[j][x] = " "
        except IndexError:
            pass
        try:
            for i in range(len(matrix[0])):
                for column in range(len(matrix[0])):
                    check = 0
                    for line in range(len(matrix)):
                        try:
                            if matrix[line][column] == " ":
                                check += 1
                                if check == len(matrix):
                                    for i in range(len(matrix[0])):
                                        del matrix[i][column]
                        except IndexError:pass
        except IndexError: pass

    def removing_column():
        for column in range(len(matrix[0])):
            check = 0
            for line in range(len(matrix)):
                try:
                    if matrix[line][column] == " ":
                        check += 1
                        if check == len(matrix) - 1:
                            for i in range(len(matrix[0])):
                                del matrix[i][column]
                except IndexError:pass

    def removing_empyt_lists():
        for line in range(len(matrix)):
            check = 0
            try:
                for column in range(len(matrix[0])):
                    if matrix[line][column] == " ":
                        check += 1
                        if check == len(matrix[0]):
                            matrix.remove(matrix[line])
            except IndexError:pass


    count_2 = 0
    def counter():
        global count_2
        count_2 = 0
        for raw in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[raw][column] == "B" or matrix[raw][column] == "G" or matrix[raw][column] == "W" or \
                        matrix[raw][column] == "Y" or matrix[raw][column] == "F" or matrix[raw][column] == "R" or \
                        matrix[raw][column] == "P" or matrix[raw][column] == "O" or matrix[raw][column] == "D":
                    count_2 += 1

    def game_over():
        count = 0
        global k
        for raw in range(len(matrix)):
            for column in range(len(matrix[0])):
                if len(matrix) != 1:
                    try:
                        if column != len(matrix[0])-1 and raw != len(matrix)-1:
                            if matrix[raw][column] != matrix[abs(raw-1)][column] and matrix[raw][column] != matrix[(raw+1)][column] and matrix[raw][column] != matrix[raw][column+1] and matrix[raw][column] != matrix[raw][abs(column-1)]:
                                count +=1
                        elif column == len(matrix[0])-1 and raw != len(matrix)-1:#köşe hariç sağ kenar
                            if matrix[raw][column] != matrix[raw-1][column] and matrix[raw][column] != matrix[raw+1][column] and matrix[raw][column] != matrix[raw][column-1]:
                                count +=1
                        elif column != len(matrix[0])-1 and raw == len(matrix)-1: #köşe hariç alt kenar
                            if matrix[raw][column] != matrix[abs(raw-1)][column] and matrix[raw][column] != matrix[raw][column+1] and matrix[raw][column] != matrix[raw][abs(column-1)]:
                                count +=1
                        elif column == len(matrix[0])-1 and raw == len(matrix)-1: #sağ alt köşe
                            if matrix[raw][column] != matrix[abs(raw-1)][column] and matrix[raw][column] != matrix[raw][abs(column-1)]:
                                count +=1
                    except IndexError:pass
                if len(matrix) == 1:
                    try:
                        if column == len(matrix[0])-1:
                            if matrix[raw][column] != matrix[raw][column-1]:
                                count +=1
                        else:
                            if matrix[raw][column] != matrix[raw][column+1] and matrix[raw][column] != matrix[raw][abs(column-1)]:
                                count += 1
                    except IndexError: pass
                if len(matrix) == 1 and len(matrix[0]) == 1 and matrix[0][0] != "X":
                    print("\n")
                    print("---GAME OVER---")
                    k = 0
        if len(matrix) == 1 and len(matrix[0]) == 0:
            print("\n")
            print("---GAME OVER---")
            k = 0

        try:
            if count == count_2 and "X" not in matrix[raw][column]:
                print("\n")
                print("---GAME OVER---")
                k = 0
        except UnboundLocalError: pass


    def print_matrix():
        print("\n")
        for i in matrix:
            print(*i)


    k = 1
    def game_starts():
         while k == 1:
            get_input()
            remove(a,b)
            try:
                for i in range(len(matrix)):
                    gravity()
            except IndexError: pass
            try:
                for i in range(len(matrix)):
                    removing_empyt_lists()
            except IndexError:pass
            print_matrix()
            print("\n")
            print("Your score is: {}".format(score))
            counter()
            game_over()
    game_starts()