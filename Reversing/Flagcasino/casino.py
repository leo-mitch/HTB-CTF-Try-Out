#  in the 'casino' binary, i found that the main function calls srand() then rand().
# then it compare the srand() output of the char i entered with a value stored in a list called 'check' (found that using Ghidra)
# since rand() is not actually random, i can find what value rand() will create using the decimal value stored in 'check' and initializing the generator (srand()) with that decimal value

import ctypes

libc = ctypes.CDLL("libc.so.6") # import the srand() & rand() function from C

check = [ # all 4 bytes integer stored in Hex, from Ghidra, thx chatgpt for formating this for me in a python list lmao
    0x244B28BE,
    0x0AF77805,
    0x110DFC17,
    0x07AFC3A1,
    0x6AFEC533,
    0x4ED659A2,
    0x33C5D4B0,
    0x286582B8,
    0x43383720,
    0x055A14FC,
    0x19195F9F,
    0x43383720,
    0x63149380,
    0x615AB299,
    0x6AFEC533,
    0x6C6FCFB8,
    0x43383720,
    0x0F3DA237,
    0x6AFEC533,
    0x615AB299,
    0x286582B8,
    0x055A14FC,
    0x3AE44994,
    0x06D7DFE9,
    0x4ED659A2,
    0x0CCD4ACD,
    0x57D8ED64,
    0x615AB299,
    0x22E9BC2A,
]



def get_flag():
    flag = ""
    for x in check:
        for i in range(256): # int is 255 bytes
            libc.srand(i) 
            tmp = libc.rand() # generate the first pseudorandom number from seed 'srand(i)'  which i is the 4 byte decimal found in the check list
            if tmp == x:
                flag += chr(i)
                break
    print(flag) # get pwned
    
get_flag()