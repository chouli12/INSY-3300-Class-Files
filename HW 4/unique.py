#define main function
def main():
    words = {"management.", "name", "been", "later,", "canceled,", "is", "Eastern,", "delay", "Eight", "1,820", "at", "it", "1867", "official", "world", "and", "company,...."}

    infile = open("text2.txt", "r")
    for line in infile:
        for words in line.split():
            if words in line: print(words)

    infile.close()

main()

