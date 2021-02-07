n = int(input())

words = {}

for i in range(n):
    word = input()
    if word in words:
        words[word]['ocurrences'] += 1
    else:
        words[word] = {'ocurrences': 1, 'appearance': len(words)}
        
ordered_words = [None]*len(words)
for word, word_dict in words.items():
    ordered_words[word_dict['appearance']] = word_dict['ocurrences']

print(len(words))
for word_ocurrences in ordered_words:
    print(word_ocurrences, end= " ")
