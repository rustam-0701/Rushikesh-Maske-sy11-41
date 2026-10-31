import gc

# Display garbage collection status
print("Garbage collection enabled:", gc.isenabled())

# Create a class
class Student:
    def __init__(self, name):
        self.name = name

# Create an object
s1 = Student("Rahul")
print("Object created:", s1.name)

# Delete the object
del s1
print("Object reference deleted.")

# Manually run garbage collection
collected = gc.collect()

print("Garbage collection completed.")
print("Objects collected:", collected)

# Disable garbage collection
gc.disable()
print("Garbage collection disabled:", gc.isenabled())

# Enable garbage collection again
gc.enable()
print("Garbage collection enabled:", gc.isenabled())