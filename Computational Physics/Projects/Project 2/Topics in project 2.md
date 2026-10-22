# Topics in project 2

Parent: [[Computational physics projects]]

The main topic is the [[Physics of the buckling beam]]: a beam under axial compression, whose straight configuration loses stability at a critical force.

The linearized deflection equation is

$$
\frac{d^2u}{dx^2}=-\lambda u(x),
$$

with the coordinate and eigenvalue interpreted according to the scaling in the beam note. Discretizing this boundary value problem produces a matrix eigenvalue problem.

We study the [[Jacobi rotation method]] and its implementation, using the Armadillo and Eigen libraries, and learn **unit testing** to check the algorithm.
