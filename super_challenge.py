"""Super challenge
    Zeeshan
    """
def fileword(A):
    result = []
    first_word = True

    while A:
        for i , pair  in enumerate(A):

# For reading the first pair only 
            if i == 0 and first_word:

# Appending every word alone to result 
                result.append(pair.split(">")[0])
                result.append(pair.split(">")[1])
                
# Poping the first word so it wouldnt be read every time                
                A.pop(0)
                first_word = False
            else:
                if (pair.split(">")[0] in result) or (pair.split(">")[1] in result):
                    if (pair.split(">")[0]) in result:
                        result.append(pair.split(">")[1] )
                        A.pop(i)
                    else:
                        result.insert(0 , pair.split(">")[0])
                        A.pop(i)
                else:
                    pass
    s = ""
    for t in result: # For converting every word which is in str to simple one str
        s = s+t
    print(s)

fileword(["p>e","e>r","r>u"])
fileword(["I>N","A>I","P>A","S>P"])
fileword(["A>N","Z>E","H>A" ,"E>S","S>H"])