# -*- coding: utf-8 -*-
s= input("введите путь к файлу:")
with open(s, 'r',encoding="utf-8") as f: #считываем файл с заданным текстом
    st = f.read()
string = st.lower() #если в файле есть заглавные буквы то преобразуем их в строчные для экономии
ru_alf = """абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:!?-()'\n """
dictionary = { c[1]:c[0] for c in enumerate(ru_alf) } #генерируем словарь исходных символов
last = len(ru_alf) #свободный код для словоря
p = ""
result = []
# p - предыдущие слово c - текущие (previous & current)
res_str=''
s_to=''
for c in string:
    pc = p + c #генерим новые слова для словоря путем добавления к предыдущему слову текущего символа
    cc = dictionary.get(c)
    if cc == None: #делаем проверку на наличие поступившего символа в словаре
        print(c,"<--данного символа нет в исходном словаре")
        continue
    if pc in dictionary: #если новое слово есть в словаре то передавать его еще рано
        p = pc
    else: #иначе если pc нет еще в словаре то мы его добавляем в словарь с кодом last и last увеличеваем
        v = dictionary.get(p)
        result.append(v)
        s_to=bin(last)
        res_str=res_str+s_to[2:]
        dictionary[pc] = last
        last += 1
        p = c
if p != '': #когда вышли из цикла но не успели записать то что было в p
    result.append(dictionary[p])
def myLog(x, b): #считаем получившуюся кодировку через log(last)
    if x < b:
        return 0
    return 1 + myLog(x/b, b)
print(res_str)
ln = myLog(last,2)
print(result) #отображаем ключи закодированного предложения
print(dictionary) #отображаем получившийся словарь с ключами и значениями
n = (ln * (len(result))) / (6 * len(string)) # исходная кодировка 6 битовая а кодировка результирущая ln битовая
print("выигрыш составил:", int(n*100),"% в сравнении с исходным закодированным текстом,"," а размерность новой кодировки равна: ",ln," бит")