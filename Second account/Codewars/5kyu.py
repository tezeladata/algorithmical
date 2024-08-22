# Moving Zeros To The End
def move_zeros(lst):
    return [i for i in lst if i!=0] + [0 for _ in range(lst.count(0))]

# Simple Pig Latin
def pig_it(text):
    split_text = text.split(' ')
    pig_sentence = ' '
    
    for word in split_text:
        if word in '!.%&?':
            pig_sentence = pig_sentence + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_sentence = pig_sentence + pig_word + ' '
    
    
    return pig_sentence.strip(' ') 