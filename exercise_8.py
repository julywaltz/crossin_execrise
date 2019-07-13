def read_words():
    with open('C:/python_work/crossin_exercises/sensitive_words.txt',
              encoding='UTF-8') as f:
        sensitive_words = f.read().splitlines()
        return sensitive_words


words_input = input('输入:')
sensitive_words = read_words()
for word in sensitive_words:
    if word in words_input:
        words_input = words_input.replace(word, '*' * len(word))
print(words_input)