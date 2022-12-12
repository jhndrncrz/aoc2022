def get_size(listx):
    return listx[1]

def main():
    current_dir: list[str] = []
    filesystem: dict[tuple[str], int] = {}
    with open("input.txt") as file:
        for line in file:
            line = line.strip().split()
            if line[0] == "$":
                if line[1] == "cd" and line[2] != "..":
                    current_dir.append(line[2])
                    filesystem[tuple(current_dir)] = 0
                elif line[1] == "cd" and line[2] == "..":
                    current_dir.pop()
                elif line[1] == "ls":
                    continue
            elif line[0].isalpha():
                continue
            elif line[0].isnumeric():
                for i in range(1, len(current_dir)+1):
                    filesystem[tuple(current_dir)[0:i]] += int(line[0])
    print(f"Space occupied: {filesystem[('/',)]}")
    print(f"Space available: {70000000 - filesystem[('/',)]}")
    print(f"Additional space needed: {30000000 - (70000000 - filesystem[('/',)])}")
    enough = []
    for key, value in filesystem.items():
        if value >= 30000000 - (70000000 - filesystem[('/',)]):
            enough.append([key, value])
    
    
    enough.sort(key = get_size)
    print(enough)
    
    print(filesystem)
    


if __name__ == "__main__":
    main()
