dataset = open('dataTest.txt')
lines = dataset.readlines()
x = 0
word = []
for line in lines:

    word.append(line.split(","))
    print(word[x])
    x+=1

    



