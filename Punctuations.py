import string
def remove_punctuation(sentence):
    punctuations = string.punctuation
    result=" "
    for character in sentence:
        if character not in punctuations:
            result = result + character
    print("original :",sentence)
    print("cleaned  :",result)

sentence = input("enter a sentence:")
remove_punctuation(sentence)    