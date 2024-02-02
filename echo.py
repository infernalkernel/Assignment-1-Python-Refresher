def echo(text: str, repetitions: int = 3) -> str:
    returnString = ""
    for i in range(len(text)):
        if i < repetitions:
            returnString = returnString + (text[len(text) - (repetitions - i) :]) + "\n"
    return returnString + "."


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
