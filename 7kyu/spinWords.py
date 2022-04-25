# def spinWords(str):
#     words=str.split()
#     for word in words:
#         print(len(word))
#         if len(word)>4:
#             str=str.replace(word,word[::-1])
#     return str

def spin_words(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())