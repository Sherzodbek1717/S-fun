# 1. Ikkita qiymat terilishini so’raydigan dastur yozing agar ulardan bittasi bo’lsa ham son bo’lmasa, konkatenatsiya bajarilishi kerak.Aks holda sonlar qo’shilishi lozim.
#
# Programma bajarilishining misoli:


# value1 = input("qiymatni kiriting: ")
# value2 = input("qiymatni kiriting: ")
#
#
# if value1.isnumeric() and value2.isnumeric():
#
#   result = float(value1) + float(value2)
#   print("natija:", result)
# else:
#
#   result = value1 + value2
#   print("natija:", result)

#-------------------------------------------------------------------

#2. sample = 'Exercises number 1, 12, 13, and 345 are important 456'
#Quyidagi misolda uch xonali sonlarni topib regular ifodalar orqali chiqarish lozim.


# import re
# sample = 'Exercises number 1, 12, 13, and 345 are important 456'
#
# three_digit_numbers = re.findall(r'\b\d{3}\b', sample)
#
# print(three_digit_numbers)

#------------------------------------------------------------------------------------
# 3. Pasda keltirilgan  kod food ro’yxatdagi so’zlarning 5-chi harfini fifth ro’yxat ichiga joylashtiradi.Ammo hozir kod noto’g’ri ishlamoqda va hato chiqarmoqda.try/except jumlani joylashtiring u tufayli kod ishga tushadi va ro’yxat yaratiladi.Agar so’z yetarlicha uzun bo’lmasa u hech narsa qaytarishi kerak emas.Eslatma. pass - operatori nol operatsiyasi hisoblanadi.hech narsa sodir bo’lmaydi kod ishga tushirilganda.




# food = ["apple", "banana", "cherry", "date", "elderberry"]
# fifth = []
#
# for item in food:
#     try:
#         fifth.append(item[4])
#     except IndexError:
#         pass
#
# print(fifth)


#------------------------------------------------------------------------------------------
# 4 *. HTML-rang topish uchun regular ifoda yarating, #ABCDEF shaklida berilgan bo’lishi kerak ya’ni # va o’n oltilik belgilardan iborat bo’lishi lozim.


import re


sample = "This text contains two HTML colors: #FFA500 and #00FF00"


color_regex = r"#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})\b"


colors = re.findall(color_regex, sample)


print(colors)



#------------------------------------------------------------------------------------------------

# 5 **. Matnda vaqtni toping.Vaqt quyidagi formatdan iborat soatlar:minutlar.Soatlar ham minutlar ham ikkita raqamdan iborat, masalan 09:00. «Завтрак в 09:00». matndagi vaqtni topadigan regular ifoda yozing.Inobatga oling «37:98» – noto’g’ri vaqt.


# import re
#
#
# sample = "We have a meeting at 14:30, please be on time."
#
#
# time_regex = r"\b([01][0-9]|2[0-3]):[0-5][0-9]\b"
#
#
# times = re.findall(time_regex, sample)
#
#
# print(times)


#-----------------------------------------------------------------------

# 6. Matndan kasrli sonlarni terib olish uchun regular ifoda yozing ajratuvchi sifatida nuqta bo’ladi.butum qism raqamlarini bo’shliq yoki vergul orqali ajratish mumkin emas.
# 1231.12313


# import re
#

# sample = "The price is $123.45, which is a 10% discount from the original $137.17."
#

# decimal_regex = r"\b\d+\.\d+\b"
#
# # Use the re.findall() function to extract the decimal numbers from the text
# decimals = re.findall(decimal_regex, sample)
#

# print(decimals)



