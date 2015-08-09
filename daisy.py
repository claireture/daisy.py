def fan(name):
	return len(name) # hash sign = comment
	
pet_names = ["Daisy", "Abby", "Dashi", "Black Sheep Rico"]
print pet_names[0]

del pet_names [1]

for name in pet_names:
	print "hello %s!" % (name)
	print fan(name)


print "Number of pets = %d" % len(pet_names)

pet_attributes = {
	"Daisy": ("tan", 9), 
	"Abby": ("tortoise", 5),
	"Dashi": ("seal", 9),
	}
pet_attributes["Westie"] =  ("Brown", -5)
print pet_attributes ["Westie"][0]



