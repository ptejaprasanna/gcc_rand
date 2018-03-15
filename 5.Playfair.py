import itertools
f = open('blackhat4.txt', 'r')
etext = f.read()
print(etext.upper())
com_total = 0
com_count = 0
c_total = 0
with open('quad.txt') as f1: 
    common_words = f1.read().splitlines()
count = 0
total = 0
dict = {}
list = []
dict_rev = {}
list_rev = []
m_dict = {}
frequency = {}

for ascii in range(ord('a'), ord('a')+26):
    frequency[chr(ascii)] = etext.count(chr(ascii))

sred1 = sorted(frequency.items(), key=lambda value: value[1])
import re
for i in range(len(etext)):
    if(i == len(etext) - 1):
        break
    temp = etext[i] + etext[i+1]
    count = etext.count(temp)
    
    if count > 1:
        if temp not in list:
            #print (temp)
            #print (count)
            dict.update({temp:count})
            list.append(temp)

for k in list:
    placebo = k[1] + k[0]
    print(placebo)
    count  = etext.count(placebo)
    if count > 1:
        if placebo not in list_rev:
            dict_rev.update({placebo:count})
            list_rev.append(placebo)
            for j in list:
                if (placebo[0] == j[1] and placebo[1] == j[0]):
                    m_dict.update({placebo:j})

sred_rev = sorted(dict_rev.items(), key = lambda value: value[1])
sred = sorted(dict.items(), key=lambda value: value[1])
print("First list")
print(sred)
print("reversed list")
print(sred_rev)
print("Merged list")
print(m_dict)
#print(list)
str = etext.replace('pf', 'TH')
str = str.replace('fp', 'HT')
#str = str.replace('cb', 'HE')
str = str.replace('vc', 'IN')
#str = str.replace('yp', 'ER')
str = str.replace('ta', 'AN')
str = str.replace('at', 'NA')
str = str.replace('tp', 'RE')
str = str.replace('dy', 'AT')
high_list = ["HE", "ER", "ON", "EN",  "ND", "TI", "ES"]
unknown_list = ["cb", "yp", "aw", "pc", "ap", "bp", "lp"]
for a in unknown_list[0]:
    for a_ in itertools.product(a, high_list):
        #f_ = open('blackhat5.txt', 'r')
        temp_text = str
        temp_text1 = temp_text.replace(a_[0], a_[1])
        for b in unknown_list[1]:
            for b_ in itertools.product(b, high_list):
                if(b_[1] == a_[1]):
                    continue
                temp_text2 = temp_text1
                temp_text3 = temp_text2.replace(b, b_[1])
                for c in unknown_list[2]:
                    for c_ in itertools.product(c, high_list):
                        if(c_[1] == b_[1] or a_[1] == c_[1]):
                            continue
                        temp_text4 = temp_text3
                        temp_text5 = temp_text4.replace(c, c_[1])
                        for d in unknown_list[3]:
                            for d_ in itertools.product(d, high_list):
                                if(c_[1] == d_[1] or d_[1]==a_[1] or d_[1] == b_[1]):
                                    continue
                                temp_text6 = temp_text5
                                temp_text7 = temp_text6.replace(d, d_[1])
                                for e in unknown_list[4]:
                                    for e_ in itertools.product(e, high_list):
                                        if(e_[1] == d_[1] or e_[1] == c_[1] or e_[1] == b_[1] or e_[1] == a_[1]):
                                            continue
                                        temp_text8 = temp_text7
                                        temp_text9 = temp_text8.replace(e, e_[1])
                                        for f in unknown_list[5]:
                                            for fk in itertools.product(f, high_list):
                                                if(fk[1] == e_[1] or fk[1] == d_[1] or fk[1] == c_[1] or fk[1] == b_[1] or fk[1] == a_[1]):
                                                    continue
                                                temp_text10 = temp_text9
                                                temp_text11 = temp_text10.replace(f, fk[1])
                                            for g in unknown_list[6]:
                                                for g_ in itertools.product(g, high_list):
                                                    if(fk[1] == g_[1] or g_[1] == e_[1] or g_[1] == d_[1] or g_[1] == c_[1] or g_[1] == b_[1] or g_[1] == a_[1]):
                                                        continue
                                                    temp_text12 = temp_text11
                                                    temp_text13 = temp_text12.replace(g, g_[1])
                                                
                                                test = temp_text13.lower()
                          
                                                for words in common_words:
                                                    com_count = test.count(words)
                                                    com_total += com_count
                                                    if com_total > c_total:
                                                        c_total = com_total
                                                        c_text = a_[0] + b_[0]+c_[0]+d_[0]+e_[0]+fk[0] + g_[0]
                                                        c_text1 = a_[1] + b_[1] + c_[1] +d_[1] + e_[1] + fk[1] + g_[1]
                                                        test1 = temp_text13
                                                com_count = 0
                                                com_total = 0
                                                                       

print (test1)
print(str)
print(sred1)
