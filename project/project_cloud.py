import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")


book1 = open("Beyond_the_Wall_of_Sleep.txt", encoding="UTF-8")
book2 = open("The_Project_Gutenberg_eBook_of_Pride_and_Prejudice_by_Jane_Austen.txt", encoding="UTF-8")
english_stop = stopwords.words('english')

list_of_book1 = book1.read().lower().split()

list_of_book2 = book2.read().lower().split()

counter = int(0)

list_of_book1 = list(set(list_of_book1))
list_of_book2 = list(set(list_of_book2))

list_of_common_word = []
for i in range(0, len(list_of_book1), 1):
    if list_of_book1[i] in list_of_book2 and (list_of_book1[i] not in english_stop):
        counter += 1
        list_of_common_word += [list_of_book1[i]]

print("the common word is : ", list_of_common_word, sep="\n")
print("the number of common word is = :", counter)
