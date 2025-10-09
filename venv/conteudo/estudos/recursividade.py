def regressiva(i):
    print (i)
    if i <= 1:
        return
    else:
        regressiva(i-1)

i = 3
regressiva(i)