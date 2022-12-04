def topriority(item):
    if item.isupper():
        return ord(item) - 38
    if item.islower():
        return ord(item) - 96

def main():
    common_items = []
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            items_per_comp = len(line)//2
            first_comp = line[:items_per_comp]
            second_comp = line[items_per_comp:]
            for i in first_comp:
                if i in second_comp:
                    common_items.append(i)
                    break
    common_items = [topriority(i) for i in common_items]
    print(sum(common_items))

            

            

if __name__ == "__main__":
    main()
