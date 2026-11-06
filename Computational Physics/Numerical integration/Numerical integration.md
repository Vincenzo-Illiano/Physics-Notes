Parent: [[Computational physics]]

A common term for **numerical integration** is **quadrature**. In these notes, we discuss two main families of methods for numerical integration:

- Newton–Cotes quadrature with a constant step size $h$, including the [[Trapezoidal rule|trapezoidal rule]] and [[Simpson's rule]].
- [[Gaussian quadrature]], in which the integration points are generally not equally spaced. This is only briefly mentioned.

These methods are often efficient for low-dimensional integration, whereas [[Monte Carlo integration]] is often useful for high-dimensional integration, as discussed in [[Monte Carlo methods]].

These quadrature methods can be formulated using **Lagrange's interpolation formula**. Given $N+1$ points $(x_i,y_i)$ with distinct $x_i$, the polynomial $P_N(x)$ of degree at most $N$ that interpolates these points is
$$
P_N(x)=\sum_{i=0}^{N}\left(\prod_{\substack{k=0\\k\neq i}}^{N}\frac{x-x_k}{x_i-x_k}\right)y_i.
$$
This formula is useful because polynomials are easy to integrate. We can therefore approximate the integral of a function by integrating a polynomial that interpolates its values at selected points. Different choices of the number and location of these points lead to different quadrature methods.

## References

- [[Sources#^lecture-notes|A. Kvellestad, *Lecture notes FYS3150 - Computational Physics*, Fall 2026. ]]
- ChatGPT 6.1 sol for grammar improvement
