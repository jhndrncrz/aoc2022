def is_unique(substring):
    return len(set(substring)) == 14


def main():
    with open("input.txt") as file:
        line = file.readline()
        for i in range(len(line)):
            if is_unique(line[i : i + 14]):
                print(line[i : i + 14], i + 14)
                break


if __name__ == "__main__":
    main()
