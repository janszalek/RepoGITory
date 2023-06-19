from helper import say_hello
from calculator import add

def main():
    say_hello("John")
    result = add(5, 3)
    print("Wynik dodawania:", result)

if __name__ == "__main__":
    main()