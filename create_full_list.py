def create_full_list(ok_words, word):
    final_list = []
    for i in ok_words :
        is_word_fit = True
        letters = [i for i in word]
        for j in i :
            if j in letters:
                letters.remove(j)
            else:
                is_word_fit = False
                break
        if is_word_fit :
            final_list.append(i)
    return final_list


