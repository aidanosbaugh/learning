def main():
    print_square(x)

def print_square(size):
    for _ in range(size):
        print("#" * size, end="\n")

x = int(input("Side Length?"))

main()


