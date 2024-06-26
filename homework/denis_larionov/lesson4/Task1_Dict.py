my_dict = {
    'tuple': ('bmw', 'audi', 'lada', 'mercedes', 'mitsubishi'),
    'list': ['siemens', 'nokia', 'samsung', 'motorola', 'sony'],
    'dict': {'login': 'qwerty', 'passwd': '1234567', 'person': '1229977', 'agent_name': 'manager'},
    'set': {'rowenta', 'dreame', 'laifen', 'dewal', 'swift'}
}
print('=' * 90)
print(my_dict['tuple'][-1])
print('=' * 90)
my_dict['list'].append('mob')
print(my_dict['list'])
print('=' * 90)
my_dict['list'].pop(1)
print(my_dict['list'])
print('=' * 90)
my_dict['dict'][('i am a tuple',)] = 2
print(my_dict['dict'])
print('=' * 90)
del my_dict['dict'][('i am a tuple',)]
print(my_dict['dict'])
print('=' * 90)
my_dict['set'].add('wind')
print(my_dict['set'])
print('=' * 90)
my_dict['set'].remove('rowenta')
print(my_dict['set'])
