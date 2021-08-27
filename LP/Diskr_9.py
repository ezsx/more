# -*- coding: utf-8 -*-
s= input("введите путь к файлу:")
with open(s, 'r',encoding="utf-8") as f: #считываем файл с заданным текстом
    st = f.read()
string = st.lower() #если в файле есть заглавные буквы то преобразуем их в строчные для экономии
ru_alf = """абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.:!?-–()'\n """
#alf= "abcdef"
dictionary = { c[1]:c[0] for c in enumerate(ru_alf) } #генерируем словарь исходных символов
last = len(ru_alf) #свободный код для словоря
p = ""
result = []
# p - предыдущие слово c - текущие (previous & current)
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
        dictionary[pc] = last
        last += 1
        p = c
if p != '': #когда вышли из цикла но не успели записать то что было в p
    result.append(dictionary[p])
#функция для сложения двоичных чисел
def bin_sum(chislo):
    # получить бинарное число в виде массива чисел (бит)
    num1 = [*map(int, chislo)]
    num2 = [*map(int, "1")]
    # перевернуть числа для удобства выполнения операций
    num1 = num1[::-1]
    num2 = num2[::-1]
    # дополнить числа нулями
    size = max(len(num1), len(num2))
    num1 += [0] * (size - len(num1))
    num2 += [0] * (size - len(num2))
    # сложить 2 числа
    overflow = 0
    res = []
    for obj in zip(num1, num2):
        value = obj[0] + obj[1] + overflow
        overflow = value // 2
        res.append(value % 2)
    # если флаг переполнения установлен - добавить бит в начало нового числа
    if overflow == 1:
        res.append(1)

    # перевернуть число назад
    res = res[::-1]
    return ''.join(map(str, res))
bin_dictionary={}
intSum="000000"
re_s=intSum
bin_dictionary[0]=re_s
#кодируем значения в исходном словаре и добавляем в новый словарь
for i in range(1,len(dictionary)):
    intSum=bin_sum(intSum)
    re_s=intSum
    bin_dictionary[i]=re_s
#print(bin_dictionary) #отображаем закодированный словарь
#print(result) #отображаем ключи закодированного предложения
#print(dictionary) #отображаем получившийся словарь с ключами и значениями
stroka=''
for i in range(0,len(result)):
    stroka=stroka+bin_dictionary.get(result[i])
print("")
print("кодирование текста:","\n")
print(stroka,"\n")
print(dictionary)
print(bin_dictionary)
n = ((len(stroka))) / (6 * len(string)) #считаем выйгрыш , делим количество бит полученных
#             при равномерном кодировании на количество бит полученных при кодирование LZW
print("выигрыш составил:", int(n*100),"% в сравнении с исходным закодированным текстом")
