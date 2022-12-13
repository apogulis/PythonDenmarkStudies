# This program calculates the average word length in a text file (Example: text.txt)

def main():
    with open(input('Enter file name: '), 'r') as f:
        words = [len(word) for line in f for word in line.rstrip().split(" ")]
        words_average = float(sum(words)) / float(len(words))

    print('Average word length: ', format(words_average, '.2f'))
    f.close()


# Calling the main function
main()
