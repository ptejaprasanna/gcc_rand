import itertools
f = open('blackhat2.txt', 'r')
with open('tri_bi.txt') as f1:
    common_words = f1.read().splitlines()
count = 0
total = 0
most = ""
etext = f.read()
etext2 = etext
length = len(etext)
c_text1=""
c_text=""
com_count = 0
com_total = 0
c_total = 0

s = list(etext)
for trav in range(length):
    if s[trav] == 'w':
        s[trav] = 'T'
    if s[trav] == 'z':
        s[trav] = 'H'
    if s[trav] == 'i':
        s[trav] = 'E'
    if s[trav] == 'h':
        s[trav] = 'A'
    if s[trav] == 'p':
        s[trav] = 'X'
    if s[trav] == 'n':
        s[trav] = 'P'
    if s[trav] == 'g':
        s[trav] = 'I'
    if s[trav] == 'k':
        s[trav] = 'S'
    if s[trav] == 'e':
        s[trav] = 'R'
    if s[trav] == 'l':
        s[trav] = 'N'
    if s[trav] == 'r':
        s[trav] = 'F'
    if s[trav] == 'c':
        s[trav] = 'L'
    if s[trav] == 'u':
        s[trav] = 'O'
    if s[trav] == 's':
        s[trav] = 'D'
    if s[trav] == 'q':
        s[trav] = 'W'
    if s[trav] == 't':
        s[trav] = 'U'
    if s[trav] == 'a':
        s[trav] = 'Y'
    if s[trav] == 'm':
        s[trav] = 'M'
    if s[trav] == 'y':
        s[trav] = 'V'
    if s[trav] == 'o':
        s[trav] = 'B'
    if s[trav] == 'v':
        s[trav] = 'C'
    if s[trav] == 'f':
        s[trav] = 'G'
    if s[trav] == 'd':
        s[trav] = 'K'
    if s[trav] == 'b':
        s[trav] = 'J'
    if s[trav] == 'j':
        s[trav] = 'Q'
    """
    if s[trav] == 'e':
        s[trav] = 'S'
    if s[trav] == 'k':
        s[trav] = 'N'
    if s[trav] == 'l':
        s[trav] = 'R'
    """
etext = ""
etext = "".join(s)
high_list = ['C', 'G', 'J', 'K', 'Q','Z'] #, 'D', 'C', 'U']
unknown_list = ['b', 'd', 'f', 'j', 'x', 'v']#'c', 'r', 'm', 't']

"""
                                            for g in unknown_list[6]:
                                                    for g_ in itertools.product(g, high_list):
                                                        if(fk[1] == g_[1] or g_[1] == e_[1] or g_[1] == d_[1] or g_[1] == c_[1] or g_[1] == b_[1] or g_[1] == a_[1]):
                                                            continue
                                                        temp_text12 = temp_text11
                                                        temp_text13 = temp_text12.replace(g, g_[1])
                                                        for h in unknown_list[7]:
                                                            for h_ in itertools.product(h, high_list):
                                                                if(fk[1] == h_[1] or h_[1] == e_[1] or h_[1] == d_[1] or h_[1] == c_[1] or h_[1] == b_[1] or h_[1] == a_[1] or h_[1] == g_[1]):
                                                                    continue
                                                                temp_text14 = temp_text13
                                                                temp_text15 = temp_text14.replace(h, h_[1])
                                                                for i in unknown_list[8]:
                                                                    for i_ in itertools.product(i, high_list):
                                                                        if(fk[1] == i_[1] or i_[1] == e_[1] or i_[1] == d_[1] or i_[1] == c_[1] or i_[1] == b_[1] or i_[1] == a_[1] or i_[1] == g_[1] or i_[1] == h_[1]):
                                                                            continue
                                                                        temp_text16 = temp_text15
                                                                        temp_text17 = temp_text16.replace(i, i_[1]
"""
    
                

"""
for trav in range(length)[::3]:
    temp = etext[trav] + etext[trav + 1] + etext[trav + 2]
    total = etext.count(temp)
    if total > 10:
        if(etext[trav] or etext[trav + 1] or etext[trav + 2] == 'i'):
            print (total)
            print (temp)
    total = 0

"""
"""
for trav in range(length)[::4]:
    temp = etext[trav] + etext[trav + 1] + etext[trav + 2] + etext[trav + 3]
    total = etext.count(temp)
    if total > 1:
        print(total)
        print(temp)
    total = 0
print (count, most)
"""
"""
for trav in range(length)[::4]:
    temp = etext[trav] + etext[trav + 1] + etext[trav + 2] + etext[trav + 3]
    total = etext.count(temp)
    if total > 5: #and total < 11:
        print(total)
        print(temp)
    total = 0
print (count, most)
"""

frequency={}
for ascii in range(ord('A'), ord('A')+26):
    frequency[chr(ascii)] = float(etext.count(chr(ascii)))/len(etext)
sum_freqs_squared = 0.0
for ltr in frequency:
    sum_freqs_squared += frequency[ltr]*frequency[ltr]
print(sum_freqs_squared)
"""
sred = sorted(frequency.items(), key=lambda value: value[1])
print(sred)
print(etext)
str = etext.replace("zi", "he")
str = etext.replace("wzhw", "that")
str = etext.replace("wzi", "the")
print(c_total)
print(c_text)
print(c_text1)
print(test1)
"""
etext = etext.lower()
print(etext)
wf = open('solved_blackhat2.txt', 'w')
wf.write(etext)

