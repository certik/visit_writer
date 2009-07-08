"""
Implements matplotlib's pcolor() like function, that produces a vtk file.
"""

import visit_writer

def pts_connectivity(X, Y):
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
            pts.extend((X[i, j], Y[i, j], 0))
            if i + 1 < w and j + 1 < h:
                connectivity.append( (
                        visit_writer.quad,
                        p(i, j), p(i+1, j), p(i+1, j+1), p(i, j+1),
                    ) )
    return pts, connectivity

def zonal_nodal(w, h, C):
    """
    Does "pcolor" plot and returns points, connectivity and zonal & nodal data.
    """
    zonal = []
    nodal = []
    for i in range(w):
        for j in range(h):
            if i + 1 < w and j + 1 < h:
                zonal.append(C[i, j])
            nodal.append(C[i, j])
    return zonal, nodal

def pcolor_unstructured(X, Y, C):
    pts, connectivity = pts_connectivity(X, Y)
    zonal, nodal = zonal_nodal(X.shape[0], X.shape[1], C)
    return pts, connectivity, zonal, nodal
