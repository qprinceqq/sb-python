print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах 
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

n = int(input('Кол-во минут: '))
print('В часах -', n//60)
print('Оставшихся минут -', n%60)