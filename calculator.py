# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Simple Calculator Demo")
    x, y = 10, 5
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")

if __name__ == "__main__":
    main()
