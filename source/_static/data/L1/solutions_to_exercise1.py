
# Exercise 1

# Problem 1

from shapely.geometry import Point, LineString, Polygon

# problem 1 Point

def createPointGeom(x_coord, y_coord):
    # create a shapely Point geometry object and return that
    new_point = Point(x_coord, y_coord)
    return new_point


point1 = createPointGeom(2.2, 4.2)

point2 = createPointGeom(7.2, -25.1)

point3 = createPointGeom(9.26, -2.456)


# problem 1 Linestring

def createLineGeom(points_list):
    # Function should first check that the input list really contains Shapely Point(s)
    checked_points = []
    for p in points_list:
        if isinstance(p, Point):
            checked_points.append(p)
        else:
            print("point {} is not a Point object".format(str(p)))
            # there are more sophisticated ways to check that, and make the program safer to bad input -> later
    # takes a list of Shapely Point objects as parameter and returns a LineString object of those input points
    if len(checked_points) >= 2:
        new_line = LineString(checked_points)
        return new_line
    else:
        print("not enough points in input list t ocreate line")
        return None


list_of_points = [point1, point2, point3]

line_coords = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]
created_points = []
for tup in line_coords:
    point = Point(tup[0], tup[1])
    created_points.append(point)


line1 = createLineGeom(list_of_points)

line2 = createLineGeom(created_points)


# problem 1 Polygon

def createPolyGeom(input_list):
    # input list should contain either points or coords
    # we can call shapely Polygon only with coord list, so we need to check
    first_data = input_list[0]
    p_coord_list = []
    for elem in input_list:
        if isinstance(elem, Point):
            p_coord_list.append((elem.x, elem.y))
        elif isinstance(elem, tuple):
            p_coord_list.append((elem[0], elem[1]))
        else:
            print("elem {} is not Point or Tuple object".format(str(elem)))
    if len(p_coord_list) >= 3:
        new_poly = Polygon(p_coord_list)
        return new_poly
    else:
        print("not enough points in input list to create polygon")
        return None


coord_list = [(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)]

poly1 = createPolyGeom(coord_list)

list_of_points = [point1, point2, point3]

poly2 = createPolyGeom(list_of_points)

# problem 2 getCentroid()

def getCentroid(geom):
    return geom.centroid


point1_centroid = getCentroid(point1)
line1_centroid = getCentroid(line1)
poly2_centroid = getCentroid(poly2)


# problem 2 getArea()

def getArea(test_poly):
    if isinstance(test_poly, Polygon):
        return test_poly.area
    else:
        print("error, is not a Polygon")


poly1_area = getArea(poly1)

# problem 2 getLength()

def getLength(geom):
    # getLength() takes either a Shapely’s LineString or Polygon
    if isinstance(geom, LineString) or isinstance(geom, Polygon):
        return geom.length
    else:
        print("Error: LineString or Polygon geometries required!")


point1_length = getLength(point1)
line1_length = getLength(line1)
poly2_length = getLength(poly2)


# Problem 3: Reading coordinates from a file and creating a geometries

import pandas as pd

#/_static/exercises/Exercise-1/data/travelTimes_2015_Helsinki.txt
df = pd.read_csv('source/_static/exercises/Exercise-1/data/travelTimes_2015_Helsinki.txt', sep=';', encoding='latin1')
pd.set_option('max_columns',20)
print(df.head(5))


def make_point(x, y):
    return Point(x, y)

def make_orig_location(row):
    return Point(row['from_x'], row['from_y'])

def make_dest_location(row):
    return Point(row['to_x'], row['to_y'])


# Go through every row, and make a point out of its lat and lon
df['orig_points'] = df.apply(make_orig_location, axis=1)

df['dest_points'] = df.apply(make_dest_location, axis=1)

print(df.head(5))


def make_lines(row):
    point_list = [row['orig_points'], row['dest_points']]
    return LineString(point_list)


df['lines'] = df.apply(make_lines, axis=1)

print(df.head(5))


def calc_all_lengths(row):
    line = row['lines']
    return line.length


df['lengths'] = df.apply(calc_all_lengths, axis=1)

print(df['lengths'].mean())






