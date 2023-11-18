numbers = open("numbers.txt", 'r')
answer = open("answer.txt", "w")

read = numbers.read()
answer.write(str(sum([int(x) for x in "".join(read.split())])))

answer.close()
numbers.close()
