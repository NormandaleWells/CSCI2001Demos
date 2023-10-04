import math

# Start with a bunch of points.
pts = [(1,1), (3,3), (1,3), (3,1), (2,2), (2,4)]

# This will sort by their x coordinates (first element of tuple).
sorted(pts)

# What if we want to sort by y coordinates?  We can use key=
# with a function.

def return_y(pt):
	return pt[1]
sorted(pts, key=return_y)

# Alternatively, we could define a lambda.

sorted(pts, key=lambda k: k[1])

# The previous code leaves x coordinates randomly ordered
# for given y.  This fixes the above issue.

sorted(pts, key=lambda k: (k[1], k[0]))

# What if we want to sort based on the distance from the
# origin to the point (the point's magnitude).

def magnitude(pt):
	x = pt[0]
	y = pt[1]
	return math.sqrt(x*x + y*y)
sorted(pts, key=magnitude)

# We can also do this as a lambda, but it's a bit less
# readable because we can't create local variables like
# x and y inside a lambda

sorted(pts, key=lambda pt: math.sqrt(pt[0]*pt[0] + pt[1]*pt[1]))

# What if we need to sort based on distance to some other
# point?

def distance_to(pt1, pt2):
	dx = pt2[0] - pt1[0]
	dy = pt2[1] - pt1[0]
	return math.sqrt(dx*dx + dy*dy)

# distance_to() takes two parameters, but sort() will only
# provide one to the function (or lambda).  We can use
# a lambda with a capture.

origin = (0,0)
sorted(pts, key=lambda pt: distance_to(origin, pt))

pt_ref = (2,2)
sorted(pts, key=lambda pt: distance_to(pt_ref, pt))
