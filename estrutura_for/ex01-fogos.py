from time import sleep
# contagem para fogos de artifício
x = 10
for fogos in range(1, 11):
    print(x)
    x -= 1
    sleep(1)
print('\033[31mFOGOOOO!\033[m')
