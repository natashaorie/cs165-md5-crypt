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
print(altSum.hexdigest())

print(altSum.digest_size)
# t = passwd + magic + salt
intSum = md5((passwd + magic + salt).encode())
if(altSum.digest_size > len(passwd)):
	# t = passwd + magic + salt + str((altSum.digest()[:len(passwd)]))
	intSum.update((altSum.digest()[:len(passwd)]))

else:
	print("passwd longer")
	i = 0
	temp = altSum
	while i < len(passwd):
		pass
	t = passwd + magic + salt + passwd[:altSum.digest_size]

print("{0:b}".format(len(passwd)))
sig = 0
length = "{0:b}".format(len(passwd))
length = length[::-1]
for i, c in enumerate(length):
	if(c == '1'):
		# t = t + passwd[i]
		intSum.update(passwd[i].encode())
		sig = 1
	else:
		# if(sig == 1):
		# 	break
		# t = t + '0'
		intSum.update('x00'.encode())

# print(t)	
# intSum = md5(t.encode())
print(intSum.digest())
print(intSum.hexdigest())

i = 0
while(i < 1000):
	t = ''

	if(i % 2 == 0):
		# t += intSum
		pass
		
	if(i % 2 != 0):
		t += passwd

	if(i % 3 != 0):
		t += salt

	if(i % 7 != 0):
		t += passwd

	if(i % 2 == 0):
		t += passwd

	if(i % 2 != 0):
		# add intSum
		pass

	intSum = md5(t.encode())
	i += 1


# for l in letters:

# result = hashlib.md5(b'GeeksforGeeks') 
# result = md5(b'GeeksforGeeks')
 

# printing the equivalent byte value. 
# print("The byte equivalent of hash is : ", end ="") 
# print(result.digest())
# print(result.hexdigest())
