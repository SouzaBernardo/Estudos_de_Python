from time import sleep


def main():
    v = int(input('valor: '))
    for v in range(0, v):
        print('#', end='')
        sleep(0.1)


if __name__ == "__main__":
    main()
