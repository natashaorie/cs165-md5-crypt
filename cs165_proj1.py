from hashlib import md5
import string
import threading
import queue
import time

salt = 'hfT7jp2q'
passHash = 'Csc6Kyx43efmL0sIdsin7'
# passwd = 'abcdef'
magic = '$1$'
base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
passBase = "abcdefghijklmnopqrstuvwxyz"

#-------------------------------------------------------------------
def queuePasswords(q):
	testPasswd = ['a','a','a','a','a','a']

	for i in range(0, len(passBase)):
		testPasswd[0] = passBase[i]

		for i in range(0, len(passBase)):
			testPasswd[1] = passBase[i]

			for i in range(0, len(passBase)):
				testPasswd[2] = passBase[i]

				for i in range(0, len(passBase)):
					testPasswd[3] = passBase[i]

					for i in range(0, len(passBase)):
						testPasswd[4] = passBase[i]

						for i in range(0, len(passBase)):
							testPasswd[5] = passBase[i]
							empty = ''
							# print(empty.join(testPasswd))
							q.put(empty.join(testPasswd))	


#-------------------------------------------------------------------
def crackPasswords(q):
	encoding = ''

	while(encoding != passHash):
		if(q.empty()):
			continue
		testPasswd = q.get()
		
		t0 = time.time()
		encoding = md5_crypt(testPasswd)
		t1 = time.time()
		print("Password throughput: " + str(3/(t1-t0)) + " passwords/sec")

	print("Cracked password: " + encoding)




#-------------------------------------------------------------------
def md5_crypt(passwd):
	altSum = md5((passwd + salt + passwd).encode())
	intSum = md5((passwd + magic + salt).encode())

	if(altSum.digest_size > len(passwd)): # add len(passwd) bits from altSum to intSum
		intSum.update((altSum.digest()[:len(passwd)]))

	length = "{0:b}".format(len(passwd)) # get len(passwd) in bits
	length = length[::-1]

	for c in length: # if bit is set, append NULL bit, else append first byte of passwd
		if(c == '0'):
			intSum.update(passwd[0].encode())

		else:
			intSum.update(b'\x00')

	# loop 1000 times
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

	while(i < 16): # reorder bytes and convert to binary
		binary = "{0:b}".format(currIntSum.digest()[reorder[i]])
		leastSigBits = 8 - len(binary)
		reordIntSum.append('0'*leastSigBits + binary)

		i += 1

	reordIntSum = ''.join(reordIntSum)

	# regroup bits into group of 2, then groups of 6 (22 groups total/128 bits)
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

	regroup = regroup[::-1] # reverse so we can read from least signifigant bit

	for i, r in enumerate(regroup): # convert new groups to decimal
		regroup[i] = int(r,2)

	encoding = '' # use decimal nums to index base64 set and complete encoding
	for r in regroup:
		encoding += base64[r]

	# print(encoding)
	return encoding

#-------------------- main --------------------------------------
q = queue.Queue()

threads = []

t = threading.Thread(target=queuePasswords,args=(q,))
threads.append(t)
t.start()

for i in range(0,3):
	t = threading.Thread(target=crackPasswords, args=(q,), daemon=True)
	t.start()
	threads.append(t)


print(threads)




