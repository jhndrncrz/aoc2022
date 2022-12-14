from typing import Any


def parse_line(line: str) -> tuple[str, Any]:
    command: list[Any] = line.strip().split()
    if len(command) == 2:
        command[1] = int(command[1])
    else:
        command.append(None)
    return tuple(command)


def run_cycle(cycle: int, x: int, line: str, milestones: list[int]) -> tuple[Any, ...]:
    command = parse_line(line)
    if command[0] == "noop":
        cycle += 1
        print(f"Cycle {cycle}: x = {x}")
        if check_cycle(cycle):
            milestones.append(signal_strength(x, cycle))
    elif command[0] == "addx":
        cycle += 1
        print(f"Cycle {cycle}: x = {x}")
        if check_cycle(cycle):
            milestones.append(signal_strength(x, cycle))
        x += command[1]
        cycle += 1
        print(f"Cycle {cycle}: x = {x}")
        if check_cycle(cycle):
            milestones.append(signal_strength(x, cycle))
    return cycle, x, milestones


def check_cycle(cycle: int) -> bool:
    return cycle % 40 == 20


def signal_strength(x: int, cycle: int) -> int:
    return x * cycle


def main():
    cycle: int = 1
    x: int = 1
    milestones: list[int] = []
    with open("input.txt") as file:
        while cycle <= 220:
            line = file.readline()
            if not line:
                break
            cycle, x, milestones = run_cycle(cycle, x, line, milestones)
    print(milestones)
    print(sum(milestones))


if __name__ == "__main__":
    main()
