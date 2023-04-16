#1. mbox-short.txt faylni oching ushbu fayldagi har bir qatorni “o’qing” va quyidagi ma’lumotga mos keladigan "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008" qatorlarni toping.Keyin esa har bir kiruvchi emal adreslarni va ularning umumiy sonini konsolga chiqaring.Quyidagi masalani yechish uchun matn metodlaridan foydalaning.


# import re
#
# filename = "mbox-short.txt"
# emails = []
#
# with open(filename, "r") as f:
#     for line in f:
#         if line.startswith("From "):
#             match = re.search(r"\b[\w.-]+@[\w.-]+\b", line)
#             if match:
#                 emails.append(match.group(0))
#
# print("Total email addresses:", len(emails))
# print(emails)

#--------------------------------------------------------------------

# 2. romeo.txt faylni oching va undagi har bir qatorni o’qing.Qatordagi har bir so’zni alohida qilib ro’yxatga saqlang unda so’zlar qaytarilmasligi zarur.Undan keyin alfavit tartibda sortirovka qilingan ro’yxatni konsolga chiqaring.

# filename = "romeo.txt"
# words = []
#
# with open(filename, "r") as f:
#     for line in f:
#         line_words = line.split()
#         for word in line_words:
#             if word not in words:
#                 words.append(word)
#
# words.sort()
# print(words)

#-----------------------------------------------------------------------

#3 *. Read_lines(lines, file) funksiya yozing, u ma’lum bir faylni ochishi lozim va konsolga oxirgi qatorlarni chiqarishi lozim berilgan lines parametri sifatida(har ehtimolga qarshi musbat son berilganini tekshirish lozim).
# funksiyani <<article.txt>> faylda sinaymiz quyidagi tarkib bilan:
# A summer day
# Has rain or sun,
# But either way
# I find it fun.
# To stand in rain
# That/s pouring down
# Or lie in sun
# That paints me brown.



def read_lines(lines, file):
    with open(file, "r") as f:
        last_lines = f.readlines()[-lines:]
        for line in last_lines:
            print(line.strip())

read_lines(3, "article.txt")


#-------------------------------------------------------
# 4 *. Dokument <<article.txt>> quyidagi matndan iborat:
#
# A summer day
# Has rain or sun,
# But either way
# I find it fun.
# To stand in rain
# That/s pouring down
# Or lie in sun
# That paints me brown.
# Longest_words(file) funksiya yaratish kerak, ushbu funksiya konsolga eng uzun so’zni chiqarishi lozim(yoki so’zlar ro’yxati, agar unaqalar bir nechta bo’lsa)

# def longest_words(file):
#     with open(file, "r") as f:
#         text = f.read()
#         words = text.split()
#         max_length = max(len(word) for word in words)
#         longest = [word for word in words if len(word) == max_length]
#         print("Longest word(s):", longest)
#
# longest_words("article.txt")


#--------------------------------------------------------------


# 5 **. the_road_not_taken.txt, byron.txt fayllar tarkibini birlashtiring bitta faylga faylning nomi Poems.txt. Har bir she’rning qatorlarini teskari qilib o’giring.

filenames = ["the_road_not_taken.txt", "byron.txt"]
output_file = "Poems.txt"

with open(output_file, "w") as out:
    for filename in filenames:
        with open(filename, "r") as f:
            lines = f.readlines()
            reversed_lines = reversed(lines)
            for line in reversed_lines:
                out.write(line)












