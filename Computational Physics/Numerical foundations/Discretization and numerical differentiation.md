# Discretization and numerical differentiation

Parent: [[Numerical foundations]]

To represent a general continuous function numerically, we often replace its domain by a finite grid. This is **discretization**. Some functions can instead be represented by finite formulas, but numerical algorithms still evaluate them at finitely many points.

## Continuous functions on a grid

For $x\in[x_{\min},x_{\max}]$, choose a uniform grid

$$
x_i=x_{\min}+ih,\qquad i=0,\ldots,N,\qquad
h=\frac{x_{\max}-x_{\min}}{N}.
$$

We store samples $u_i=u(x_i)$, or numerical approximations $v_i\approx u_i$. The **step size** is $h=x_{i+1}-x_i$, so $u(x_i+h)=u_{i+1}$.

## Numerical differentiation

For a sufficiently smooth function, Taylor expansion gives

$$
\begin{aligned}
u(x+h)&=u(x)+hu'(x)+\frac{h^2}{2}u''(x)+\frac{h^3}{6}u'''(x)+O(h^4),\\
u(x-h)&=u(x)-hu'(x)+\frac{h^2}{2}u''(x)-\frac{h^3}{6}u'''(x)+O(h^4).
\end{aligned}
$$

These expansions lead to the following approximations:

**Forward difference**

$$
u_i'=\frac{u_{i+1}-u_i}{h}+O(h).
$$

**Backward difference**

$$
u_i'=\frac{u_i-u_{i-1}}{h}+O(h).
$$

**Central difference**

$$
u_i'=\frac{u_{i+1}-u_{i-1}}{2h}+O(h^2).
$$

Subtracting the two Taylor expansions cancels the even powers and yields the central first derivative. Adding the expansions, including the fourth-order term when identifying the leading error, gives

$$
u_i''=\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}+O(h^2).
$$

*The central formulas are second-order accurate, whereas the forward and backward first derivatives are first-order accurate.* This statement concerns truncation error; very small $h$ can amplify round-off, as discussed in [[Floating point errors and FLOPs]].

![[Computational Physics/Assets/finite-differences.png]]

*Secant slopes approximating $u'(x)$ for $u(x)=e^x$. The central secant uses samples on both sides of $x$.*
