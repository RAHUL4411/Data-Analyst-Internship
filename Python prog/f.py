file = open('sample1.txt', 'r')
content=file.read()

file.close()

file2 = open('sample2.txt', 'w')
file2.write(content)
print(content)
file2.close()