def num_letters(num_rows,num_columns):
    return (num_rows * 2) + (num_columns-2)*2
assert num_letters(3, 4) == 10
print("Checking assertions.")
assert num_letters(13,4) == 30
assert num_letters(4,4) == 12
assert num_letters(6,4) == 16
assert num_letters(6,7) == 22
import numpy as np
#loop1
data = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] 
rows, columns = data.shape
for r in range(rows):
    for c in range(columns):
        word = data[r,c].strip()
        if word != "":
            words.append(word)
print(words) 
assert len(words) == num_letters(rows, columns)
#loop2
data = np.loadtxt("loop2.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] 
rows, columns = data.shape
for r in range(rows):
    for c in range(columns):
        word = data[r,c].strip()
        if word != "":
            words.append(word)
print(words) 
assert len(words) == num_letters(rows, columns)
#loop3
data = np.loadtxt("loop3.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] 
rows, columns = data.shape
for r in range(rows):
    for c in range(columns):
        word = data[r,c].strip()
        if word != "":
            words.append(word)
print(words) 
assert len(words) == num_letters(rows, columns)
#loop4
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] 
rows, columns = data.shape
for r in range(rows):
    for c in range(columns):
        word = data[r,c].strip()
        if word != "":
            words.append(word)
print(words) 
assert len(words) == num_letters(rows, columns)
#loop1
data = np.loadtxt("loop1.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] 
rows, columns = data.shape
c = 0
r=0
while c < columns:
    word1 = data[0,c]
    word2 = data[0,c+1]
    pair = word1 + word2
    if word != "":
        words.append(pair)
    c = c+2
r=1
c=0
while r < rows:
    word1 = data[r,columns-1]
    word2 = data[r+1,columns-1]
    pair = word1 + word2
    if word!= "":
        words.append(pair)
    r = r+2 
r=rows-1
c=columns-1
while c < columns:
    word1 = data[r,c-1]
    word2 = data[r,c-2]
    pair = word1 + word2
    if word != "":
        words.append(pair)
    c = c+2
r=rows-1
c=0
while r > 0:
    word1 = data[r,c]
    word2 = data[r-1,c]
    pair = word1 + word2
    if word != "":
        words.append(pair)
    r = r-2
print(words)
