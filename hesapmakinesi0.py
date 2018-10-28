print("Hesap makinesine hos geldiniz, cikmak icin q")
while True:
    x = str(input('->'))
    if x == 'q':
        break
    try:
        print(eval(x))
    except:
        print("ERROR")
        break
print("Hesap makinesini kullandiginiz icin tesekkur ederiz")
