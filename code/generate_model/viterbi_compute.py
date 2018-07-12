

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
