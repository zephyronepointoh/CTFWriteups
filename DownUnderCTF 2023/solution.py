message = open('./message.txt', 'rb').read()


palette = '.=w-o^*'
#template = list(open('./mask.txt', 'r').read())

###Used regex to remove tabs, spaces, newlines from output.txt
encoded = "==wo=.=*.w.^==-^..ow==w*.w=o=.w^..--==w*.w=o=...=.=*.w.^==.-.wwo=.=*.w.^.wwo==.-=.=*..--.=-*=....w.^==-^.wwo.w=o.wo*=...==.-.wwo=.o=.wo*==w*..--..--=w=-.w.^==-^=w=-=.-^.wwo..o..wo*=w=-.wwo==oo==w*==.-=www.wwo.wo*==w*==.-.wwo=.w=..-*..-*.wwo.=-o=.oo==.-.wwo==.-=.=*.wwo.wo*=w=-..ow=w=-.wwo==w*..ow=w=-.wwo==.-=.=*==oo=w=-.wwo..ow==w*.w.^.=.w=.=*==oo.wwo=wo.=.=*..ow.=.w==.-.wwo.w=o=.=*.wwo==oo==w*=www=w=-.wwo.w=o.wo*=w=-.wwo==oo=w=-==.-==.-==w*==-^=w=-.wwo..--=.=*.w.^==-^.wwo=w=-.w.^=.=*=.w^==-^.wo*.==o.wwo=wo^=.=*=.w^..ow.wwo..wo..--==w*==-^.wwo=...==.-.=-w.wwo.w-^==.===wo..o..=..=.-o..ow=.=w=.o=..-*.w.^==.-.w=o..ow=.w^=.o=.w=o==o...-*.w.^=w.o..-*..wo=w.o..wo..--.=w-==-^=w.o..wo..ow..-*==oo=w.o..wo..--.=w-==-^=w.o.=w-..ow==.*=w.o.w-.===w=w.o..--..-*..-*=www=.w^.=w.=w.o.w=o.=w-.w-...--=.=w=w.o..-*..ow=w.o=.o=.wo*==o..w.^=.=w==.-=.=w=w.o..ow=.=w==oo.=w-==o..w.^.=.w=.=w..ow==o..w.^==-^=.-.=w.*"

"""
canvas = ''
for c in message:
    for m in [2, 3, 5, 7]:
        canvas += palette[c % m]

print(canvas)

"""



nums = []
for c in encoded:
    nums.append(palette.index(c))

print(nums)

fournums = []

for i in range(0, 256):
    fournums.append([i%2, i%3, i%5, i%7])

print(fournums)

funlist = []

for i in range(0, int(len(nums)/4)):
    j = i * 4
    funlist.append(chr(fournums.index([nums[j],nums[j+1],nums[j+2],nums[j+3]])))

print("".join(funlist))
