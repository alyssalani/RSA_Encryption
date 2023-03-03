import plistlib
import random
import math

class RSA:

    def __init__(self):
        self.baseAlphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alphabet = ".,?! \t\n\rabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        # self.baseAlphabet = string1
        # self.alphabet = string2

    def generateKeys(self, s1, s2):

        pBase10 = self.toBase10(s1, self.baseAlphabet)
        qBase10 = self.toBase10(s2, self.baseAlphabet)

        if pBase10 >= 10**200:
            p = pBase10 % 10**200
        else:
            print("String 1 Not Long Enough")
            
        if qBase10 >= 10**200:
            q = qBase10 % 10**200
        else:
            print("String 2 Not Long Enough")

        if p % 2 == 0:
            p += 1
        if q % 2 == 0:
            q += 1

        prime_p = self.makeOddAndPrime(p)
        prime_q = self.makeOddAndPrime(q)
        
        n = prime_p * prime_q
        r = (prime_p-1)*(prime_q-1)
        e = self.generateRandomNum(398)
        if e % 2 == 0:
            e += 1
        while self.IsPrimeMiller(e) == False:
            e += 2
        
        gcd,x,d = self.gcdExtended(r,e)

        f = open("public.txt","w")
        f.write(str(n))
        f.write("\n")
        f.write(str(e))
        f.close()

        fw = open("private.txt", "w")
        fw.write(str(n))
        fw.write("\n")
        fw.write(str(d))
        fw.close()

    def encrypt(self, inputfile, outfile):
        fin = open(inputfile,"rb")
        PlainTextBinary = fin.read()
        PlainText = PlainTextBinary.decode("utf-8")
        fin.close()

        public = open("public.txt")
        file_contents = public.read()
        contents = file_contents.splitlines()
        print(contents)
        n = contents[0]
        e = contents[1]

        size_chunk = 216
        chunks = [PlainText[i:i+size_chunk]
                    for i in range(0, len(PlainText), size_chunk)]

        fout = open(outfile, "wb")
        i = 0
        money = "$"
        for i in range(len(chunks)):
            chunks[i] = self.toBase10(chunks[i], self.alphabet)
            chunks[i] = pow(int(chunks[i]), int(e), int(n))
            chunks[i] = self.fromBase10(chunks[i], self.alphabet)
            fout.write(chunks[i].encode("utf-8"))
            fout.write(money.encode("utf-8"))
        fout.close()
    
    def decrypt(self, inputfile, outfile):
        fin = open(inputfile, "rb")
        PlainTextBinary = fin.read()
        PlainText = PlainTextBinary.decode("utf-8")
        fin.close()

        blocks = PlainText.split("$")

        private = open("private.txt")
        file_contents = private.read()
        contents = file_contents.splitlines()
        n = contents[0]
        d = contents[1]
        fout = open(outfile, "wb")
        i = 0
        for i in range(len(blocks)):
            blocks[i] = self.toBase10(blocks[i], self.alphabet)
            blocks[i] = pow(blocks[i], int(d), int(n))
            blocks[i] = self.fromBase10(blocks[i], self.alphabet)
            fout.write(blocks[i].encode("utf-8"))
        fout.close()

    def generateRandomNum(self,n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)

    def toBase10(self, n,alphabet):
        a = 0
        for c in n:
            pos = alphabet.find(c)
            a *= len(alphabet)
            a += pos
        return a

    def fromBase10(self,n, alphabet):
        string = ""
        while n:
            pos = int(n%len(alphabet))
            string += alphabet[pos]
            n //= len(alphabet)
        return(string[::-1])

    def checkSize(num):
        if num >= 10**200:
            return num % 10**200
        else:
            print("String Not Long Enough")

    def gcdExtended(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1  = self.gcdExtended(b % a, a)
        x = y1 - (b//a)*x1
        y = x1

        return gcd,x,y

    def makeOddAndPrime(self, num):
        if num % 2 == 0:
            num += 1
        while self.IsPrimeMiller(num) == False:
            num += 2
        return num

    def IsPrimeMiller(self,x):
        x = int(x)
        for i in range(20):
            b = random.randrange(2,x)
            r = self.MillerTest(x,b)
            if r == False:
                return False
        return True

    def MillerTest(self, x,b):
        t = x-1 
        s = 0 
        while t%2 == 0:
            t = t//2
            s+= 1
        if pow(b,t,x)==1:
            return True
        for i in range(s):
            if pow(b,t,x)==x-1:
                return True
            t *= 2
        return False
def _main_():
    mRSA = RSA()
    mRSA.generateKeys("fjiowjijklfjaiojoiwefmofnmoiewajfoiejwioajfioewjfioaewjfioewjfioajfioewncnijfwiojpwofnagajiejgiomadmpcjllpajfojeiajjfajocjimkmaklmcejaiojiogejakmkf", "yessheisvejoifwjomcmaklmkfjiawjpwaokmceajofejioajfioejiofjaiojeiofjaeiowfjelkfjewoiajfioawjfioejiofjawiojeojfeioafjeiigjioeanfkmapklmlzjocidjicomklmkfmpajgioajijfidjankngkalmkclmdjmakfniaenfkamgekamfiajijafamfkmefijiejiejttifjeiojaiojifajaiojfoijaifojaikfji")
    mRSA.encrypt("data.txt", "encrypted.txt")
    mRSA.decrypt("encrypted.txt", "decrypted.txt")


_main_()
