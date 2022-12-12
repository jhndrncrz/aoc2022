def parse_line(line: str) -> list[int]:
    return [int(char) for char in line]


def get_scenic_score(grid: list[list[int]], r: int, c: int) -> int:
    """
    Counts how many trees can the tree at r,c see until it gets blocked and multiplies them together
    """

    visibility = [0] * 4

    ## Check visibility from top
    for i in range(r - 1, -1, -1):
        visibility[0] += 1
        if grid[r][c] <= grid[i][c]:
            break

    ## Check visibility from bottom
    for i in range(r + 1, len(grid)):
        visibility[1] += 1
        if grid[r][c] <= grid[i][c]:
            break

    ## Check visibility from left
    for i in range(c - 1, -1, -1):
        visibility[2] += 1
        if grid[r][c] <= grid[r][i]:
            break

    ## Check visibility from right
    for i in range(c + 1, len(grid[r])):
        visibility[3] += 1
        if grid[r][c] <= grid[r][i]:
            break

    score: int = 1

    for s in visibility:
        score *= s

    return score


def main():
    with open("input.txt") as file:
        grid: list[list[int]] = []
        for line in file:
            line = line.strip()
            grid.append(parse_line(line))

    print(get_scenic_score(grid, 1, 2))
    print(get_scenic_score(grid, 3, 2))

    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if get_scenic_score(grid, i, j) > max_score:
                max_score = get_scenic_score(grid, i, j)
    print(max_score)


if __name__ == "__main__":
    main()
