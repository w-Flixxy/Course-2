age = 10
height = 100
 #and
if age >= 8 and height >= 140:
    print("You can ride the ride!")

#or
if age >= 17 or height >= 160:
    print("YOu can run the super ride!")

#elif(else if)

if height <= 120:
    print("You cannot ride any rides!")
elif height <= 135:
    print("You can only ride level-1 rides!")
elif height <= 200:
    print("You can ride any ride!")
else:
    print("Too tall to ride any rides!")