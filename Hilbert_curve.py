# Hilbert_curve.py
#
# author: Ted Pudlik
# created: May 11th, 2013

"""
Hilbert curve plotter: this program generates and plots approximations to the
Hilbert curve containing a finite number of turns.  I define a 'Hilbert cap'
to be the the curve connecting four points,

       ------------------
       |                |
       |                |
       |                |
       |                |
       |                |
       |                |

and a 'Hilbert fork' to be four such caps, symmetrically placed and  connected
to form a single curve:

       ----  ----
       |  |  |  |
       |  ----  |
       |        |
       ----  ----
          |  |
       ----  ----

The Hilbert cap contains 4 points and is the Hilbert curve of order 0.  The
Hilbert fork contains 16 points (or 4 caps) and is the Hilbert curve of order 1.
The Hilbert curve of order n has 4^(n+1) points and is obtained by converting
each Hilbert cap in the Hilbert curve of order n-1 into a fork.  In the limit
n -> infinity, the Hilbert curve becomes space-filling.

To learn more about these objects, consult the article "Crinkly Curves" by
Brian Hayes, published in the May-June 2013 issue of the American Scientist
(Volume 101, page 178).  My program implements the `grammatical' algorithm for
the curve's generation, described on page 179.
"""


import numpy as np
import itertools
import matplotlib.pyplot as plt

start_path = [np.array([0.25, 0.25]), np.array([0.25, 0.75]),
              np.array([0.75, 0.75]), np.array([0.75, 0.25])]

def cap_to_fork(point_list):
    """ Given a list of the coordinates of four points making up a Hilbert cap,
        return a list of the coordinates of sixteen points making up the Hilbert
        fork.
    """
    A, B, C, D = point_list
    x = (D-A)/2
    y = (B-A)/2
    E = A - x/2 - y/2
    F = E + x
    G = F + y
    H = G - x
    I = H + y
    J = I + y
    K = J + x
    L = K - y
    M = L + x
    N = M + y
    O = N + x
    P = O - y
    Q = P - y
    R = Q - x
    S = R - y
    T = D + x/2 - y/2
    return [E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T]

def caps_from_path(path):
    """ Yield successive size-four chunks from path.  These chunks correspond
        to the Hilbert caps of which the path is composed.

        Based on the accepted answer to,
        http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    """
    for i in xrange(0, len(path), 4):
        yield path[i:i+4]

def finegrain(path):
    """ Given a list of points making up a Hilbert curve of some order,
        return the Hilbert curve of next order.

        This function works by converting the path into a sequence of caps
        using caps_from_path, then converting each cap to a fork using
        cap_to_fork, and finally chaining the points in all forks.  (The
        chaining operation can be thought of as a list flattening: recall that
        the application of map leaves us with a list of lists of points.)
    """
    return list(itertools.chain.from_iterable(map(cap_to_fork, caps_from_path(path))))

def Hilbert_curve(order):
    """ Return a path corresponding to the Hilbert curve of given order, where
        order = 0 is a single Hilbert cap (the start_path).
    """
    if order < 0 or not isinstance(order, (int, long)):
        raise TypeError
    elif order == 0:
        return start_path
    else:
        return finegrain(Hilbert_curve(order - 1))

def plot_Hilbert_curve(order):
    """ Plot a Hilbert curve of given order and save the image as a png file.
    """
    plt.axes([0,0,1,1])
    plt.axes().set_aspect('equal')
    point_array = np.array(Hilbert_curve(order))
    plt.plot(point_array[:,0], point_array[:,1])
    plt.tight_layout()
    plt.gca().axis('off')
    plt.savefig("".join(['Hilbert_curve_', str(order),'.png']))
    plt.show()
