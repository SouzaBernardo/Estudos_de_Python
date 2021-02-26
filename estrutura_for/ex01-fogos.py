from time import sleep
# contagem para fogos de artifício
x = 5
for fogos in range(1, 6):
    print(x)
    x -= 1
    sleep(1)
print('\033[31mFOGOOOO!\033[m')
