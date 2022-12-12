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
    top3 = 0
    top3 += max(elves)
    elves.remove(max(elves))
    top3 += max(elves)
    elves.remove(max(elves))
    top3 += max(elves)
    elves.remove(max(elves))
    print(top3)


if __name__ == "__main__":
    main()
