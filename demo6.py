"""
Implements matplotlib's pcolor() like function, that produces a vtk file.
"""

from pylab import meshgrid, arange, cos, sin, pcolor, show
import visit_writer

def pcolor_unstructured(X, Y, C):
    """
    Does "pcolor" plot and returns points, connectivity and zonal & nodal data.
    """
    pts = []
    connectivity = []
    zonal = []
    nodal = []
    w = X.shape[0]
    h = X.shape[1]
    assert w == Y.shape[0]
    assert h == Y.shape[1]
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
            nodal.append(C[i, j])
    return pts, connectivity, zonal, nodal

# Create a simple demo (circular) mesh
r, phi = meshgrid(arange(0, 1, 0.1), arange(-3, 3, 0.1))
x = r * cos(phi)
y = r * sin(phi)
C = x * y
pts, connectivity, z1, n1 = pcolor_unstructured(x, y, C)
C = r**2
pts, connectivity, z2, n2 = pcolor_unstructured(x, y, C)
C = r**2 * sin(phi)
pts, connectivity, z3, n3 = pcolor_unstructured(x, y, C)


# Pass the data to visit_writer
vars = (
        ("C1", 1, 0, z1), ("nodal1", 1, 1, n1),
        ("C2", 1, 0, z2), ("nodal2", 1, 1, n2),
        ("C3", 1, 0, z3), ("nodal3", 1, 1, n3),
        )
visit_writer.WriteUnstructuredMesh("pcolor.vtk", 1, pts, connectivity, vars)
