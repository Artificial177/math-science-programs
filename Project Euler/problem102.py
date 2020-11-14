class OnePoint(object):
   def __init__(self, x, y):
      self.x = x
      self.y = y

def sign(p1, p2, p3):
   return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

def point_in_triangle(p1, p2, p3):
   main = OnePoint(0, 0)

   d1 = sign(main, p1, p2)
   d2 = sign(main, p2, p3)
   d3 = sign(main, p3, p1)

   neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
   pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

   return not (neg and pos)

file = open("Text Files/PEtextfiles/p102_triangles.txt")
lines = file.readlines()

a = []; b = []; c = []
for line in lines:
   nums = line.split(",")
   a.append([int(nums[0]), int(nums[1])])
   b.append([int(nums[2]), int(nums[3])])
   c.append([int(nums[4]), int(nums[5][:-1])])

counter = 0
for a1, b1, c1 in zip(a, b, c):
   if point_in_triangle(OnePoint(a1[0], a1[1]),
                        OnePoint(b1[0], b1[1]),
                        OnePoint(c1[0], c1[1])):
      counter += 1

print("Number of Triangles: " + str(counter))

