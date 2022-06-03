def streamCipher(message, key):
    encrypted = ''

    binaryKey = ''.join(format(ord(i), '08b') for i in key)
    binaryKey = str(binaryKey)

    binaryMsg = ''.join(format(ord(i), '08b') for i in message)
    binaryMsg = str(binaryMsg)

    while(len(binaryKey) < len(binaryMsg)):
        binaryKey += binaryKey

    for i in range(len(binaryMsg)):
        encrypted += (encryptAlgo(binaryMsg, binaryKey, i))

    return encrypted


def encryptAlgo(message, key, i):

    

    if(message[i] != key[i]):
        return '1'

    return '0'
    

def calcDiffusion(original, encryption):
    binaryMsg = ''.join(format(ord(i), '08b') for i in original)
    original = str(binaryMsg)


    lenMsg = len(original)
    numSimilarity = 0

    for i in range(lenMsg):
        if(original[i] == encryption[i]):
            numSimilarity += 1
    
    return round((lenMsg-numSimilarity)/lenMsg * 100, 2)