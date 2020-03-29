import hashlib
import random
import time



######### File Format #########
### HEADER {9+sn bytes} ###
# [] cleared {1 bit}, version {3 bits}, name length (sn) {4 bits}
# [] name bytes {sn bytes}
# [] creation timestamp {4 bytes}
# [] last playied timestamp {4 bytes}
### BODY {22+sn+ec*(11+ed)+bc*(11+dl) bytes} ###
# [] type {1 byte}
# [] width {2 bytes}
# [] height {1 byte}
# [] start X pos (between 1-16) {4 bits}, end X pos (between 1-16) {4 bits}
# [] start Y pos {1 byte}
# [] end Y pos {1 byte}
# [] entity count (ec) {4 bytes}
# {
#   [] entity id {4 bytes}
#   [] entity X pos {2 bytes}
#   [] entity Y pos {1 byte}
#   [] entity data length in bytes (ed) {4 bytes}
#   [] entity data {ed bits}
# }*
# [] block count (bc) {4 bytes}
# {
#   [] block id {4 bytes}
#   [] block X pos {2 bytes}
#   [] block Y pos {1 byte}
#   [] block data length in bytes (dl) {4 bytes}
#   [] block data {dl bits}
# }*
### END {16 bytes} ###
# [] md5 of all previous bytes {16 bytes}
###############################



CLEARED=1
VERSION=0
NAME_LENGTH=9
NAME="World 1-1"
C_TIMESTAMP=int(round(time.time()*1000))
LP_TIMESTAMP=int(round(time.time()*1000))+int(random.randint(1000,100000000))+1000
TYPE=0
WIDTH=300
HEIGHT=50
START_X_POS=5
START_Y_POS=13
END_X_POS=10
END_Y_POS=13
ENTITY_COUNT=1
ENITY_DATA=b"\x00\x00\x00\x00\x00\x3c\x12\x00\x00\x00\x01\x01"
BLOCK_COUNT=39
BLOCK_DATA=b"\x00\x00\x00\x00\x00\x3b\x11\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x01\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x00\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x02\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x03\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x04\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x05\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x06\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x07\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x08\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x09\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x0a\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x0b\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x0c\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x17\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x00\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x01\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x02\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x03\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x04\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x05\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x06\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x07\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x08\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x09\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0a\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0b\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0c\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0d\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0e\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x0f\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x10\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x11\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x12\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x13\x0d\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x13\x0c\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x13\x0b\x00\x00\x00\x00"+b"\x00\x00\x00\x00\x00\x13\x0a\x00\x00\x00\x00"+b"\x00\x00\x00\x01\x00\x05\x0b\x00\x00\x00\x00"



with open("0.ld","wb") as f:
	f.write((CLEARED<<7|VERSION<<4|NAME_LENGTH).to_bytes(1,byteorder="big",signed=False))
	f.write(bytes(NAME,"utf-8"))
	f.write(C_TIMESTAMP.to_bytes(8,byteorder="big",signed=False))
	f.write(LP_TIMESTAMP.to_bytes(8,byteorder="big",signed=False))
	f.write(TYPE.to_bytes(1,byteorder="big",signed=False))
	f.write(WIDTH.to_bytes(2,byteorder="big",signed=False))
	f.write(HEIGHT.to_bytes(1,byteorder="big",signed=False))
	f.write((START_X_POS<<4|END_X_POS).to_bytes(1,byteorder="big",signed=False))
	f.write(START_Y_POS.to_bytes(1,byteorder="big",signed=False))
	f.write(END_Y_POS.to_bytes(1,byteorder="big",signed=False))
	f.write(ENTITY_COUNT.to_bytes(4,byteorder="big",signed=False))
	f.write(ENITY_DATA)
	f.write(BLOCK_COUNT.to_bytes(4,byteorder="big",signed=False))
	f.write(BLOCK_DATA)
	f.flush()
	with open("0.ld","rb") as f2:
		h=hashlib.md5(f2.read())
	f.write(h.digest())