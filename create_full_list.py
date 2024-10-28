def create_full_list(ok_words, word):
    final_list = []
    for i in ok_words :
        letters = [word]
        final_list.append(i)
        for j in i :
            if j in letters:
                letters.remove(j)
            else:
                final_list.pop(len(final_list)-1)
                break
    return final_list


