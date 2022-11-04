def main():
    outfile=open('C:/Users/choul/Documents/UTA/INSY 3300/num_list.txt','w')
    for i in range(1,101):
        outfile.write(str(i)+"\n")

    outfile.close()

main()

