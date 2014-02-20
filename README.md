This small Python module generates and plots approximations to the Hilbert curve containing a finite number of turns.

I define a 'Hilbert cap' to be the the curve connecting four points,

       ------------------
       |                |
       |                |
       |                |
       |                |
       |                |
       |                |

and a 'Hilbert fork' to be four such caps, symmetrically placed and  connected to form a single curve:

       ----  ----
       |  |  |  |
       |  ----  |
       |        |
       ----  ----
          |  |
       ----  ----

The Hilbert cap contains 4 points and is the Hilbert curve of order 0.  The Hilbert fork contains 16 points (or 4 caps) and is the Hilbert curve of order 1. The Hilbert curve of order n has 4^(n+1) points and is obtained by converting each Hilbert cap in the Hilbert curve of order n-1 into a fork.  In the limit n -> infinity, the Hilbert curve becomes space-filling.

To learn more about these objects, consult the article "Crinkly Curves" by Brian Hayes, published in the May-June 2013 issue of the *American Scientist* (Volume 101, page 178).  My program implements the 'grammatical' algorithm for the curve's generation, described on page 179.