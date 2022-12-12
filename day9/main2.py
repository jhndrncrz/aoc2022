def is_touching(hx: int, hy: int, tx: int, ty: int) -> bool:
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def motion(lx: int, ly: int, nx: int, ny: int) -> tuple[int, int]:
    n_dir = {
        (lx - nx >= 2 and ly == ny): (1, 0),
        (ly - ny >= 2 and lx == nx): (0, 1),
        (lx - nx <= -2 and ly == ny): (-1, 0),
        (ly - ny <= -2 and lx == nx): (0, -1),
        (not is_touching(lx, ly, nx, ny) and lx > nx and ly > ny): (1, 1),
        (not is_touching(lx, ly, nx, ny) and lx < nx and ly > ny): (-1, 1),
        (not is_touching(lx, ly, nx, ny) and lx > nx and ly < ny): (1, -1),
        (not is_touching(lx, ly, nx, ny) and lx < nx and ly < ny): (-1, -1),
    }
    dnx, dny = n_dir.get(True, (0, 0))
    nx += dnx
    ny += dny

    return (nx, ny)


def main():
    rope = {
        0: [0, 0],
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 0],
        8: [0, 0],
        9: [0, 0],
    }

    head_dir = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    tail_dests: list[tuple[int, int]] = []

    with open("input.txt") as file:
        for line in file:
            line = line.strip().split()
            for _ in range(int(line[1])):
                dhx, dhy = head_dir[line[0]]
                rope[0][0] += dhx
                rope[0][1] += dhy
                for i in range(len(rope) - 1):
                    rope[i + 1][0], rope[i + 1][1] = motion(
                        rope[i][0], rope[i][1], rope[i + 1][0], rope[i + 1][1]
                    )

                tail_dests.append((rope[9][0], rope[9][1]))
        print(f"Unique Positions: {len(set(tail_dests))}")


if __name__ == "__main__":
    main()
