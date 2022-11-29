import string
apla = string.ascii_uppercase
usr_name = str(input("Enter Your Name : "))
for i in usr_name:
  if i in apla:
    print("You Entered Capital letter")
    break
  else:
    print("You Entered small letter")