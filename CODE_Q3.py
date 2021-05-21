def TextJustify(words,l):
    array=[]
    words = [x for x in words if x!=""]
    if l<=0:
        return [""]
    if len(words)==0:
        return [' '*l]
    while len(words)>0:
        left=l
        extra=0
        i=0
        while i<len(words):
            temp=words[i]
            if left-len(temp)<-1:
                break
            left-=len(temp)
            extra=left+1
            i+=1
        space=0
        if i==1:
            avespace=extra
        else:
            avespace=int(extra/(i-1))
            space=extra%(i-1)
        temp=''
        if i==1:
            temp+=words.pop(0)+' '*extra
            array.append(temp)
            continue
        if i==len(words):
            for k in range(i):
                temp+=words.pop(0)+' '
            temp+=' '*left
            array.append(temp)
            break
        for k in range(i-1):
            temp+=words.pop(0)+' '
            temp+=' '*avespace
            if k<space:
                temp+=' '
        temp+=words.pop(0)
        array.append(temp)
    return array
text=input("Enter Words to compute seperated by spaces:- ")
words=[]
words=text.split()
print(words)
print("Enter MAX_WIDTH:- ")
l=int(input())
print()
print(TextJustify(words,l))