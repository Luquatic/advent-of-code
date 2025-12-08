dial = list(range(100))
amountAtZero = 0
currentNumber = 50


def main():
    with open("input.txt") as file:
        for line in file:
            rotate(line)

    print(amountAtZero)


def rotate(line: str):
    global amountAtZero, currentNumber

    direction = line[0]
    amount = int(line[1:])

    match direction:
        case "L":
            currentNumber = (currentNumber - amount) % 100
        case "R":
            currentNumber = (currentNumber + amount) % 100

    if currentNumber == 0:
        amountAtZero += 1


if __name__ == "__main__":
    main()
