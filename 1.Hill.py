from fractions import gcd as bltin_gcd
f = open('blackhat1.txt', 'r')
etext = f.read()
length = len(etext)
listofwords = [0 for i in range(4)]
determinant = 0
inverse = 0
count = 0
adj_matrix = [0 for i in range(4)]
enc_matrix = [0 for i in range(2)]
dec_matrix = [0 for i in range(2)]

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def getNumber(letter):
    num_letter = ord(letter) - 97
    return num_letter

def getLetter(number):
    number += 97
    letter = chr(number)
    return letter
    
for i in range (0,26):
    word = ""
    a = i
    for j in range(0,26):
        b = j
        for k in range(0,26):
            c = k
            for l in range(0, 26):
                d = l
                dtext = ""
                determinant = (a*d) - (b*c)
                mod_determinant = determinant % 26
                if coprime2(mod_determinant, 26) is False:
                    continue
                for mul_inv_temp in range(100):
                    if((mod_determinant * mul_inv_temp) % 26 == 1):
                        inverse = mul_inv_temp
                        mul_inv_temp = 0
                        break
                adj_matrix[0] = d
                adj_matrix[1] = -b
                adj_matrix[2] = -c
                adj_matrix[3] = a
                for x in adj_matrix:
                    if ( x < 0 ):
                        x = x + 26
                    x = x * inverse
                    x = x % 26
                for enc in range(length)[0::2]:
                    num_enc = getNumber(etext[enc])
                    enc_matrix[0] = num_enc
                    num_enc = getNumber(etext[enc + 1])
                    enc_matrix[1] = num_enc
                    dec_matrix[0] = (adj_matrix[0]*enc_matrix[0] + adj_matrix[1]*enc_matrix[1]) % 26
                    dec_matrix[1] = (adj_matrix[2]*enc_matrix[0] + adj_matrix[3]*enc_matrix[1]) % 26
                    temp1 = getLetter(dec_matrix[0])
                    temp2 = getLetter((dec_matrix[1]))
                    dtext_temp = temp1 + temp2
                    dtext = dtext + dtext_temp
                frequency = {}
                
                for ascii in range(ord('a'), ord('a')+26):
                    frequency[chr(ascii)] = float(dtext.count(chr(ascii)))/len(dtext)
                sum_freqs_squared = 0.0
                for ltr in frequency:
                    sum_freqs_squared += frequency[ltr]*frequency[ltr]
                if abs(sum_freqs_squared - .065) < .005:
                    count += 1
                    print (i, j, k, l)
                    print (count)
                    print (dtext)
                    if ( i == 6 and j == 25 and k == 7 and l == 5):
                        wf = open('solved_blackhat1.txt', 'w')
                        wf.write(dtext)
                    

        
        
                    
                
                
                
                
        