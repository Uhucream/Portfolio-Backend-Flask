def cut_none_keys(dic):
    for key in list(dic):
        if dic[key] is None:
            dic.pop(key)

    return dic