# main
# commer ver x.x.x prototype ver x.x.x.x
# x.0.0 version 0.x.0 patch ver 0.0.x sub patch ver
# UI ver0.0.2.1
# prototype V0.0.4.003
from EEF.enc_mode import enc
from EEF.dec_mode import dec
from tkinter import *

root=Tk()
root.title("Laniakea")
    
root.mainloop()
if __name__ == '__main__':

    print('-------------------------------')
    print("File encrypt Program")
    print('version prototype v0.0.3.001')
    # print('-------------------------------')
    while True:
        print('-------------------------------')
        print("명령어 입력")
        print('-h help -en encrypt -de decrypt')
        print('-q quit')
        print('-------------------------------')

        command = input()
        if command == '-en':
            enc()
        elif command == '-de':
            dec()
        elif command == '-h':
            print('준비중..')
            break
        elif command == '-q':
            break
        else:
            print('다시입력 press Enter key..')