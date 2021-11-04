from Crypto.Hash import keccak

def CalcCommitment(choice, sender):
    print('sender:', sender)
    print('choice:', choice)
    blindingFactor = '17'*32
    print('blindingFactor:', '0x' + blindingFactor)

    buf2Kec = bytes.fromhex(sender) + bytes([choice]) + bytes.fromhex(blindingFactor)
    k = keccak.new(digest_bits=256)
    k.update(buf2Kec)
    print('hash:', '0x' + k.hexdigest().upper())

CalcCommitment(1, '17F6AD8Ef982297579C203069C1DbfFE4348c372')
CalcCommitment(2, '14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C')
