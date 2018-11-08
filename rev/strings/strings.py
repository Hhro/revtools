def s2l(s):
    return [ord(x) for x in s]

def l2s(l):
    return ''.join([chr(x) for x in l])

def xor(l1,l2):
    res=[]
    base=len(l2)

    if type(l1)==str:
        l1=s2l(l1)
    if type(l2)==str:
        l2=s2l(l2)
    if type(l1)!=list or type(l2)!=list:
        print '[REV ERROR]type should be list or string'
        return 
    if len(l1)<len(l2):
        print '[REV ERROR]len of first argv should be longer than second one or same.'
        return

    for i in range(len(l1)):
       res.append(l1[i]^l2[i%base])
    return res
