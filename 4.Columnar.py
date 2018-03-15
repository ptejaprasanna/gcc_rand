import itertools
f = open('blackhat4.txt', 'r')
etext = f.read()
text = ""
f1 = open('quad.txt', 'r')
common_words = f1.read()
common_words = common_words.splitlines()
print(common_words)
high = 0
count2, total = 0,0
temp_ = ""
temp1 = ""
etext_list = list(etext)
temp_list = []
"""
for i in range(75):
    text += etext[i]
    text += "\n"
text_temp = text.splitlines()
for j in range(1,8):
    if j < 4:
        for i in range(75):
            text_temp[i] += (etext[(75*j) + i])
    if j == 4:
        for i in range(74):
            text_temp[i] += (etext[(75*j) + i])
    if j > 4:
        for i in range(74):
            text_temp[i] += (etext[(74*j + i)])

text_temp = "\n".join(text_temp)
print(text_temp)
"""
lst = list(itertools.product([0, 1], repeat=8))
list2 = []
count3 = 0
okay = 1
for i in range(len(lst)):
    count3 = lst[i].count(okay)
    if count3 == 4:
        list2.append((lst[i]))
print (list2)
x_pos = []
x_pos_ = []
temp = ""
for i in range(len(list2)):
    for a in list2[i]:
        x_pos.append(74 * a)
    
    for j in range(len(x_pos)):
        if x_pos[j] == 74:
            x_pos_.append(((j + 1) * x_pos[j]) + j)
    """
    for k in range(len(x_pos_)):
        if k < 1:
            temp = etext[0: (x_pos_[k] - 1)] + "x"
        if k > 0:
            temp += etext[(x_pos_[k-1] - k): (x_pos_[k]) - k] + "x"
        if k == 3 and (x_pos_[k] == 524 or x_pos_[k] == 449 or x_pos_[k] == 374 or x_pos_[k] == 299):
            temp += etext[(x_pos_[k]): ]
    """
    temp_list= []
    etext_list = list(etext)
    temp_list = etext_list
    for k in x_pos_:
        temp_list.insert(k, 'X')
    print(temp_list)
    
    temp = ''.join(temp_list)
    temp_list = []
    print(temp)
    print(len(temp))
    text = ""
    
    for i_ in range(75):
        text += temp[i_]
        text += "\n"
    text_temp = text.splitlines()
    for j_ in range(1,8):
        for i__ in range(75):
            text_temp[i__] += (temp[(75*j_) + i__])

    text_temp = "\n".join(text_temp)
    text2 = text_temp.splitlines()
    key = [(2,1,3,0,5,4,6,7)]
    for a in key: #itertools.permutations(range(8)):
        for b in range(75):
            for c in range(8):
                c = a[c]
                temp1 += text2[b][c]
            temp1 += "\n"
        for words1 in common_words:
            count2 = temp1.count(words1)
            total += count2
            count2 = 0
        if total > high:
            high = total
            temp_ = temp1
            a_ = a
            b_ = x_pos_

        total = 0
        temp1 = ""
    
    text2 = []
    print (text_temp)
    text_temp = ""
    temp = ""
    x_pos = []
    x_pos_ = []

print (high)
temp_ = "".join(line.strip() for line in temp_)
print (temp_)
print(a_)
print(b_)
wf = open('solved_blackhat4.txt', 'w')
wf.write(temp_)