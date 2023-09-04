# flag art
### Solved By James Crowley

For this challenge, we were given [code](/DownUnderCTF%202023/Given%20Info/flag-art.py) that produced a [file](/DownUnderCTF%202023/Given%20Info/output.txt). The file was made up of the characters .=w-o^* seemingly randomly assigned and arranged in the shape of the contest logo. The description was as follows:


<p align="center">
  <img src="https://github.com/zephyronepointoh/CTFWriteups/assets/97200193/cfadd02c-4eaf-43e3-af41-4c34fc22cc6f", width = 500 />
</p>

and the image:

<p align="center">
  <img src="https://github.com/zephyronepointoh/CTFWriteups/assets/97200193/b16178e6-c48a-4a48-a679-14ede52f8add", width = 600 />
</p>





---

The code is as follows:

```
message = open('./message.txt', 'rb').read() + open('./flag.txt', 'rb').read()

palette = '.=w-o^*'
template = list(open('./mask.txt', 'r').read())

canvas = ''
for c in message:
    for m in [2, 3, 5, 7]:
        while True:
            t = template.pop(0)
            if t == 'X':
                canvas += palette[c % m]
                break
            else:
                canvas += t

print(canvas)
```

A non-trivial amount of this code is simply used to map the message and flag to the logo of the competition. Removing it leaves us with this. 

```
message = open('./message.txt', 'rb').read() + open('./flag.txt', 'rb').read()

palette = '.=w-o^*'

"""
canvas = ''
for c in message:
    for m in [2, 3, 5, 7]:
        canvas += palette[c % m]

print(canvas)
```

That's better. Now, we can clearly see what's happening. The message.txt and flag.txt files are being read as binary, then some math is being performed on their components. 

```
for c in message:
    for m in [2, 3, 5, 7]:
        canvas += palette[c % m]
```

Every char in message is iterated through all the values for m. The values are the ascii numbers for characters, because we read the file as binary(rb). So if we mod each of these numbers by our four values, [2, 3, 5, 7], we will get a unique set of values that represents that number. I could have done some math(or guess and check) to determine how high you have to go to get repeat values, but I chose to skip that unless I ran into issues. ASCII(for our purposes) only has 128 for normal letters. 

Hint hint. I might write a challenge that uses higher values, and has the same amount of numbers as this. Could be fun. Or infuriating. Would definitely require some guess and check. 

```
palette = '.=w-o^*'
```

Either way, there's one more step to the encoding process. Each value that we get from the math is converted to the character at that index in palette. 0 is ., 1 is =, etc. That's added to the result. 

The beautiful logo of gibberish text in the shape of the competition logo can be shortened to this string. All newlines and spaces were removed with regex. This is our ciphertext. 

```
encoded = "==wo=.=*.w.^==-^..ow==w*.w=o=.w^..--==w*.w=o=...=.=*.w.^==.-.wwo=.=*.w.^.wwo==.-=.=*..--.=-*=....w.^==-^.wwo.w=o.wo*=...==.-.wwo=.o=.wo*==w*..--..--=w=-.w.^==-^=w=-=.-^.wwo..o..wo*=w=-.wwo==oo==w*==.-=www.wwo.wo*==w*==.-.wwo=.w=..-*..-*.wwo.=-o=.oo==.-.wwo==.-=.=*.wwo.wo*=w=-..ow=w=-.wwo==w*..ow=w=-.wwo==.-=.=*==oo=w=-.wwo..ow==w*.w.^.=.w=.=*==oo.wwo=wo.=.=*..ow.=.w==.-.wwo.w=o=.=*.wwo==oo==w*=www=w=-.wwo.w=o.wo*=w=-.wwo==oo=w=-==.-==.-==w*==-^=w=-.wwo..--=.=*.w.^==-^.wwo=w=-.w.^=.=*=.w^==-^.wo*.==o.wwo=wo^=.=*=.w^..ow.wwo..wo..--==w*==-^.wwo=...==.-.=-w.wwo.w-^==.===wo..o..=..=.-o..ow=.=w=.o=..-*.w.^==.-.w=o..ow=.w^=.o=.w=o==o...-*.w.^=w.o..-*..wo=w.o..wo..--.=w-==-^=w.o..wo..ow..-*==oo=w.o..wo..--.=w-==-^=w.o.=w-..ow==.*=w.o.w-.===w=w.o..--..-*..-*=www=.w^.=w.=w.o.w=o.=w-.w-...--=.=w=w.o..-*..ow=w.o=.o=.wo*==o..w.^=.=w==.-=.=w=w.o..ow=.=w==oo.=w-==o..w.^.=.w=.=w..ow==o..w.^==-^=.-.=w.*"

```

The first step in our solution is to turn these back into numbers. We'll basically be doing the encoding process in reverse. 
```
nums = []
for c in encoded:
    nums.append(palette.index(c))

print(nums)
```

This code gives us the numbers. There are 900 of them, which conveniently is divisible by four. This was how I confirmed what was going on. This is the output of print(nums).
```
[1, 1, 2, 4, 1, 0, 1, 6, 0, 2, 0, 5, 1, 1, 3, 5, 0, 0, 4, 2, 1, 1, 2, 6, 0, 2, 1, 4, 1, 0, 2, 5, 0, 0, 3, 3, 1, 1, 2, 6, 0, 2, 1, 4, 1, 0, 0, 0, 1, 0, 1, 6, 0, 2, 0, 5, 1, 1, 0, 3, 0, 2, 2, 4, 1, 0, 1, 6, 0, 2, 0, 5, 0, 2, 2, 4, 1, 1, 0, 3, 1, 0, 1, 6, 0, 0, 3, 3, 0, 1, 3, 6, 1, 0, 0, 0, 0, 2, 0, 5, 1, 1, 3, 5, 0, 2, 2, 4, 0, 2, 1, 4, 0, 2, 4, 6, 1, 0, 0, 0, 1, 1, 0, 3, 0, 2, 2, 4, 1, 0, 4, 1, 0, 2, 4, 6, 1, 1, 2, 6, 0, 0, 3, 3, 0, 0, 3, 3, 1, 2, 1, 3, 0, 2, 0, 5, 1, 1, 3, 5, 1, 2, 1, 3, 1, 0, 3, 5, 0, 2, 2, 4, 0, 0, 4, 0, 0, 2, 4, 6, 1, 2, 1, 3, 0, 2, 2, 4, 1, 1, 4, 4, 1, 1, 2, 6, 1, 1, 0, 3, 1, 2, 2, 2, 0, 2, 2, 4, 0, 2, 4, 6, 1, 1, 2, 6, 1, 1, 0, 3, 0, 2, 2, 4, 1, 0, 2, 1, 0, 0, 3, 6, 0, 0, 3, 6, 0, 2, 2, 4, 0, 1, 3, 4, 1, 0, 4, 4, 1, 1, 0, 3, 0, 2, 2, 4, 1, 1, 0, 3, 1, 0, 1, 6, 0, 2, 2, 4, 0, 2, 4, 6, 1, 2, 1, 3, 0, 0, 4, 2, 1, 2, 1, 3, 0, 2, 2, 4, 1, 1, 2, 6, 0, 0, 4, 2, 1, 2, 1, 3, 0, 2, 2, 4, 1, 1, 0, 3, 1, 0, 1, 6, 1, 1, 4, 4, 1, 2, 1, 3, 0, 2, 2, 4, 0, 0, 4, 2, 1, 1, 2, 6, 0, 2, 0, 5, 0, 1, 0, 2, 1, 0, 1, 6, 1, 1, 4, 4, 0, 2, 2, 4, 1, 2, 4, 0, 1, 0, 1, 6, 0, 0, 4, 2, 0, 1, 0, 2, 1, 1, 0, 3, 0, 2, 2, 4, 0, 2, 1, 4, 1, 0, 1, 6, 0, 2, 2, 4, 1, 1, 4, 4, 1, 1, 2, 6, 1, 2, 2, 2, 1, 2, 1, 3, 0, 2, 2, 4, 0, 2, 1, 4, 0, 2, 4, 6, 1, 2, 1, 3, 0, 2, 2, 4, 1, 1, 4, 4, 1, 2, 1, 3, 1, 1, 0, 3, 1, 1, 0, 3, 1, 1, 2, 6, 1, 1, 3, 5, 1, 2, 1, 3, 0, 2, 2, 4, 0, 0, 3, 3, 1, 0, 1, 6, 0, 2, 0, 5, 1, 1, 3, 5, 0, 2, 2, 4, 1, 2, 1, 3, 0, 2, 0, 5, 1, 0, 1, 6, 1, 0, 2, 5, 1, 1, 3, 5, 0, 2, 4, 6, 0, 1, 1, 4, 0, 2, 2, 4, 1, 2, 4, 5, 1, 0, 1, 6, 1, 0, 2, 5, 0, 0, 4, 2, 0, 2, 2, 4, 0, 0, 2, 4, 0, 0, 3, 3, 1, 1, 2, 6, 1, 1, 3, 5, 0, 2, 2, 4, 1, 0, 0, 0, 1, 1, 0, 3, 0, 1, 3, 2, 0, 2, 2, 4, 0, 2, 3, 5, 1, 1, 0, 1, 1, 1, 2, 4, 0, 0, 4, 0, 0, 1, 0, 0, 1, 0, 3, 4, 0, 0, 4, 2, 1, 0, 1, 2, 1, 0, 4, 1, 0, 0, 3, 6, 0, 2, 0, 5, 1, 1, 0, 3, 0, 2, 1, 4, 0, 0, 4, 2, 1, 0, 2, 5, 1, 0, 4, 1, 0, 2, 1, 4, 1, 1, 4, 0, 0, 0, 3, 6, 0, 2, 0, 5, 1, 2, 0, 4, 0, 0, 3, 6, 0, 0, 2, 4, 1, 2, 0, 4, 0, 0, 2, 4, 0, 0, 3, 3, 0, 1, 2, 3, 1, 1, 3, 5, 1, 2, 0, 4, 0, 0, 2, 4, 0, 0, 4, 2, 0, 0, 3, 6, 1, 1, 4, 4, 1, 2, 0, 4, 0, 0, 2, 4, 0, 0, 3, 3, 0, 1, 2, 3, 1, 1, 3, 5, 1, 2, 0, 4, 0, 1, 2, 3, 0, 0, 4, 2, 1, 1, 0, 6, 1, 2, 0, 4, 0, 2, 3, 0, 1, 1, 1, 2, 1, 2, 0, 4, 0, 0, 3, 3, 0, 0, 3, 6, 0, 0, 3, 6, 1, 2, 2, 2, 1, 0, 2, 5, 0, 1, 2, 0, 1, 2, 0, 4, 0, 2, 1, 4, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 3, 3, 1, 0, 1, 2, 1, 2, 0, 4, 0, 0, 3, 6, 0, 0, 4, 2, 1, 2, 0, 4, 1, 0, 4, 1, 0, 2, 4, 6, 1, 1, 4, 0, 0, 2, 0, 5, 1, 0, 1, 2, 1, 1, 0, 3, 1, 0, 1, 2, 1, 2, 0, 4, 0, 0, 4, 2, 1, 0, 1, 2, 1, 1, 4, 4, 0, 1, 2, 3, 1, 1, 4, 0, 0, 2, 0, 5, 0, 1, 0, 2, 1, 0, 1, 2, 0, 0, 4, 2, 1, 1, 4, 0, 0, 2, 0, 5, 1, 1, 3, 5, 1, 0, 3, 0, 1, 2, 0, 6]
```

Next, fournums. This takes all the digits 0-255(127 would be enough) and performs the mod operations on them. 

```
fournums = []

for i in range(0, 256):
    fournums.append([i%2, i%3, i%5, i%7])

print(fournums)
```
And the output. All in groups of four.
```
[[0, 0, 0, 0], [1, 1, 1, 1], [0, 2, 2, 2], [1, 0, 3, 3], [0, 1, 4, 4], [1, 2, 0, 5], [0, 0, 1, 6], [1, 1, 2, 0], [0, 2, 3, 1], [1, 0, 4, 2], [0, 1, 0, 3], [1, 2, 1, 4], [0, 0, 2, 5], [1, 1, 3, 6], [0, 2, 4, 0], [1, 0, 0, 1], [0, 1, 1, 2], [1, 2, 2, 3], [0, 0, 3, 4], [1, 1, 4, 5], [0, 2, 0, 6], [1, 0, 1, 0], [0, 1, 2, 1], [1, 2, 3, 2], [0, 0, 4, 3], [1, 1, 0, 4], [0, 2, 1, 5], [1, 0, 2, 6], [0, 1, 3, 0], [1, 2, 4, 1], [0, 0, 0, 2], [1, 1, 1, 3], [0, 2, 2, 4], [1, 0, 3, 5], [0, 1, 4, 6], [1, 2, 0, 0], [0, 0, 1, 1], [1, 1, 2, 2], [0, 2, 3, 3], [1, 0, 4, 4], [0, 1, 0, 5], [1, 2, 1, 6], [0, 0, 2, 0], [1, 1, 3, 1], [0, 2, 4, 2], [1, 0, 0, 3], [0, 1, 1, 4], [1, 2, 2, 5], [0, 0, 3, 6], [1, 1, 4, 0], [0, 2, 0, 1], [1, 0, 1, 2], [0, 1, 2, 3], [1, 2, 3, 4], [0, 0, 4, 5], [1, 1, 0, 6], [0, 2, 1, 0], [1, 0, 2, 1], [0, 1, 3, 2], [1, 2, 4, 3], [0, 0, 0, 4], [1, 1, 1, 5], [0, 2, 2, 6], [1, 0, 3, 0], [0, 1, 4, 1], [1, 2, 0, 2], [0, 0, 1, 3], [1, 1, 2, 4], [0, 2, 3, 5], [1, 0, 4, 6], [0, 1, 0, 0], [1, 2, 1, 1], [0, 0, 2, 2], [1, 1, 3, 3], [0, 2, 4, 4], [1, 0, 0, 5], [0, 1, 1, 6], [1, 2, 2, 0], [0, 0, 3, 1], [1, 1, 4, 2], [0, 2, 0, 3], [1, 0, 1, 4], [0, 1, 2, 5], [1, 2, 3, 6], [0, 0, 4, 0], [1, 1, 0, 1], [0, 2, 1, 2], [1, 0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [0, 0, 0, 6], [1, 1, 1, 0], [0, 2, 2, 1], [1, 0, 3, 2], [0, 1, 4, 3], [1, 2, 0, 4], [0, 0, 1, 5], [1, 1, 2, 6], [0, 2, 3, 0], [1, 0, 4, 1], [0, 1, 0, 2], [1, 2, 1, 3], [0, 0, 2, 4], [1, 1, 3, 5], [0, 2, 4, 6], [1, 0, 0, 0], [0, 1, 1, 1], [1, 2, 2, 2], [0, 0, 3, 3], [1, 1, 4, 4], [0, 2, 0, 5], [1, 0, 1, 6], [0, 1, 2, 0], [1, 2, 3, 1], [0, 0, 4, 2], [1, 1, 0, 3], [0, 2, 1, 4], [1, 0, 2, 5], [0, 1, 3, 6], [1, 2, 4, 0], [0, 0, 0, 1], [1, 1, 1, 2], [0, 2, 2, 3], [1, 0, 3, 4], [0, 1, 4, 5], [1, 2, 0, 6], [0, 0, 1, 0], [1, 1, 2, 1], [0, 2, 3, 2], [1, 0, 4, 3], [0, 1, 0, 4], [1, 2, 1, 5], [0, 0, 2, 6], [1, 1, 3, 0], [0, 2, 4, 1], [1, 0, 0, 2], [0, 1, 1, 3], [1, 2, 2, 4], [0, 0, 3, 5], [1, 1, 4, 6], [0, 2, 0, 0], [1, 0, 1, 1], [0, 1, 2, 2], [1, 2, 3, 3], [0, 0, 4, 4], [1, 1, 0, 5], [0, 2, 1, 6], [1, 0, 2, 0], [0, 1, 3, 1], [1, 2, 4, 2], [0, 0, 0, 3], [1, 1, 1, 4], [0, 2, 2, 5], [1, 0, 3, 6], [0, 1, 4, 0], [1, 2, 0, 1], [0, 0, 1, 2], [1, 1, 2, 3], [0, 2, 3, 4], [1, 0, 4, 5], [0, 1, 0, 6], [1, 2, 1, 0], [0, 0, 2, 1], [1, 1, 3, 2], [0, 2, 4, 3], [1, 0, 0, 4], [0, 1, 1, 5], [1, 2, 2, 6], [0, 0, 3, 0], [1, 1, 4, 1], [0, 2, 0, 2], [1, 0, 1, 3], [0, 1, 2, 4], [1, 2, 3, 5], [0, 0, 4, 6], [1, 1, 0, 0], [0, 2, 1, 1], [1, 0, 2, 2], [0, 1, 3, 3], [1, 2, 4, 4], [0, 0, 0, 5], [1, 1, 1, 6], [0, 2, 2, 0], [1, 0, 3, 1], [0, 1, 4, 2], [1, 2, 0, 3], [0, 0, 1, 4], [1, 1, 2, 5], [0, 2, 3, 6], [1, 0, 4, 0], [0, 1, 0, 1], [1, 2, 1, 2], [0, 0, 2, 3], [1, 1, 3, 4], [0, 2, 4, 5], [1, 0, 0, 6], [0, 1, 1, 0], [1, 2, 2, 1], [0, 0, 3, 2], [1, 1, 4, 3], [0, 2, 0, 4], [1, 0, 1, 5], [0, 1, 2, 6], [1, 2, 3, 0], [0, 0, 4, 1], [1, 1, 0, 2], [0, 2, 1, 3], [1, 0, 2, 4], [0, 1, 3, 5], [1, 2, 4, 6], [0, 0, 0, 0], [1, 1, 1, 1], [0, 2, 2, 2], [1, 0, 3, 3], [0, 1, 4, 4], [1, 2, 0, 5], [0, 0, 1, 6], [1, 1, 2, 0], [0, 2, 3, 1], [1, 0, 4, 2], [0, 1, 0, 3], [1, 2, 1, 4], [0, 0, 2, 5], [1, 1, 3, 6], [0, 2, 4, 0], [1, 0, 0, 1], [0, 1, 1, 2], [1, 2, 2, 3], [0, 0, 3, 4], [1, 1, 4, 5], [0, 2, 0, 6], [1, 0, 1, 0], [0, 1, 2, 1], [1, 2, 3, 2], [0, 0, 4, 3], [1, 1, 0, 4], [0, 2, 1, 5], [1, 0, 2, 6], [0, 1, 3, 0], [1, 2, 4, 1], [0, 0, 0, 2], [1, 1, 1, 3], [0, 2, 2, 4], [1, 0, 3, 5], [0, 1, 4, 6], [1, 2, 0, 0], [0, 0, 1, 1], [1, 1, 2, 2], [0, 2, 3, 3], [1, 0, 4, 4], [0, 1, 0, 5], [1, 2, 1, 6], [0, 0, 2, 0], [1, 1, 3, 1], [0, 2, 4, 2], [1, 0, 0, 3]]
```
Now for the answer. I incorporated an amazing one-liner here, and will use it as an exercise in explaining myself.
```
funlist = []

for i in range(0, int(len(nums)/4)):
    j = i * 4
    funlist.append(chr(fournums.index([nums[j],nums[j+1],nums[j+2],nums[j+3]])))

print("".join(funlist))
```

First, the for loop. Iterates through the length of nums/4. Then, we assign these values to j, and multiply it by four. This code makes j iterate by four. Is there a better way to do it? Sure. This was quick and dirty, I was having fun. Sue me.

Next, the nasty oneliner. Starting from the inside, we take, four at a time, the numbers in nums(ciphertex), and group them like I had them in fournums(key). Then I use the index method to locate where in fournums this is. This number corresponds to the ASCII value for the character in plaintext. The chr() method makes it the actual value.

Because I am apparently allergic to strings, I used a list, and the .join() method to list it out. The result is:
```
Congratulations on solving this challenge! The mask has 900 X's so here are some random words to make the message long enough. Your flag is: DUCTF{r3c0nstruct10n_0f_fl4g_fr0m_fl4g_4r7_by_l00kup_t4bl3_0r_ch1n3s3_r3m41nd3r1ng?}
```

# The Subsequent Rabbit Hole

To answer the flag's question, basically a lookup table. I actually had never heard of the Chinese Remainder Theorem. 

Essentially, it says if you know the answers for a few modulus operations, where the modulus operators are coprime(none of them are divisible by each other) you can determine the original if it's less than the product of those operators. 

If it's greater, then it's that original number plus a multiple of the product of those operators.

This problem led me down a rabbit hole of learning about this, so to make it worthwhile, I will explain it through an example below.

## Chinese Remainder Theorem

121 will be the example number. The modulo numbers will be 2, 3, 5 and 7 as used in this challenge. Here are the results of the mod operators on this number.

```
121 mod 2 = 1
121 mod 3 = 1
121 mod 5 = 1
121 mod 7 = 2
```
|  operator(n) | 2 | 3 | 5 | 7 |
|---|---|---|---|---|
| mod(m)  |  1 |  1 | 1  |  1 |

Now, for each number, we will write the product of the other numbers in its column. The product of all the numbers is 210. This will be part of our result at the end, so remember it. 

| operator(n)  | 2 | 3 | 5 | 7 |
|---|---|---|---|---|
| mod(m)  |  1 |  1 | 1  |  2 |
| products(p)  | 105  | 70  | 42  | 30  |

Finally, the hardest part. We need to find out what number h, times the product, mod n, = 1. Guess and check gets this pretty quick.
``` 
(h*p)mod(n) = 1
h = ?
```
| operator(n)  | 2 | 3 | 5 | 7 |
|---|---|---|---|---|
| mod(m)  |  1 |  1 | 1  |  2 |
| products(p)  | 105  | 70  | 42  | 30  |
| multiplier(h)  |  1 | 1  | 3  | 4  |

The rest is easy. We multiply down the columns, then add. 

| operator(n)  | 2 | 3 | 5 | 7 ||
|---|---|---|---|---|---|
| mod(m)  |  1 |  1 | 1  |  2 ||
| products(p)  | 105  | 70  | 42  | 30  ||
| multipliers(h)  |  1 | 1  | 3  | 4  ||
| **Total** |  105 | 70 | 126  | 240  |**541**|

And it's 541. Subtract 210 twice, and we're left with our original number, 121. 

The exact answer to this is that any number that produces 1, 1, 1, and 2 from the modulus operators 2, 3, 5, and 7 is 121+(210*n) for any integer n. 

Python implementation of function

```
def chineseremainder(operators: list, results: list, printme: bool):
    opprod = 1
    products = []
    multipliers = []
    for each in operators:
        opprod *= each

    for eachh in operators:
        products.append(int(opprod/eachh))

    for eachhh in products:
        n = 1
        while int((eachhh*n) % (operators[products.index(eachhh)])) != 1:
            n += 1
        multipliers.append(n)

    total = 0
    for i in range(len(operators)):
        total += (results[i] * products[i] * multipliers[i])

    base_original = int(total % opprod)
    if printme:
        print(opprod)
        print(products)
        print(multipliers)
        print("With original values " + str(operators) + " and results " + str(results))
        print("The original number can be expressed by the formula " + str(base_original) + " + (" + str(opprod) + " * n) for any integer n.")
    return base_original, opprod

```

Implementation for this problem

```
nums = []
for c in encoded:
    nums.append(palette.index(c))

funlist = []

for i in range(0, int(len(nums)/4)):
    j = i * 4
    funlist.append(chr(chineseremainder([2,3,5,7],[nums[j],nums[j+1],nums[j+2],nums[j+3]], False)[0]))

print("".join(funlist))
```
