from rev.strings.utils import s2l, l2s

def xor(s1,s2):
    res=[]
    base=len(s1)

    if type(s1)!=str or type(s2)!=str:
        print '[REV ERROR] type should be str'
        return
    if len(s1)<len(s2):
        print '[REV ERROR]len of first argv should be longer than second one or same.'
        return

    l1=s2l(s1)
    l2=s2l(s2)

    for i in range(len(l1)):
       res.append(l1[i]^l2[i%base])
    return l2s(res)

def lsh(s,op):
    l=s2l(s)
    res=[]

    if type(s)!=str:
        print '[REV ERROR]type should be string'
        return

    for elem in l:
        res.append(elem<<op)
    return l2s(res)

def rsh(s,op):
    l=s2l(s)
    res=[]

    if type(s)!=str:
        print '[REV ERROR]type should be string'
        return

    for elem in l:
        res.append(elem>>op)
    return l2s(res)

def rot(s,op):
    l=s2l(s)
    res=l[op%len(s):]+l[:op%len(s)]
    return l2s(res)