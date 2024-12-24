class Calculator:
    def add(self, a, b):
        return a + b


def main():
    calc = Calculator()
    result = calc.add(5, 3)
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
