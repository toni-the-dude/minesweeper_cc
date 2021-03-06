import matrix
print("Welcome to Minesweeper! Uncover all the rectangles while avoiding the mines to win!")
matrix.generate_matrix()
matrix.generate_matrix_interface()
matrix.display_matrix()
while True: # First Input
    try:
        player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
        while player_i < 0 or player_i > 8:
            player_i = int(input("Try a number between 1 and 9.\n")) - 1
        player_j = int(input("Awaiting input for vertical axis(j):")) - 1
        while player_j < 0 or player_j > 8:
            player_j = int(input("Try a number between 1 and 9.\n")) - 1
        matrix.generate_mines(player_i, player_j)
        matrix.update_matrix(player_i, player_j)
        matrix.display_matrix()
        break
    except ValueError:
        print("Try a number.\n")
while True: # Game Loop + Input
    try:
        player_i = int(input("Awaiting input for horizontal axis(i):")) - 1
        while player_i < 0 or player_i > 8:
            player_i = int(input("Try a number between 1 and 9.\n")) - 1
        player_j = int(input("Awaiting input for vertical axis(j):")) - 1
        while player_j < 0 or player_j > 8:
            player_j = int(input("Try a number between 1 and 9.\n")) - 1
        if  matrix.space_is_available(player_i, player_j) == True:
            matrix.update_matrix(player_i, player_j)
            matrix.display_matrix()
            if matrix.matrix_ui[player_i][player_j] == '*':
                print("GAME OVER")
                matrix.reveal_matrix()
                break
            print(matrix.counter, "spaces revealed.")
            if matrix.counter >= 72:
                print("YOU WIN")
                matrix.reveal_matrix()
                break
        else: print("Position already revealed.")
    except ValueError:
        print("Try a number.\n")
