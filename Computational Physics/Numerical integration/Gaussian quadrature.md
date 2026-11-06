Parent: [[Numerical integration]]

In this note we will very briefly discuss the **Gaussian quadrature** method. 

Consider a single interval with ${}n{}$ points. In Newton-Cotes methods, such as [[Simpson's rule]] or the [[Trapezoidal rule]], the points ${}x_{i}{}$ in the intervals are fixed, and we adjust ${}n{}$ points ${}w_{i}{}$ such that
$$
I = \int_{x_{0}}^{x_{n}}f(x)dx \approx \sum_{i=1}^{n}w_{i}f(x_{i}).
$$
For this reason, Newton-Cotes methods have ${}n{}$ free parameters. The idea of **Gaussian quadrature** on the other hand is to vary the points ${}x_{i}{}$ as well in order to find the best value for the integral. For this reason, Gaussian quadrature has ${}2n{}$ degrees of freedom and can be used to compute the integral of any polynomial of order ${}2n-1{}$ exactly.

## References

- [[Sources#^lecture-notes|A. Kvellestad, *Lecture notes FYS3150 - Computational Physics*, Fall 2026]]
