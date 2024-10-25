# def check_word_count(given_word):
#     if given_word not in word_trash:
#         print("0, the word doesn't appear anywhere.")
#         return
#     else:
#         count = 0
#         for word in word_trash:
#             if word == given_word:
#                 count += 1
#         return count

# text_list = [
#     "I love c programming",
#     "I dont think muhc of java, maybe alitle bit of c. How was your day?",
#     "I like scala",
#     "what is scala",
#     "c is in java and the c is in scala the house ",
# ]


# def word_list(list):
#     word_trash = []
#     for line in list:
#         temp_list = line.split(" ")
#         for item in temp_list:
#             word_trash.append(item)
#     return word_trash


# word_trash = word_list(text_list)


# def check_word_count(word_list):
#     word_list = sorted(word_list)
#     for word in word_list:
#         if word in word_trash:
#             count = 0
#             for item in word_trash:
#                 if word == item:
#                     count += 1
#             print(word, count)
#         else:
#             continue


# check_list = ["java", "scala", "c", "house"]
# check_word_count(check_list)


sample_dict = {"name": "omar", "age": "10"}

for item, value in sample_dict.items():
    print(item, value)
