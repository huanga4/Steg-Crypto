import pyaes
import numpy

def tobits(msg): #converts msg as string to array of bits [0,0,1,0,1]etc..
    msgasbits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in msg])))
    return msgasbits

#msg = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

def frombits(bits): #from array of bits return a msg as string
    bitsasmsg = "".join(chr(int("".join(map(str,bits[i:i+8])),2)) for i in range(0,len(bits),8))
    return bitsasmsg

def bitfield(n): #returns array of bits from byte value
    return [int(digit) for digit in bin(n)[2:]] # [2:] to chop off the "0b" part

def intasbits(num,m): #returns array of bits from integer value
    """Convert a positive integer num into an m-bit bit vector"""
    return numpy.array(list(numpy.binary_repr(num).zfill(m))).astype(numpy.int8)

#print(intasbits(2,32))
#print(len(intasbits(2,32)))

def bittobytes(msgasbits, bytesize): #return byte value of bits given a bytesize as integer(padding)
    out = 0
    for bit in msgasbits:
        out = (out << 1) | bit
        #print(out)
    return out.to_bytes(bytesize, byteorder='big')

def bitsasint(bitArr): #return array of bits as integer
    return int("".join(str(x) for x in bitArr), 2)

def encryptmsg(plaintext, key): #AES encryption
    # key must be bytes, so we convert it
    key = key.encode('utf-8')
    aes = pyaes.AESModeOfOperationCTR(key) #AES COUNTER MODE
    ciphertext = aes.encrypt(plaintext) #plaintext is encrypted as ciphertext created as byte value
    return ciphertext
    # show the encrypted data
    #print (ciphertext)

def decryptmsg(msgasbits, key, bytesize): #AES decryption
    # DECRYPTION
    # CRT mode decryption requires a new instance be created
    #print(int.from_bytes(ciphertext,byteorder = 'big'))
    # key must be bytes, so we convert it
    key = key.encode('utf-8')
    msgasbytes = bittobytes(msgasbits, bytesize) #converts stored array of bits back into bytes to be decrypted
    aes = pyaes.AESModeOfOperationCTR(key) #AES COUNTER MODE
    #print(test1 == ciphertext)
    decrypted = aes.decrypt(msgasbytes).decode('utf-8'); #decrypted from byte ciphertext back to original string message
    #print(testout)
    return decrypted

# A 256 bit (32 byte) key
'''
key = "This_key_for_demo_purposes_only!"
plaintext = "Text may be any length you wish, no padding is required"
ciphertext = encryptmsg(plaintext, key)
print(ciphertext)
msgasbits = bitfield(int.from_bytes(ciphertext,byteorder = 'big'))
print(msgasbits)
decrypted = decryptmsg(msgasbits, key, len(ciphertext))
print(decrypted)
print(key)
'''
#print(msgasbits)

#msg = 'yullo'
#msgasbits = tobits(msg)

#print(chr(0))
