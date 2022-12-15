def is_touching(hx: int, hy: int, tx: int, ty: int) -> bool:
    return abs(hx - tx) <= 1 and abs(hy - ty) <= 1


def main():
    # initialize
    hx, hy = 0, 0
    tx, ty = 0, 0

    head_dir = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    tail_dests: list[tuple[int, int]] = []

    with open("input.txt") as file:
        for line in file:
            line = line.strip().split()
            for _ in range(int(line[1])):
                dhx, dhy = head_dir[line[0]]
                hx += dhx
                hy += dhy
                tail_dir = {
                    (hx - tx >= 2 and hy == ty): (1, 0),
                    (hy - ty >= 2 and hx == tx): (0, 1),
                    (hx - tx <= -2 and hy == ty): (-1, 0),
                    (hy - ty <= -2 and hx == tx): (0, -1),
                    (not is_touching(hx, hy, tx, ty) and hx > tx and hy > ty): (1, 1),
                    (not is_touching(hx, hy, tx, ty) and hx < tx and hy > ty): (-1, 1),
                    (not is_touching(hx, hy, tx, ty) and hx > tx and hy < ty): (1, -1),
                    (not is_touching(hx, hy, tx, ty) and hx < tx and hy < ty): (-1, -1),
                }
                state = is_touching(hx, hy, tx, ty)
                dtx, dty = tail_dir.get(True, (0, 0))
                tx += dtx
                ty += dty
                tail_dests.append((tx, ty))
                print(
                    f"Head: ({hx}, {hy}) -- Tail: ({tx}, {ty}) ---- (Touching: {state})"
                )
        print(f"Unique Positions: {len(set(tail_dests))}")


if __name__ == "__main__":
    main()
