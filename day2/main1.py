def rps(player, enemy):
    moves = {
        "X": {
            "A": 3,
            "B": 0,
            "C": 6
        },
        "Y": {
            "A": 6,
            "B": 3,
            "C": 0
        },
        "Z": {
            "A": 0,
            "B": 6,
            "C": 3
        }
    }
    return moves[player][enemy]

def rps_bonus(player):
    moves = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return moves[player]

def main():
    score = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            score += rps(line[2], line[0]) + rps_bonus(line[2])
    print(score)


if __name__ == "__main__":
    main()
