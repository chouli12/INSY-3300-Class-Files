def main():
    counter = 0
    line = ""
    openfile = input('Please Enter The Name of the File  ')
    file = open(openfile,'r')
    while(counter < 10):
        line= file.readline()
        print(line.rstrip())
        counter+=1
    file.close()

main()


