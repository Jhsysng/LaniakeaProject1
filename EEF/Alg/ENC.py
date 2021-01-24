class FileEnc():
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
        
    def encrypt_file(self, filename,blocksize=65536):
        filesize=path.getsize(filename)
        