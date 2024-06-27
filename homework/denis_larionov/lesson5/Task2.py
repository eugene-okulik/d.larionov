text1 = 'результат операции: 42'
text2 = 'результат операции: 514'
text3 = 'результат работы программы: 9'
res_text1 = int(text1.split(':')[-1]) + 10
res_text2 = int(text2.split(':')[-1]) + 10
res_text3 = int(text3.split(':')[-1]) + 10
print(res_text1, res_text2, res_text3)
