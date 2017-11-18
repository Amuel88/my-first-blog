print('Hello, Django girls!')
name="Anne"
if 5>2:
    print("Lääääuft!")
else:
    print("Läuft nicht!")
if name=="Sonja":
    print("Hallo Sonja")
elif name=="Anne":
    print("Hallo Anne")
else:
    print("Hallo Fremder!")
def hi():
    print ("Hallo!")
    print ("Wie geht's?")
hi()
def hi(name):
    if name=="Sonja":
        print ("Hi Sonja!")
    elif name=="Anne":
        print("Hi Anne!")
    else:
        print ("Hallo Fremder!")
hi("Nils")

def hi(name):
        print("Hi "+name+"!")

girls=["Rachel", "Monica", "Phoebe", "Anne", "Du"]
for name in girls:
    hi(name)
    print("Next girl")

for i in range (1, 8):
    print(i)
