
l=[['afok2','pkfn3 ','864ty'],['qwe5','zxc90','hjn76']]
a=''
b=''
for i in l:
    for j in i:
         for k in j:
            if k.isdigit():
                a+=k
            elif k.isalpha():
                b+=k
print(''.join(sorted(a)))
print(''.join(sorted(b)))
