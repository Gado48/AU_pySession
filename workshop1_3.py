def diamond_alphabet_pattern(rows):

    start_char = ord("A")

    for i in range(1, rows + 1):

        for j in range(1, rows - i + 1):

            print(" ", end=" ")

        for j in range(1, 2 * i):

            print(chr(start_char + i - 1), end=" ")

        print()

    for i in range(rows - 1, 0, -1):

        for j in range(1, rows - i + 1):

            print(" ", end=" ")

        for j in range(1, 2 * i):

            print(chr(start_char + i - 1), end=" ")

        print()


diamond_alphabet_pattern(4)
