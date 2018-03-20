€def topla(x,y):
	print(x+y)
def cikar(x,y):
	print(x-y)
def carp(x,y):
	print(x*y)
def bol(x,y):
	print(x/y)

s1 = int(input("İşlemi Giriniz"))
islem = input("İşlemi Giriniz")
s2 = int(input("İşlemi Giriniz"))
print("=")

if(islem == "+"):
	topla(s1 , s2)
elif(islem == "-"):
	cikar(s1 , s2)
elif(islem == "*"):
	carp(s1 , s2)
elif(islem == "/"):
	bol(s1 , s2)
