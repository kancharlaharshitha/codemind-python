n=int(input())
for k in range(n):
    strl, str2= input(),input()
    if (len(strl) == len(str2)):
        for i in range(len(strl)):
            if (strl[i]>str2[i]):
                print('NO')
                break
        else:
            print("YES")
    else:
        print("NO")