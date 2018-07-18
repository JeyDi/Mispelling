import os 
import re 
import math 
import random 
import sys
import json
import itertools
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

def change_letter(letter, neighbours):
    
    none_count = 0
    for letter in neighbours:
        if letter == None:
            none_count += 1

    for i in range(0,none_count):
        neighbours.remove(None)

    #neighbours.remove(letter)

    return neighbours[randint(0,len(neighbours)-1)]

#Perturb the word by a certain percentage 
def perturb_word_qwerty(word,percentage): 

    string_list = list(word) 
    string_count = len(string_list) 
    string_to_perturb = int(math.floor(string_count*percentage/100)) 

    layout_file = config["config"]["layout_file"] #"../resources/qwerty_simple.json"

    #Read the json file
    with open(layout_file) as data_file:    
        layout_json = json.load(data_file)


    for s in range(string_to_perturb): 
        string_index = randint(0,string_count-1) 
        string_list[string_index] = change_letter(string_list[string_index],list(itertools.chain.from_iterable(layout_json[string_list[string_index]])))
     
    #Re assemble the string 
    word = "".join(string_list) 
 
    return word 
 
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
def perturb(input_words,words_percentage=10,string_percentage=10, qwerty_perturbation = True): 
    input_words_list = input_words.split(" ") 
    words_count = len(input_words_list) 
    words_to_perturb = int(math.floor(words_count*words_percentage/100)) 
 
    for i in range(words_to_perturb): 
        word_index = randint(0,words_count-1) 
        word = input_words_list[word_index] 
        if (qwerty_perturbation):
            input_words_list[word_index] = perturb_word_qwerty(word,string_percentage) 
        else:
            input_words_list[word_index] = perturb_word(word,string_percentage) 
  
    return input_words_list
 
 
#Word perturbation main method 
#If you call the method with an input_file --> the program start perturbation to this file 
#If you call the method with string --> the program start perturbation the string text 
#If you set clean = 1 --> the program start to clean and preprocess the text before the perturbation 
#Default percentage for the perturbation = 10% 
def word_perturbation(input_file = None, string = None, clean = 0, words_percentage = 10, string_percentage = 10, qwerty_perturbation = True): 
    input_words = "" 
    result_text = "" 
 
    #Start perturbation the file 
    if(input_file != None): 
        print("Reading the file") 
        with open (input_file, "r",encoding="utf-8") as file: 
            input_words = file.readline() 
            file.close()
 
        #Clean the text and perturb the string 
        if(clean == 1): 
            print("Start cleaning and preprocessing the input text file..") 
            input_words = clean_text(input_words) 
            result_text = perturb(input_words,words_percentage,string_percentage, qwerty_perturbation) 
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

    result_path = config["config"]["perturbed_tweets_folder"] #"..\\..\\tweets\\perturbed"

    result_path = path.join(result_path,filename + ".txt") 
 
    with open(result_path, "w") as text_file: 
        for i in result: 
            text_file.write("%s " % i) 
    text_file.close()
 
    return result_path
 
 
# Functions test 

#input_string = "ciao come stai proviamo a fare un test andrea guzzo che succede se aggiungo altre parole al ciclo uff" 
#result = word_perturbation(string=input_string,clean=0,words_percentage=50,string_percentage=50) 
#print(result)
# input_path = "..\\..\\tweets\\cleaned"
# filename = "clean_realDonaldTrump.txt" 
# input_path = path.join(input_path,filename) 
# print(input_path) 
 
# word_perturbation(input_file=input_path,string=None,clean=0,words_percentage=50,string_percentage=50) 
 
# print("Finish..") 