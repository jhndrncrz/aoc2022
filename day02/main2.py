def rps(player, enemy):
    score = {
        "A": {"A": 3, "B": 0, "C": 6},
        "B": {"A": 6, "B": 3, "C": 0},
        "C": {"A": 0, "B": 6, "C": 3},
    }
    return score[player][enemy]


def rps_bonus(player):
    moves = {"A": 1, "B": 2, "C": 3}
    return moves[player]


def rps_playermove(enemy, result):
    decision = {
        "X": {"A": "C", "B": "A", "C": "B"},
        "Y": {"A": "A", "B": "B", "C": "C"},
        "Z": {"A": "B", "B": "C", "C": "A"},
    }
    return decision[result][enemy]


def main():
    score = 0
    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            play_move = rps_playermove(line[0], line[2])
            score += rps(play_move, line[0]) + rps_bonus(play_move)
    print(score)


if __name__ == "__main__":
    main()
