def area(width, height):
    return width*height
w = int(input("가로:"))
h = int(input("세로:"))

print("가로: %d 세로: %d 넓이: %d" %(w, h, area(w, h)))