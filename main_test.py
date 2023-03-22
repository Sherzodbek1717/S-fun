# Json
import  json
# data = {
#     "student": {
#         "id": 1,
#         "name": "Abror",
#         "course": "python"
#
#
#     }
# }
# data_str = json.dumps(data)
#
# with open('student_info.json', mode = 'w', encoding= 'utf-8') as file: json.dump(data_str,file)

# with open('student_info.json', mode='r', encoding='utf-8') as file:
#     content = json.load(file)
#     content_python_obj = json.loads(content)
#     print(content_python_obj['student']['name'])

user_language = input("Tilni tanleng: ru, uz: ")
if user_language == 'uz':
    file = open('uz.json', mode='r', encoding='utf-8')
elif user_language == 'ru':
    file = open('ru.json', mode ='r', encoding='utf-8')

content = json.load(file)

print(content['messages']['start'])
user_answer = input(content['questions']['start'])