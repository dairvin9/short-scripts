# Learning idiomatic python

# I can hjust make equals like this
name = "Grace"
is_name = name in ("Madeline", "Rebekah","Denise","Grace")
print(is_name)

print (7 in (4,5,6))

# Enumerate is great
listy = ["giant squid","giants","giant lizard"]
for index,monster in enumerate(listy):
	print(index)
	
cakes = ["cheese","chocolate","strawberry","white"]
for index,cake in enumerate(cakes):
	print(cake)
	
# Useful exceptions to raise:
# -KeyError
# -ValueError

(maddiepie,gracey) = ("buddies","my")
(maddiepie,gracey) = (gracey,maddiepie)
print (maddiepie,gracey)
print(gracey)