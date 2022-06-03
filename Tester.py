from StreamCipher import calcDiffusion, streamCipher

key = 'Jack of all trades is a master of none'

userMessage = input("Input your message: ")

encryption = streamCipher(userMessage, key)

print(encryption)

print(calcDiffusion(userMessage, encryption))