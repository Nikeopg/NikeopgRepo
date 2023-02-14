known_words = [input().lower() for i in range(int(input()))]

line_count = int(input())
line_in = [input().lower().split() for i in range(line_count)]

errors = set()

for i in range(len(line_in)):
    for j in range(len(line_in[i])):
        if line_in[i][j] not in known_words:
            errors.add(line_in[i][j])

for x in errors:
    print(x)


"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество

d известных нам слов, после чего на
d строках указываются эти слова. Затем передаётся количество
l строк текста для проверки, после чего
l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
_____________________
Sample Output:
stepic
champignons
the

"""