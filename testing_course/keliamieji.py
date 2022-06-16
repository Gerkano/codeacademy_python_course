def ar_keliamieji(metai):
    return (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)
        