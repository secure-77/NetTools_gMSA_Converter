import binascii
from Cryptodome.Hash import MD4
import argparse
import sys


parser = argparse.ArgumentParser(description='Convert gMSA Password Hex (retrieved from NetTools) into MD4 / HT Hash ')
parser.add_argument('-s','--no-swap', help='dont swap endianness',required=False, dest='swap', action='store_true')
parser.add_argument('-i','--input', help='Hex to convert', required=True)
parser.set_defaults(swap=False)

args = parser.parse_args()
noswap = args.swap


#reading Hex
orig = args.input
#delete white spaces
orig = orig.replace(" ", "")


if noswap:
    print('no endianness swap')
    swap = orig
else:
    swap =''.join(sum([(c,d,a,b) for a,b,c,d in zip(*[iter(orig)]*4)], ()))

#convert hex to binary
raw = binascii.unhexlify(swap)

#create md4 / NT Hash
hash = MD4.new ()
hash.update (raw)
passwd = binascii.hexlify(hash.digest()).decode("utf-8")

print('\nmd4 / NT Hash: ')
print(passwd)