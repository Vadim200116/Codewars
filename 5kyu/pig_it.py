def pig_it(text):
    words=text.split(' ')
    return " ".join([word[1:]+word[:1]+"ay" if word.isalpha() else word for word in words ])


print(pig_it("Hello world !"))


