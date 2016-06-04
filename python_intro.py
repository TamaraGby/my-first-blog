print("Hello, Django girls")
if 3>2:
	print("It works!")
	if 5>2:
		print("5 est effectivement plus grand que 2")
	else:
		print("5 n'est pas plus grand que 2")
name="Olivier"
if name=="Tamara":
	print("Hey Tamara")
elif name == "Sonja":
	print("Hey Sonja")
else:
	print("Hey anonymous!")
volume=57
if volume<20:
	print("C'est plutôt calme.")
elif 20<=volume<40:
	print("Une jolie musique de fond.")
elif 40<=volume<60:
	print("Parfait, je peux entendre tous les détails du morceau.")
elif 60<=volume<80:
	print("Parfait pour faire la fête.")
elif 80<=volume<100:
	print("Un peu trop fort.")
else:
	print("Au secours ! Mes oreilles !:(")
def hi():
	print("Hi there!")
	print("How are you?")
hi()
def hi(name):
	if name=="Tamara":
		print("Hi Tamara")
	elif name=="Sonja":
		print("Hi Sonja")
	else:
		print("Hi anonymous")
hi("Mathilda")
def hi(name):
	print("Hi "+name+"!")
girls=["Rachel","Monica","Phoebe","Ola","Tamara"]
for name in girls:
	hi(name)
	if name == "Rachel":
		print("T'es la meilleure")
	print("Next girls")
for i in range(1,6):
	print(i)