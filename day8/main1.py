def parse_line(line: str) -> list[int]:
    return [int(char) for char in line]

def is_visible(grid: list[list[int]], r:int, c:int) -> bool:
    """
    Checks if tree is visible by comparing it to the edges and the height of the trees with the same column and row
    """
    # Checks if it is an edge tree
    if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
        return True
    
    visibility = [True] * 4

    # Checks for visibility from top
    for i in range(len(grid[0:r])):
        if grid[r][c] < grid[i][c]:
            visibility[0] = False
    
    # Checks for visibility from bottom
    for i in range(len(grid[r:])):
        if grid[r][c] < grid[i][c]:
            visibility[1] = False

    # Checks for visibility from left
    for i in range(len(grid[r][:c])):
        if grid[r][c] < grid[r][i]:
            visibility[2] = False
    
    # Checks for visibility from right
    for i in range(len(grid[r][c:])):
        if grid[r][c] < grid[r][i]:
            visibility[3] = False

    #for tree in grid[x]:
    #    if grid[x][y] < tree:
    #        return False
    #for row in grid:
    #    if grid[x][y] < row[y]:
    #        return False
    return any(visibility)


def main():
    with open("input.txt") as file:
        grid:list[list[int]] = []
        for line in file:
            line = line.strip()
            grid.append(parse_line(line))
    print(grid)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_visible(grid, i, j):
                count += 1
                print(grid[i][j], is_visible(grid, i, j))
        print()
    print(count)

if __name__ == "__main__":
    main()