import requests
from heandlers import *
from time import sleep

def main():
    while True:
        inic_client()
        client_command()
                    

if __name__=='__main__':
    try:
        main()
    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        sleep(3)
        main()