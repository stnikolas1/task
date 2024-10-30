def single_root_words (root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for i in other_words:
        if i.lower() in root_word or root_word in i.lower():
            same_words.append(i)
    print(same_words)

single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
single_root_words('Кот', 'Коты', 'Кошка', 'рокот', 'от')