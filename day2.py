def area_of_circle(r):
    return 3.14*(r**2)

def circum_of_circle(r):
    return 2*3.14*r


r = 30

print(area_of_circle(r), " площадь круга")
print(circum_of_circle(r), " длинна окружности")
print(area_of_circle(int(input())))
