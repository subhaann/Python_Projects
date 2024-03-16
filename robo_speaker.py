import os

def main():
    print("Welcome to tece created by subhan")
    while True:
        word = input('Enter text: ')
        if word == 'q':
            break
        command = f" echo {word}" #say command only work in mac
        os.system(command)
      
if __name__ == "__main__":
    main()
   