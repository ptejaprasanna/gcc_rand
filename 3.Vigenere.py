normal_freqs = {'a': 0.080642499002080981, 'c': 0.026892340312538593, 'b': 0.015373768624831691, 'e': 0.12886234260657689, 'd': 0.043286671390026357, 'g': 0.019625534749730816, 'f': 0.024484713711692099, 'i': 0.06905550211598431, 'h': 0.060987267963718068, 'k': 0.0062521823678781188, 'j': 0.0011176940633901926, 'm': 0.025009719347800208, 'l': 0.041016761327711163, 'o': 0.073783151266212627, 'n': 0.069849754102356679, 'q': 0.0010648594165322703, 'p': 0.017031440203182008, 's': 0.063817324270355996, 'r': 0.06156572691936394, 'u': 0.027856851020401599, 't': 0.090246649949305979, 'w': 0.021192261444145363, 'v': 0.010257964235274787, 'y': 0.01806326249861108, 'x': 0.0016941732664605912, 'z': 0.0009695838238376564}
with open('1-1000.txt') as f:
    common_words = f.read().splitlines()

def shiftBy(c,n):
    return chr(((ord(c) - ord('a') + n) % 26) + ord('a'))

def getFreqs(text):
    frequency = {}
    for ascii in range(ord('a'), ord('z') + 1):
        frequency[chr(ascii)] = float (text.count(chr(ascii)))/len(text)
    return frequency

def getShift(text):
    freqs = getFreqs(text)
    keys = []
    for possible_key in range(0, 26):
        sum_f_sqr = 0.0
        for ltr in normal_freqs:
            caesar_guess = shiftBy(ltr, possible_key)
            sum_f_sqr += normal_freqs[ltr] * freqs[caesar_guess]
        if abs(sum_f_sqr - 0.065) < 0.005:
            keys.append(possible_key)
            #print possible_key
    #if (len(keys) > 1):
        #print("Many Possiblities", keys)
    #print(keys)
    if len(keys) == 0:
        keys.append(8)
    return keys[0]

def vigBreakKnownKey(encrypted, keylength):
    keys = [0 for i in range(keylength)]
    count = 0
    for i in range(keylength):
        keys[i] = getShift(encrypted[i::keylength])
        print(keys)
        keys[3] = 9
        keys[11] = 20
        keys[17] = 9
    answer = ""
    for j in range(len(encrypted)):
        
        """
        if j > 1 and 17 % j == 0 :
            for k in range(0,26):
                count = 0
                keys[17] = k
                answer += shiftBy(encrypted[j], 26 - keys[j % len(keys)])
                for words in common_words:
                    if words in answer:
                        count += 1
                print(k, count)
        """
        #count = 0
        answer += shiftBy(encrypted[j], 26 - keys[j % len(keys)])
    for words in common_words:
        if words in answer:
            count += 1
    print(count)
    count = 0
    
    return answer
"""
def mine(encrypted1, keylength):
    keys = [0 for i in range(keylength)]
    keys = getShift(encrypted1[0::keylength])
    answer = ""
    for j in range (len(encrypted1)):
        answer += shiftBy(encrypted1[j], 26 - keys[j % len(keys)])

"""
'''
for i in range (1,27):
    for j in range(20):
        f = file('blackhat1.txt', 'r')
        etext = f.read()
        etext = etext.replace(" ", "")
        etext = filter(lambda x: x.isalpha, etext)
        etext = etext[j::i]
        answer = getShift(etext)
        print ("Possible keylength: ", i, "Shift: ",j)
        print answer
'''
#answer1 = {}
f = file('blackhat3.txt', 'r')
etext = f.read()
etext = etext.replace(" ", "")
etext = filter(lambda x: x.isalpha, etext)
answer1 = vigBreakKnownKey(etext, 19)
print(answer1)
wf = file('solved_blackhat3.txt', 'w')
wf.write(answer1)