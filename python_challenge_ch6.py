# python challenge ch6

# 1 print every character in the string 'camus'

author = 'camus'

print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

# 2 write a program that collects two strings from a user, inserts them into the string 'yesterday i wrote a [response_one]. I sent it to [response_two' and prints a new string

response_one = input('What did you write?')
response_two = input("where did you send it?")

answer= 'yesterday I wrote a {}. I sent it to {}'.format(response_one, response_two)

print(answer)

# 3 use a method to make the string 'aldous Huxley was born in 1894' grammatically correct by capitalizing the first letter in the sentence

sentence = 'aldous Huxley was born in 1894.'.capitalize()


print(sentence)

# 4 take the string 'where now? who now? when now?' and call a method that returns a list that looks like ['where now?', 'who now?','when now?']

message = 'where now?, who now?, when now?'.split(',')

print(message)

# 5 take the list ['the', 'fox', 'jumped', 'over', 'the', 'fence', '.'] & turn it into a grammatically correct string. There should be a space between each word, but no space between the word
# fence and the period that follows it

book = ['the', 'fox', 'jumped', 'over', 'the', 'fence', '.']

book = " ".join(book)

book = book[0:-2] + '.'
print(book)

# 6  replace every instance of 's' in 'a screaming comes across the sky' with a dollar sign

msg = 'a screaming comes across the sky'.replace('s','$')

print(msg)

# 7 use a method to find the first index of the character 'm' in the string 'hemingway'[

author_1 = 'hemingway'.index('m')


print(author_1)

# 8 find dialogue in your favorite book (containg quotes) and turn it into a string

print('I can\'t find a quote at the moment so I am freestyling \"this is my quote\" that was easy.')

#9 create the string 'three three three' using concatenation, and then again using multiplication

msg_1 = 'three'

msg_2 = 'three' + ' three' + ' three'


print(msg_1 * 3)
print(msg_2)

# 10 slice the string 'it was a bright cold day in April, and the clocks were striking thirteen' to only the characters before the comma

sentence_1 = 'It was a bright cold day in April, and the clocks were striking thirteen'

new_sentence = sentence_1[0:33]

print(new_sentence)
