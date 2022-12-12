def main():
    elves = []
    with open("input.txt") as file:
        elf = 0
        for line in file:
            line = line.strip()
            if line:
                elf += int(line)
            else:
                elves.append(elf)
                print(elf, elves)
                elf = 0
                continue
    print(max(elves))


if __name__ == "__main__":
    main()
