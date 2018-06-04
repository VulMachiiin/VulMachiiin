import time
import math

def print_log(message, leading_space=0):
    log = open('robotconnectionlog.txt', 'a')
    log.write('{} - {}'.format(time.asctime(), pad_string(message, leading_space, string_end='\n')))
    log.close()

def print_padded(message, leading_space=0):
	print(pad_string(message, leading_space))

def pad_string(string, leading_space=0, string_end=''):
	return '{:>{space}}'.format(string + string_end, space = leading_space + len(string))

# elegant pairing function by matthew szudzik
def elegant_pair(coor_tuple):
    coor_tuple_x = coor_tuple[0]
    coor_tuple_y = coor_tuple[1]
    return (coor_tuple_x * coor_tuple_x + coor_tuple_y) if (coor_tuple_x >= coor_tuple_y) else (coor_tuple_y * coor_tuple_y + coor_tuple_x)

def elegant_unpair(z):
    sqrtz = math.floor(math.sqrt(z))
    sqz = sqrtz * sqrtz
    return (sqrtz, z - sqz - sqrtz) if ((z - sqz) >= sqrtz) else (z - sqz, sqrtz)
