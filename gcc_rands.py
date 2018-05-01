import itertools, random
def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)

theseed = random.randint(1, 2**30)
skip = random.randint(10000, 200000)
print (theseed,skip)
#theseed = 1987
#skip = 10001
my_generator = crand(theseed)
for i in range(skip):
    temp = my_generator.next()

the_input = [my_generator.next() for i in range(93)]

the_output = [my_generator.next() for i in range(93)]

o = the_input
r = [-1 for i in range(93*2)]
x = [-1 for i in range(93)]


def code(theinput):
    o_guesses = []
    for i in range(31,93):
       
        diff = o[i] - (o[i-3] + o[i - 31]) % 2**31
        
        if diff == 1:
            x[i] = 0
            x[i - 3] = 1
            x[i - 31] = 1
        elif diff == 0:
            if x[i] == 0:
                x[i-3] = 0
                x[i-31] = 0
            elif x[i-3] == 1:
                x[i] = 1
                x[i-31] = 0
            elif x[i -31] == 1:
                x[i] = 1
                x[i-3] = 0
    
    for i in range(93):
        if x[i] != -1:
            r[i] = 2 * o[i] + x[i]
        if r[i-3] != -1 and r[i-31] != -1:
            r[i] = (r[i-3] + r[i-31]) % 2**32
    
    unknowns = []
    count1 = r[58:93].count(-1)
    lst = list(itertools.product([0, 1], repeat=count1))
    for i in range(58,93):
        if r[i] == -1:
            unknowns.append(i)

    for i in lst:
        u1 = 0
        for j in i:
            u = unknowns[u1]
            u1 = u1 + 1
            r[u] = (2 * o[u]) + j
         
        for l in range(93):
            r[93 + l] = ((r[(93 + l) - 3] + r[(93 + l) -31]) % 2**32) 
            o_guesses.append(r[93 +l] >> 1)
       
        if(the_output == o_guesses):
            theoutput = o_guesses
            return theoutput
        o_guesses = []
 
if code(the_input) == the_output:
    print ("Successfully predicted all the outcomes")
else:
    print ("Try again")
