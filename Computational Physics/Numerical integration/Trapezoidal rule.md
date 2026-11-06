Parent: [[Numerical integration]]

The **trapezoidal rule** is a method for numerical integration. The idea is to approximate the integrand $f(x)$ by a first-degree polynomial $P_1(x)$ on each interval $[x_i,x_i+h]$, integrate $P_1(x)$ over that interval, and sum the results.

For a function with a continuous second derivative, we obtain
$$
\begin{aligned}
\int_{x_i}^{x_i+h}f(x)\,dx
&=\int_{x_i}^{x_i+h}\left[P_1(x)+O\!\left(h^2\max_{x\in[x_i,x_i+h]}|f''(x)|\right)\right]\,dx\\
&=\frac{h}{2}\left[f(x_i)+f(x_i+h)\right]
+O\!\left(h^3\max_{x\in[x_i,x_i+h]}|f''(x)|\right).
\end{aligned}
$$
Summing over all subintervals from $a$ to $b$ gives an approximation to the full integral. The local error is $O(h^3)$, so the global error over a fixed interval is $O(h^2)$. In particular, with $x_i=a+ih$ and $h=(b-a)/n$,
$$
I=\int_a^b f(x)\,dx
=h\left[\frac{1}{2}f(x_0)+f(x_1)+\cdots+f(x_{n-1})+\frac{1}{2}f(x_n)\right]+O(h^2).
$$

## Implementation

An efficient implementation of the trapezoidal rule uses a **recurrence relation**. To see how this works, consider a sequence of step sizes obtained by halving the step size at each iteration. Starting with $h_1=b-a$, we have
$$
T_1=\frac{h_1}{2}\left[f(a)+f(b)\right],
$$
where $T_1$ is a first approximation to the integral. Halving the step size to $h_2=h_1/2$ gives
$$
T_2=h_2\left[\frac{1}{2}f(a)+f(a+h_2)+\frac{1}{2}f(b)\right].
$$
We can rewrite this as
$$
T_2=\frac{1}{2}T_1+h_2f(a+h_2).
$$
Halving the step size again, so that $h_3=h_2/2$, gives
$$
T_3=\frac{1}{2}T_2+h_3\left[f(a+h_3)+f(a+3h_3)\right].
$$
More generally, let $n_j=2^{j-1}$ be the number of subintervals used in $T_j$, and let $h_j=(b-a)/n_j$. Then
$$
T_{j+1}=\frac{1}{2}T_j+h_{j+1}\sum_{k=1}^{n_j}f\!\left(a+(2k-1)h_{j+1}\right).
$$
This recurrence reuses previously computed function values. This way only the new midpoints need to be evaluated.

Uniformly halving the step size refines the entire integration range. We can also use these approximations in a recursive algorithm that **adaptively subdivides the integration range**, using different step sizes in different regions. The idea is to use larger steps where a linear approximation is adequate and smaller steps where the curvature of $f$ makes the error larger.

A simple adaptive procedure is:

1. Choose a relative tolerance $\epsilon$.
2. Compute $T_1$ over the current integration interval.
3. Compute $T_2$ over the same interval using half the step size.
4. If $|T_2-T_1|>\epsilon|T_1|$, split the interval in two and repeat from step 2 on each half. Otherwise, accept $T_2$ for the current interval.
5. Sum the accepted approximations over all subintervals.

The difference $|T_2-T_1|$ serves as an error indicator. A better version of this algorithm can be made using [[Simpson's rule|Simpson's rule]], which consists of accepting ${}4 / 3 T_{2} - 1/3 T_{1}{}$ instead of simply ${}T_{2}{}$. 

![[adaptive_trapezoidal_rule.png]]

## References

- [[Sources#^lecture-notes|A. Kvellestad, *Lecture notes FYS3150 - Computational Physics*, Fall 2026]]
- ChatGPT 6.1 sol for assistance with language and graph.
