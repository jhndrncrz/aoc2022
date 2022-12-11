def parse_line(line: str) -> list[int]:
    return [int(char) for char in line]

def is_visible(grid: list[list[int]], r:int, c:int) -> bool:
    """
    Checks if tree is visible by comparing it to the edges and the height of the trees with the same column and row
    """
    #print(f"{grid[r][c]} ({r},{c})", end = " ")
    # Checks if it is an edge tree
    if r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1:
        #print(f"is an edge tree")
        return True
    
    visibility = [True] * 4

    ## Check visibility from top, iterate on rows, fix column
    for i in range(0, r):
        if grid[r][c] <= grid[i][c]:
            #print(f"not visible from top since {grid[r][c]} <= {grid[i][c]}")
            visibility[0] = False
    
    ## Check visibility from bottom, iterate on rows, fix column
    for i in range(r+1, len(grid)):
        if grid[r][c] <= grid[i][c]:
            #print(f"not visible from bottom since {grid[r][c]} <= {grid[i][c]}")
            visibility[1] = False

    ## Check visibility from left, iterate on columns, fix row
    for i in range(0, c):
        if grid[r][c] <= grid[r][i]:
            #print(f"not visible from left since {grid[r][c]} <= {grid[r][i]}")
            visibility[2] = False
    
    ## Check visibility from right, iterate on columns, fix row
    for i in range(c+1, len(grid[r])):
        if grid[r][c] <= grid[r][i]:
            #print(f"not visible from right since {grid[r][c]} <= {grid[r][i]}")
            visibility[3] = False
    
    if any(visibility):
        visiblefrom = ""
        if visibility[0]:
            visiblefrom += "top "
        if visibility[1]:
            visiblefrom += "bottom "
        if visibility[2]:
            visiblefrom += "left "
        if visibility[3]:
            visiblefrom += "right"
        #print(f"is visible from {visiblefrom}")
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
    print(count)

if __name__ == "__main__":
    main()