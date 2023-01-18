# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text_for_prog = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_words(text_for_prog):
    text_for_prog = list(filter(lambda x: 'абв' not in x, text_for_prog.split()))
    return " ".join(text_for_prog)

text_for_prog = del_words(text_for_prog)
print(text_for_prog)
