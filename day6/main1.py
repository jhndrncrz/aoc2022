def is_unique(quad):
    return len(set(quad)) == 4


def main():
    with open("input.txt") as file:
        line = file.readline()
        for i in range(len(line)):
            if is_unique(line[i : i + 4]):
                print(line[i : i + 4], i + 4)
                break


if __name__ == "__main__":
    main()
