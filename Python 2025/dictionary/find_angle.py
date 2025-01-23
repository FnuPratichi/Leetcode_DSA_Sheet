import math
Length_AB = int(input())
Length_BC = int(input())

AC = math.sqrt(((Length_AB)**2) + ((Length_BC)**2))
print(AC)

Length_MC = AC/2
print(Length_MC)


angle_MBC_radians = math.atan(Length_MC / Length_BC)
angle_MBC_degrees = round(math.degrees(angle_MBC_radians))

print(angle_MBC_degrees)

