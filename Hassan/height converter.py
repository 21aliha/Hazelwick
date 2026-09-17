cm_inch=1/2.54
heightcm=float(input("Please enter your height in cm: "))
heightm= round(heightcm / 100,2)
heightinch=round(heightcm * cm_inch,2)
print("You are", heightm,"metres tall which is", heightinch,"in inches")
print("Taller than 180cm:", heightcm >= 180)