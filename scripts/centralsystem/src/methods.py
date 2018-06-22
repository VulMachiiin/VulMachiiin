import time
import math
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

def print_log(message, leading_space=0):
    log = open('robotconnectionlog.txt', 'a')
    log.write('{} - {}'.format(time.asctime(), pad_string(message, leading_space, string_end='\n')))
    log.close()

def print_padded(message, leading_space=0, border_size=0):
    if border_size != 0:
        print('#{:<{size}}#'.format(pad_string(message, leading_space),  size = border_size - 2))
    else:
        print(pad_string(message, leading_space))

def pad_string(string, leading_space=0, string_end=''):
	return '{:>{space}}'.format(str(string) + string_end, space = leading_space + len(string))

def print_list(name, array):
    print('{}: '.format(name))
    for item in array:
        print_padded(item, 4)

# elegant pairing function by matthew szudzik
def elegant_pair(coor_tuple):
    coor_tuple_x = coor_tuple[0]
    coor_tuple_y = coor_tuple[1]
    return (coor_tuple_x * coor_tuple_x + coor_tuple_y) if (coor_tuple_x >= coor_tuple_y) else (coor_tuple_y * coor_tuple_y + coor_tuple_x)

def elegant_unpair(z):
    sqrtz = math.floor(math.sqrt(z))
    sqz = sqrtz * sqrtz
    return (sqrtz, z - sqz - sqrtz) if ((z - sqz) >= sqrtz) else (z - sqz, sqrtz)

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)).encode()
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
key = b'2r5u7x!A%D*G-KaP'
iv = b'This is an IV456'
cipher = AES.new(key, AES.MODE_CBC, iv)

def encrypt(self, message):
    raw = self.pad(message.encode())
    return b64encode(self.cipher.encrypt(raw))

def decrypt(self, message):
    return self.unpad(self.cipher.decrypt(b64decode(message))).decode()
