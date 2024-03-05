import math
i = 0

points = [{'x': 2, 'y': 0, 'inRegion': 'unknown',}, 
      {'x': -3, 'y': 4, 'inRegion': 'unknown'},
      {'x': 5, 'y': 3, 'inRegion': 'unknown'},
      {'x': 0, 'y': 7, 'inRegion': 'unknown'},
      {'x': -6, 'y': 0, 'inRegion': 'unknown'}
          ]

def isPointInRegion(x:float, y:float)->bool: 
      aux, x0, y0 = 5, 5, 5 
      return (aux**2 >= x**2) and (aux**2 >= y**2), math.sqrt(x ** 2 + y ** 2) <= aux, math.sqrt((x-x0)**2 + (y-y0)**2) <= aux

while i < 5:
      circle, square, random_square = isPointInRegion(points[i]['x'], points[i]['y'])
      if circle:
        points[i]['inRegion'] = 'Принадлежит'  
      else:
         points[i]['inRegion'] = 'Не принадлежит' 
      i += 1
      
print('а)', points, '\n')

while i < 5:
      circle, square, random_square = isPointInRegion(points[i]['x'], points[i]['y'])
      if square:
        points[i]['inRegion'] = 'Принадлежит' 
      else:
         points[i]['inRegion'] = 'Не принадлежит' 
      i += 1
      
print('б)', points, '\n')

while i < 5:
      circle, square, random_square = isPointInRegion(points[i]['x'], points[i]['y']) 
      if random_square:
        points[i]['inRegion'] = 'Принадлежит' 
      else:
         points[i]['inRegion'] = 'Не принадлежит' 
      i += 1
      
print('в)', points)
