from hashlib import md5
import string
# import thread

# letters = string.ascii_lowercase
salt = 'hfT7jp2q'
passHash = 'Csc6Kyx43efmL0sIdsin7'
passwd = 'abcdef'
magic = '$1$'
base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

altSum = md5((passwd + salt + passwd).encode())
# altSum = md5()
# altSum.update(passwd)
# altSum.update(salt)
# altSum.update(passwd)

print("The byte equivalent of hash is : ", end ="") 
print(altSum.digest())

# print(altSum.digest_size)
# t = passwd + magic + salt
intSum = md5((passwd + magic + salt).encode())
if(altSum.digest_size > len(passwd)):
	# t = passwd + magic + salt + str((altSum.digest()[:len(passwd)]))
	# temp = altSum.digest()
	# print(temp[0])
	intSum.update((altSum.digest()[:len(passwd)]))
	# intSum.update((altSum.hexdigest()[:len(passwd)*2]).encode())

else:
	print("passwd longer")
	i = 0
	temp = altSum
	while i < len(passwd):
		pass
	t = passwd + magic + salt + passwd[:altSum.digest_size]

print(intSum.digest())
print(intSum.hexdigest())

# for c in str(intSum.digest()):
# 	print("{:02x}".format(ord(c)))

print("{0:b}".format(len(passwd)))
sig = 0
length = "{0:b}".format(len(passwd))
length = length[::-1]

# for i, c in enumerate(length):
# 	if(c == '0'):
# 		# t = t + passwd[i]
# 		intSum.update(passwd[i].encode())
# 		sig = 1
# 	else:
# 		# if(sig == 1):
# 		# 	break
# 		# t = t + '0'
# 		intSum.update('x00'.encode())

for c in length:
	if(c == '0'):
		intSum.update(passwd[0].encode())

	else:
		intSum.update(b'\x00')

# print(t)	
# intSum = md5(t.encode())
print(intSum.digest())
print(intSum.hexdigest())
# for c in str(intSum.digest()):
# 	print("{:02x}".format(ord(c)))


i = 0

currIntSum = intSum
nextIntSum = md5()
while(i < 1000):
	# print(currIntSum.hexdigest())
	# t = ''

	if(i % 2 == 0):
		nextIntSum.update(currIntSum.digest())
		
	if(i % 2 != 0):
		nextIntSum.update(passwd.encode())

	if(i % 3 != 0):
		nextIntSum.update(salt.encode())

	if(i % 7 != 0):
		nextIntSum.update(passwd.encode())

	if(i % 2 == 0):
		nextIntSum.update(passwd.encode())

	if(i % 2 != 0):
		nextIntSum.update(currIntSum.digest())

	currIntSum = nextIntSum
	nextIntSum = md5()

	# intSum = md5(t.encode())
	i += 1


print(currIntSum.digest())
print(currIntSum.hexdigest())
	
print("{0:b}".format(currIntSum.hexdigest()))
length = "{0:b}".format(currIntSum.hex digest())
length = length[::-1]
# for l in letters:

# result = hashlib.md5(b'GeeksforGeeks') 
# result = md5(b'GeeksforGeeks')
 

# printing the equivalent byte value. 
# print("The byte equivalent of hash is : ", end ="") 
# print(result.digest())
# print(result.hexdigest())
