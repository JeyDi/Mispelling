import os 
import re 
import math 
import random 
import sys
from random import randint 
from string import ascii_letters 
from os import path, listdir
from configparser import ConfigParser
 
pathname = os.path.dirname(sys.argv[0])
config = ConfigParser()
config.read( pathname + '/config.ini')
 
#Function to basic clean and preprocess input string or text 
def clean_text(text): 
     
    #Some usefull regexp 
    MENTIONS = re.compile(r'@[^\s]*') 
    URL = re.compile(r'htt[^\s]*') 
    SYMBOLS = re.compile(r'[^A-Za-z ]') 
    RT = re.compile(r'RT ') 
    SPACE = re.compile(r'\s+') 
 
    #Text preprocessing using the REGEXP 
    text = MENTIONS.sub(' ', text)  # Mentions 
    text = URL.sub(' ', text)  # URLs 
    text = SYMBOLS.sub(' ', text)  # Symbols 
    text = RT.sub(' ', text)  # RT 
    text = SPACE.sub(' ', text) 
    result_text = text.strip()  # spaces at head or tail 
 
    return result_text 
 
 
#Perturb the word by a certain percentage 
def perturb_word(word,percentage): 
     
    string_list = list(word) 
    string_count = len(string_list) 
    string_to_perturb = int(math.floor(string_count*percentage/100)) 
 
    for s in range(string_to_perturb): 
        string_index = randint(0,string_count-1) 
        string_list[string_index] = random.choice(ascii_letters) 
     
    #Re assemble the string 
    word = "".join(string_list) 
 
    return word 
 
 
#Main function for the perturbation algorithm 
def perturb(input_words,words_percentage=10,string_percentage=10): 
    result_text = "" 
    input_words_list = input_words.split() 
    words_count = len(input_words_list) 
    words_to_perturb = int(math.floor(words_count*words_percentage/100)) 
 
    #Generate a new list with the words for safety check 
    input_words_list_perturbed = input_words_list 
    words_dict = {} 
 
    for i in range(words_to_perturb): 
         
        words_count = len(input_words_list_perturbed) 
        word_index = randint(0,words_count-1) 
        word = input_words_list[word_index] 
        #delete the word from the list 
        input_words_list_perturbed.pop(word_index) 
 
        #Perturb the word 
        word = perturb_word(word,string_percentage) 
 
        #Add the word in the perturbed dictionary     
        words_dict[word_index] = word 
 
    #recreate the list of words 
    for key,value in words_dict.items(): 
        input_words_list_perturbed.insert(key,value) 
 
    result_text = input_words_list_perturbed 
 
    return result_text 
 
 
#Word perturbation main method 
#If you call the method with an input_file --> the program start perturbation to this file 
#If you call the method with string --> the program start perturbation the string text 
#If you set clean = 1 --> the program start to clean and preprocess the text before the perturbation 
#Default percentage for the perturbation = 10% 
def word_perturbation(input_file = None, string = None, clean = 0, words_percentage = 10, string_percentage = 10): 
    input_words = "" 
    result_text = "" 
 
    #Start perturbation the file 
    if(input_file is not None): 
        print("Reading the file") 
        with open (input_file, "r",encoding="utf-8") as file: 
            input_words = file.readline() 
 
        #Clean the text and perturb the string 
        if(clean == 1): 
            print("Start cleaning and preprocessing the input text file..") 
            input_words = clean_text(input_words) 
            result_text = perturb(input_words,words_percentage,string_percentage) 
            print("Clean input file perturbation succesful!") 

            #Export again to file 
            file_name, _ = path.splitext(path.basename(input_file)) 
            export_path = export_result(file_name,result_text) 

            return export_path 
         
        #Perturb the string without the cleaning 
        elif(clean == 0): 
            result_text = perturb(input_words,words_percentage,string_percentage) 
            print("Plain input file perturbation successful!") 

            #Export again to file 
            file_name, _ = path.splitext(path.basename(input_file)) 
            export_path = export_result(file_name,result_text) 

            return export_path 
         
        else: 
            print("\nERROR! Wrong method call, please set clean = 0 or clean = 1..\n") 
 
    #Start perturbation the string 
    elif(string is not None): 
        result_text = perturb(string,words_percentage,string_percentage) 
        print("String Perturbation succesful!") 
        return result_text 
 
    #Error 
    else: 
        print("\nERROR! Generate word perturbation error, please insert a string or a valid file\n") 
        return result_text 
 

 
#Function to export the perturbation result into a file txt 
def export_result(filename,result): 
    result_path = config["config"]["perturbed_tweets_folder"]
     
    result_path = path.join(result_path,filename + ".txt") 
 
    with open(result_path, "w") as text_file: 
        for i in result: 
            text_file.write("%s " % i) 
 
    print("File cleaned saved") 
 
    return result_path
 
 
# #Functions test 
# #TODO: non usare ASCII CHAR, ma solamente un dizionario di lettere o solo lettere maiuscole e minuscole 
# input_string = "ciao come stai proviamo a fare un test andrea guzzo che succede se aggiungo altre 10 parole al ciclo uff" 
# result = word_perturbation(string=input_string,clean=0,words_percentage=50,string_percentage=50) 
# input_path = ".\\tweets\\cleaned" 
# filename = "clean_realDonaldTrump.txt" 
# input_path = path.join(input_path,filename) 
# print(input_path) 
 
# k = word_perturbation(input_file=input_path,string=None,clean=0,words_percentage=50,string_percentage=50) 
 
# print("Finish..") 
# print(result)