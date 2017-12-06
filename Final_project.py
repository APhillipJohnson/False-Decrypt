'''
Phillip Johnson
ESOC 488
Final Project
Single Encrypt, Double Decrypt
Purpose: Create a program that encrypts a file, and assigns a key. 
		This will offer two possible decryptions, a partial or full.
		To accomplish this, the Full Decryption key will be as designated 
		upon encryption. The Partial Decryption key will be the Full
		Decryption key, with 0's added to the end until you have 5 digits.
	


To DO:  
	1. Change encryption to rotating cypher incrementing up by one for each character
		in the file, with rollover	
	2. Add error catch for 'out of range'
	3. Try to fix 'large prime' issue.
	4. Remove 'limit' for key input length, and just call if its len > 2.
	5. Add functionality for .doc type.
	6. Create GitHub repo for project, Modify proposal to a Purpose document.
	7. Update display prompt and input functions when running from IDLE.
		
'''

import string
import random
catchset=[]
key_list=[]
decrypt_key=[]



def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
prime_bin = [i for i in range(0,100) if isPrime(i)]


while len(key_list)<2:
	key_list.append(random.choice(prime_bin))



#print(catchset)

file_breakout = []
full_D_key=[] 
#full_D_key=1
encrypted_file=[]
decrypted=[]

if key_list[0]==59 or key_list[0] == 0:
	full_D_key=key_list[1]
else:
	full_D_key=key_list[0]


def Encode_function(filename, writefile):
	file = open(filename, 'r', encoding='utf-8')
	final_file = open(str(writefile), 'w', encoding='utf-8')
	for line in file:
		line = line.split()
		#print(line)
		for word in line:
			#print(word)
			for i in range(len(word)):
				file_breakout.append(word[i])
				#print(word[i])
			file_breakout.append(' ')
	#print(file_breakout)
	#print('plaintext file ^^^')
	#print(len(catchset))
	for i in range(len(file_breakout)):
		x = ord(file_breakout[i]) + full_D_key
		encrypted_file.append(chr(x))

	
	final_file.write(''.join(encrypted_file))
	#print(''.join(encrypted_file))
	#print('^^^encrypted^^^')
	
	
	
def Decode_function(filename, keyinput, writefile):
	dec_key=int(keyinput)
	if len(keyinput)==5:
		dec_key=keyinput[0:2]
		file = open(filename, 'r', encoding='utf-8')
		Decrypted_file = open(writefile, 'w', encoding='utf-8')
		file_breakout=[]
		#Full decrypt function
		for line in file:
			line = line.split()
			#print(line)
			for word in line:
				#print(word)
				for i in range(len(word)):
					file_breakout.append(word[i])
					#print(word[i])
				file_breakout.append(' ')
		#print(file_breakout)
		#print(len(catchset))
		
		split=len(file_breakout)/2
		split=int(split)
		#print(split)
		file_breakout=file_breakout[0:split]
			
		for i in range(len(file_breakout)-1):
			#print(ord(file_breakout[i]))
			x = ord(file_breakout[i]) - int(dec_key)
			#print(x)
			#print(file_breakout[i])
			if ord(file_breakout[i]) != ' ':
				decrypted.append(chr(x))
		
		#print(''.join(decrypted))
		#print('decrypted ^^^^^^')	
		for i in range(len(decrypted)):
			if decrypted[-i] == '.':
				printer=''.join(decrypted[0:-i+1])
				Decrypted_file.write( printer + '.' + ' End of File')
				return None
				
	else:
		file = open(filename, 'r', encoding='utf-8')
		Decrypted_file = open(writefile, 'w', encoding='utf-8')
		file_breakout=[]
		#Full decrypt function
		for line in file:
			line = line.split()
			#print(line)
			for word in line:
				#print(word)
				for i in range(len(word)):
					file_breakout.append(word[i])
					#print(word[i])
				file_breakout.append(' ')
		#print(file_breakout)
		#print(len(catchset))
		
			
			
		for i in range(len(file_breakout)-1):
			#print(ord(file_breakout[i]))
			x = ord(file_breakout[i]) - dec_key
			#print(x)
			#print(file_breakout[i])
			if ord(file_breakout[i]) != ' ':
				decrypted.append(chr(x))
		
		#print(''.join(decrypted))
		#print('decrypted ^^^^^^')	
		Decrypted_file.write(''.join(decrypted))
#Encode_function('encrypt_test.txt')
#Decode_function('encrypted.txt')


Encode_input=input('Would you like to encrypt a file?')
if Encode_input.lower() == 'yes':
	print("Your decrypt key is '" + str(full_D_key) + "'. Please keep this in a safe location as it will not appear again")
	file_input = input('Please enter filename')
	writefile= input('Please input output filename')
	Encode_function(file_input, writefile)
	print('Your file has been successfully encrypted')
else: 
	decrypt_input=input('Would you like to decrypt a file?')
	if  decrypt_input.lower() == 'yes':
		decrypt_file_input= input('please input filename')
		decrypt_key_input= input('Please input your 5 character key')
		writefile= input('Please input output filename')
		Decode_function(decrypt_file_input, decrypt_key_input, writefile)
	else:
		print('Session Terminated')
	print('Your file has been successfully encrypted')
