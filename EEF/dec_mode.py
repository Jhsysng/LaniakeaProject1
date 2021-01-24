from EEF.Alg.AESEnc import fileAES


class dec():
    def __init__(self):
        print("\n")
        print("파일명입력")
        name = input()
        print("key 입력")
        try:
            key = input()
        except ValueError as e:
            print("키가 틀립니다. error code 001:")
            print(e)
            return
        paes = fileAES(key, None)
        paes.decrypt_file(name)
