def createGenerator(n) :
    for i in range(n):
        yield i+i*i*2

for elem in createGenerator(5):
    print(elem)