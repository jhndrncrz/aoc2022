def main():
    common_items = []
    group = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            group.append(line)
            if len(group) == 3:
                for item in group[0]:
                    if item in group[1] and item in group[2]:
                        common_items.append(item)
                        break
                group.clear()
            
    common_items = [topriority(i) for i in common_items]
    print(common_items)
    print(sum(common_items))         


def topriority(item):
    if item.isupper():
        return ord(item) - 38
    if item.islower():
        return ord(item) - 96


if __name__ == "__main__":
    main()

