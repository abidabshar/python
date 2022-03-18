try:
 radius=int(input("What is the radius of the circle "))
except ValueError:
  print("Please,input the radius value again")
  radius=float(input("What is the radius of the circle "))

pi=3.142
rsqr=radius*radius
Area=pi*rsqr
print("Area of the circle is "+str(Area))