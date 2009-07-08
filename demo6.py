"""
Implements matplotlib's pcolor() like function, that produces a vtk file.
"""

from pylab import meshgrid, arange, cos, sin
import visit_writer
from pcolor import pcolor_unstructured

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
