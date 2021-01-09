from EEF.Alg.AESEnc import fileAES


class enc():
    def __init__(self):
        print("파일명 입력")
        name = input()
        # key='run for your life'
        print("key 입력")
        key = input()
        paes = fileAES(key, None)
        paes.encrypt_file(name)