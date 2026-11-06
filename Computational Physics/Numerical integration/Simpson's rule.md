Parent: [[Numerical integration]]

**Simpson's rule** is an integration method that approximates the integrand $f(x)$ by a second-degree polynomial over two consecutive subintervals of width $h$. With $x_{i+1}=x_i+h$ and $x_{i+2}=x_i+2h$, it gives
$$
\int_{x_i}^{x_{i+2}}f(x)\,dx
=\underbrace{\frac{h}{3}\left[f(x_i)+4f(x_{i+1})+f(x_{i+2})\right]}_{S}
+\underbrace{O\!\left(h^5\max_{x\in[x_i,x_{i+2}]}|f^{(4)}(x)|\right)}_{\text{local error}}. \tag 1
$$
This follows by integrating the quadratic polynomial obtained from **Lagrange's interpolation formula**, introduced in [[Numerical integration]]. The error estimate assumes that $f$ has a continuous fourth derivative on the interval.

We can also express Simpson's approximation in terms of the successive trapezoidal approximations $T_i$ and $T_{i+1}$ defined in [[Trapezoidal rule]]. If both approximate the integral over the same range, and $T_{i+1}$ uses half the step size of $T_i$, then
$$
S=\frac{4}{3}T_{i+1}-\frac{1}{3}T_i.
\tag{2}
$$
Equation (2) is useful because we can include it in the recursive implementation of the [[Trapezoidal rule|trapezoidal rule]]. Once we have computed $T_i$ and $T_{i+1}$, we can combine them to obtain $S$, which generally has a smaller discretization error for sufficiently smooth functions.

We can extend equation (1) to a larger interval by summing over pairs of subintervals. Let $x_k=x_0+kh$, with $n$ points and an even number $n-1$ of subintervals. This gives
$$
\begin{aligned}
I=\int_{x_0}^{x_{n-1}}f(x)\,dx
={}&\frac{h}{3}\bigl[f(x_0)+4f(x_1)+2f(x_2)+4f(x_3)+\cdots\\
&\qquad+2f(x_{n-3})+4f(x_{n-2})+f(x_{n-1})\bigr]+O(h^4).
\end{aligned}
$$
This is the **composite Simpson's rule**, with global error $O(h^4)$ on a fixed integration interval for sufficiently smooth $f$.

## References

- [[Sources#^lecture-notes|A. Kvellestad, *Lecture notes FYS3150 - Computational Physics*, Fall 2026]]
