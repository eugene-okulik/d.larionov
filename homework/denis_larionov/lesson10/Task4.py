PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


price = PRICE_LIST
v = price.replace('0р', '0')
res_dict = dict((key, int(value)) for key, value in (element.split(' ') for element in v.split('\n')))
print(res_dict)
