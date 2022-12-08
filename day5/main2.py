def parse_drawing(line):
    """
    Parses the drawing line by line by taking the character at index 1 and every 4th character from there of each line and joins them in a string
    """
    x = [line[i] for i in range(1, len(line), 4)]
    return x


def parse_moves(line):
    """
    Parse the input line by line leaving only integers
    """
    x = "".join([char if char.isnumeric() else " " for char in line])
    return [int(i) for i in x.split()]


def swap_drawing(drawing):
    """
    Takes the drawing and swaps it such that each subarray contains columns instead of rows
    """
    # Reverse since we need to convert from bottom-top to left-right
    drawing.reverse()

    # Create blank matrix with as many rows as the columns of the original
    result = [[] for _i in range(len(drawing[0]))]

    # Take each row in drawing except first row
    for i in range(1, len(drawing)):
        # Take each element in row and append it to its corresponding column
        for j in range(len(drawing[0])):
            # Remove blank spaces
            if drawing[i][j] != " ":
                result[j].append(drawing[i][j])

    return result


def mover(matrix, amount, origin, destination):
    matrix[destination] += matrix[origin][-amount:]
    for _i in range(amount):
        matrix[origin].pop()
    return matrix


def main():
    # Take drawing and swap its columns and rows for processing
    with open("drawing.txt") as file:
        drawing = [parse_drawing(line.strip("\n")) for line in file]
    drawing = swap_drawing(drawing)

    # Take moves from input.txt, apply it to drawing
    with open("input.txt") as file:
        for line in file:
            move = parse_moves(line.strip())
            drawing = mover(drawing, move[0], move[1] - 1, move[2] - 1)
            print(drawing)

    # Print last characters to get message
    for i in drawing:
        if len(i):
            print(i[-1], end="")
        else:
            pass


if __name__ == "__main__":
    main()
