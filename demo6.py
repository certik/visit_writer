"""
Implements matplotlib's pcolor() like function, that produces a vtk file.
"""

from pylab import meshgrid, arange, cos, sin, pcolor, show
import visit_writer

# Create a simple demo (circular) mesh
r, phi = meshgrid(arange(0, 1, 0.3), arange(-3, 3, 2))
x = r * cos(phi)
y = r * sin(phi)
# C = r**2
# C = r**2 * sin(phi)
C = x * y
#pcolor(x, y, C)
#show()

pts = []
connectivity = []
zonal = []
w = x.shape[0]
h = x.shape[1]
print w, h
p = lambda i, j: i*h+j
for i in range(w):
    for j in range(h):
        pts.extend((x[i, j], y[i, j], 0))
        if i + 1 < w and j + 1 < h:
            connectivity.append( (
                    visit_writer.quad,
                    p(i, j), p(i+1, j), p(i+1, j+1), p(i, j+1),
                ) )
            zonal.append(C[i, j])

print pts
print connectivity
print zonal
#print len(pts)/3

# Node coordinates
pts2 = (
        0., 0., 0.,
        2., 0., 0.,
        5., 0., 0.,
        3., 3., 0.,
        5., 3., 0.,
        0., 5., 0.,
        2., 5., 0.,
        4., 5., 0.,
        5., 5., 0.)
# Connectivity
connectivity2 = (
   (visit_writer.triangle, 1,3,6),
   (visit_writer.triangle, 3,7,6),
   (visit_writer.quad, 0,1,6,5),
   (visit_writer.quad, 1,2,4,3),
   (visit_writer.quad, 3,4,8,7)
)
# Data arrays
zonal2 = (1,2,3,4,5)
# Pass the data to visit_writer
vars = (("C", 1, 0, zonal),)
visit_writer.WriteUnstructuredMesh("pcolor.vtk", 1, pts, connectivity, vars)
