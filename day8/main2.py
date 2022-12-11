def parse_line(line: str) -> list[int]:
    return [int(char) for char in line]


def is_visible(grid: list[list[int]], r: int, c: int) -> bool:
    """
    Checks if tree is visible by comparing it to the edges and the height of the trees with the same column and row
    """
    if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
        return True

    visibility = [True] * 4

    ## Check visibility from top
    for i in range(0, r):
        if grid[r][c] <= grid[i][c]:
            visibility[0] = False

    ## Check visibility from bottom, iterate on rows, fix column
    for i in range(r + 1, len(grid)):
        if grid[r][c] <= grid[i][c]:
            visibility[1] = False

    ## Check visibility from left, iterate on columns, fix row
    for i in range(0, c):
        if grid[r][c] <= grid[r][i]:
            visibility[2] = False

    ## Check visibility from right, iterate on columns, fix row
    for i in range(c + 1, len(grid[r])):
        if grid[r][c] <= grid[r][i]:
            visibility[3] = False

    return any(visibility)


def main():
    with open("input.txt") as file:
        grid: list[list[int]] = []
        for line in file:
            line = line.strip()
            grid.append(parse_line(line))
    print(grid)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_visible(grid, i, j):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
