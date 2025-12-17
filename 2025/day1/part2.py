count = 0
currentNumber = 50


def main():
    with open("input.txt") as file:
        for line in file:
            rotate(line.strip())

    print(count)


def rotate(line: str):
    global count, currentNumber

    direction = line[0]
    amount = int(line[1:])

    if direction == "R":
        first_hit = (100 - currentNumber) % 100
    else:
        first_hit = currentNumber % 100

    if first_hit == 0:
        first_hit = 100

    if first_hit <= amount:
        count += 1 + (amount - first_hit) // 100

    if direction == "R":
        currentNumber = (currentNumber + amount) % 100
    else:  # "L"
        currentNumber = (currentNumber - amount) % 100


if __name__ == "__main__":
    main()
