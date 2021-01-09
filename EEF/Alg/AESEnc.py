from Crypto.Cipher import AES
from Crypto.Hash import SHA256 as SHA
import struct
# import pandas as pd
from os import path

class fileAES():
    def __init__(self, keytext, out_filename):
        hash = SHA.new()
        hash.update(keytext.encode('utf-8'))
        key = hash.digest()
        self.key = key[:16]

        iv_text = 'star streaming'
        hash.update(iv_text.encode('utf-8'))
        iv = hash.digest()
        del iv_text
        self.iv = iv[:16]
        self.out_filename = out_filename

    def encrypt_file(self, filename, blocksize=65536):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        filesize = path.getsize(filename)
        if self.out_filename == None:
            fileexp = filename[len(filename)-3: len(filename)]
            fileexp = fileexp.encode()
            print(len(fileexp))
            print(fileexp)
            out_filename = filename[0:len(filename)-4]+'.enc'
        else:
            out_filename = self.out_filename
        with open(filename, 'rb') as origin:
            with open(out_filename, 'wb') as ret:
                ret.write(struct.pack('<Q', filesize))
                ret.write(fileexp)
                ret.write(self.iv)
                # ret.write(fileexp)
                while True:
                    block = origin.read(blocksize)
                    # print(block)
                    if len(block) == 0:
                        break
                    elif len(block) % 16 != 0:
                        block += b'0'*(16 - len(block) % 16)
                        # block = pd.concat(block, '0'*(16-len(block) % 16))
                    ret.write(aes.encrypt(block))
        print('encrypt done')

    def decrypt_file(self, filename, blocksize = 1024):
        with open(filename, 'rb') as origin:
            filesize = struct.unpack('<Q', origin.read(struct.calcsize('<Q')))[0]
            file_exp = origin.read(3)
            file_exp = file_exp.decode()
            print(file_exp)
            iv = origin.read(16)
            aes = AES.new(self.key, AES.MODE_CBC, iv)
            filename = filename[0:len(filename)-3] + file_exp
            # signature code def position
            with open(filename, 'wb') as ret:
                ret.write(aes.decrypt(origin.read(16)))
                while True:
                    block = origin.read(blocksize)
                    if len(block) == 0:
                        break
                    ret.write(aes.decrypt(block))
                ret.truncate(filesize)
        print('decrypt done')