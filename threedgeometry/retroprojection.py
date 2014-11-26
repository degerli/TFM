#!/usr/bin/env python

"""
r = np.array([[-0.51413534, 0.25338303, -0.81942778], [-0.43703925, -0.89943394, -0.00391001], [-0.73801189, 0.35611183, 0.5731691]])
t = np.array([[ -2952.436879], [  1410.285426], [ 80157.550249]])
h = np.array([[r[0, 0], r[0, 1], t[0]], [r[1, 0], r[1, 1], t[1]], [r[2, 0], r[2, 1], t[2]]])
h = h / t[2]
ih = np.linalg.inv(h)
uv = np.array([[100], [100], [1]])
d = ih.dot(uv)
d = d / d[2]
"""
