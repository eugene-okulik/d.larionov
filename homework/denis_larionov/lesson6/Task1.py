text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, "
        "facilisis vitae semper at, dignissim vitae libero")
text_list = text.split()
res_text = []
for word in text_list:
    if word.endswith('.'):
        res_text.append(word.replace('.', 'ing.'))
    elif word.endswith(','):
        res_text.append(word.replace(',', 'ing,'))
    else:
        res_text.append(word + 'ing')
print(' '.join(res_text))
