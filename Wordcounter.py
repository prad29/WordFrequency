import requests
from bs4 import BeautifulSoup
import operator


def start(url):                                             # This function is the simple webcrawler definition
    wordlist=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code,'html.parser')
    for each_text in soup.findAll('blockquote',{'class':'testimonial'}):
        content=each_text.string
        words=content.lower().split()
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)                            #Calling of the second function which removes any special character 
                                                            # from the created list of words



def clean_wordlist(wordlist):                              #replaces every special character present in a word with a 'space'
    clean_list=[]
    for word in wordlist:
        symbols='!@#$%^&*()_-+={[}]|\;:"<>?/.,'
        for i in range (0,len(symbols)):
            word=word.replace(symbols[i],'')
        if len(word)>0:
            clean_list.append(word)
    create_dictionary(clean_wordlist)                      #Calls the third function


def create_dictionary(clean_wordlist):                     #This function takes every word in the list and counts the number of times
                                                           #it occurs in the list and then it counts its frequency and packs it into
                                                           #a Frequency Chcecker Dictionary
                                                           #The Frequency of the most word determines the subject of the talk
    word_count={}
    for word in clean_wordlist:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
                                                            #BUT IF WE WANT A SORTED WORD COUNTER ARRAY
    for key,value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print (key,value)

start("http://inventwithpython.com/")
