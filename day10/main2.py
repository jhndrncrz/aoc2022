from typing import Any


def parse_line(line: str) -> tuple[str, Any]:
    command: list[Any] = line.strip().split()
    if len(command) == 2:
        command[1] = int(command[1])
    else:
        command.append(None)
    return tuple(command)


def run_cycle(cycle: int, x: int, line: str, screen: list[int]) -> tuple[Any, ...]:
    command = parse_line(line)
    print(f"Cycle {cycle}: x = {x}")
    cycle += 1
    if (cycle - 1) % 40 in range(x - 1, x + 2):
        screen[(cycle - 1)] += 1

    if command[0] == "noop":
        pass

    elif command[0] == "addx":
        x += command[1]
        print(f"Cycle {cycle}: x = {x}")
        cycle += 1
        if (cycle - 1) % 40 in range(x - 1, x + 2):
            screen[(cycle - 1)] += 1

    return cycle, x, screen


def main():
    cycle: int = 1
    x: int = 1
    screen: list[int] = [0] * 240
    with open("input.txt") as file:
        while cycle <= 240:
            line = file.readline()
            if not line:
                break
            cycle, x, screen = run_cycle(cycle, x, line, screen)

    screen_new = "".join([str(i) for i in screen])

    screen_new = screen_new.replace("0", ".").replace("1", "#")

    print(screen_new[0:40])
    print(screen_new[40:80])
    print(screen_new[80:120])
    print(screen_new[120:160])
    print(screen_new[160:200])
    print(screen_new[200:240])


if __name__ == "__main__":
    main()
