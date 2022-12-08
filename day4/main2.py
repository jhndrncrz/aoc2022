def parse_line(line):
    """
    Takes line and outputs a list of integers
    """
    # Replaces all non-numeric characters to spaces by list comprehension and joins it to a string
    x = "".join([char if char.isnumeric() else " " for char in line])

    # Splits the string by spaces to list and converts all to integers
    return list(map(int, x.split()))


def sort_range(arr):
    """
    Takes list of integers and sorts them according to the size of the range they belong in
    """
    if arr[0] > arr[2]:
        return arr[2:] + arr[:2]
    else:
        return arr


def is_in(arr):
    """
    Takes an array and checks if the smaller one is a subset of the other
    """
    return arr[0] >= arr[2] and arr[1] <= arr[3]


def is_intersect(arr):
    """
    Takes an array and checks if the two subarrays intersect
    """
    return arr[0] <= arr[2] <= arr[1]


def main():
    count = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            arr = sort_range(parse_line(line))
            if is_intersect(arr):
                count += 1
    print(count)


if __name__ == "__main__":
    main()
