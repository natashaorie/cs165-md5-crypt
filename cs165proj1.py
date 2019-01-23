from hashlib import md5
import string
# import thread

salt = 'hfT7jp2q'
passHash = 'Csc6Kyx43efmL0sIdsin7'
passwd = 'abcdef'
magic = '$1$'
base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

altSum = md5((passwd + salt + passwd).encode())

intSum = md5((passwd + magic + salt).encode())

if(altSum.digest_size > len(passwd)):
	intSum.update((altSum.digest()[:len(passwd)]))

# sig = 0
length = "{0:b}".format(len(passwd))
length = length[::-1]

for c in length:
	if(c == '0'):
		intSum.update(passwd[0].encode())

	else:
		intSum.update(b'\x00')


i = 0
currIntSum = intSum
nextIntSum = md5()

while(i < 1000):
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
	i += 1


i = 0
reorder = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
reordIntSum = []


while(i < 16): # this gets the bytes into ascii i think
	binary = "{0:b}".format(currIntSum.digest()[reorder[i]])
	leastSigBits = 8 - len(binary)
	reordIntSum.append('0'*leastSigBits + binary)

	i += 1


reordIntSum = ''.join(reordIntSum)
# print(len(reordIntSum))

regroup = []
i = 0
j = 2
regroup.append(reordIntSum[i:j])
i = 2
j = 8
while(j <= 128):
	regroup.append(reordIntSum[i:j])
	i += 6
	j += 6


regroup = regroup[::-1]

for i, r in enumerate(regroup):
	regroup[i] = int(r,2)

# print(regroup)

encoding = ''
for r in regroup:
	encoding += base64[r]

print(encoding)


