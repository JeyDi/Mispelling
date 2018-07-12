import os

#Viterbi prompt single word check
def viterbi_check(model,repeat=True):
    while(repeat):
        try_word = input("\nViterbi correction check for test \nWrite 0 if you want to exit\nPlease enter a word to test the correction: ")
        if(try_word.strip() == "0"):
            repeat = False
        elif(try_word.isalpha()):
            repeat = True
            print("Viterbi results for " + try_word)
            print("".join(model.viterbi(list(try_word))))
        else:
            print("Error validating the input string\nPlease insert only characters\nPlease retry\n")
    
    return 0

#Word correction function for the GUI call
def word_correction(model,word):
    result = model.viterbi(word)
    return result


#File correction function to correct a txt file
def file_correction(model,input_file):
    result = ""
    text = ""
    
    try:
        file = open(input_file, 'rt',encoding='UTF-8')
        text = file.read()
        file.close()
    except FileNotFoundError:
        print("File not found, please insert a valid one")

    for i in text:
        result = result + " " + model.viterbi(i)

    #Remove the first empty space
    result.strip()

    print("File corrected")
    return result
