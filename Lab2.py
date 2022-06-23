import Crypto.Util.number as cu

def findFactor(size_):
    p_ = cu.getPrime(size_)
    while (p_ % 4 != 3):
        p_ = cu.getPrime(size_)
    q_ = cu.getPrime(size_)
    while (q_ % 4 != 3) or (q_ == p_):
        q_ = cu.getPrime(size_)
    return p_, q_			
	
def findSeed(size_, n_):
    s_ = cu.getRandomNBitInteger(int(size_ / 2))
    while not (cu.GCD(s_, n_) == 1):
        s_ = cu.getRandomNBitInteger(int(size_ / 2))
    return s_

size = (512 + 512)
p, q = findFactor(size)
print(p)
print(q)

n = p * q
s = findSeed(size, n)

m = "Wiwi es la mejor"
mBytes = bytearray(m.encode())
mNumber = cu.bytes_to_long(mBytes)
k = 0b0
X0 = (s ** 2) % n
for i in range(0, len(mBytes)*8, 1):
    Xi = (X0 ** 2) % n
    k = (k << 1) | (Xi % 2)
    X0 = Xi
cipherNumber = mNumber ^ k
cipheredBytes = cu.long_to_bytes(cipherNumber)
uncipherNumber = cipherNumber ^ k
uncipheredBytes = cu.long_to_bytes(uncipherNumber)
print('\n Ciphered: ', cipheredBytes)
print('\n Deciphered: ', uncipheredBytes.decode())
exit()
