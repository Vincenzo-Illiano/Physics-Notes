# Boundary value problems

Parent: [[Numerical differential equations]]

A **boundary value problem** specifies a differential equation together with conditions at the boundaries of its domain. 

For example, the one-dimensional Poisson equation with homogeneous Dirichlet conditions is
$$
-\frac{d^2u}{dx^2}=f(x),\qquad u(0)=u(1)=0.
$$

It is a special case of

$$
\alpha(x)u''+\beta(x)u'+\gamma(x)u=f(x).
$$

This is an **ordinary** differential equation because it has one independent variable. It is **linear** because $u$ and its derivatives enter linearly; the dependence of the coefficients on $x$ need not be linear. It is **inhomogeneous** when $f$ is not identically zero.

*Superposition applies directly to homogeneous equations.* If $Lu_1=f$ and $Lu_2=f$, then $L(u_1+u_2)=2f$, not $f$. A solution of the homogeneous equation can be added to a particular inhomogeneous solution, subject to the boundary conditions.

## Finite difference method

The method discretizes the equation and solves the resulting matrix system. Set $x_i=ih$, $i=0,\ldots,n+1$, with $h=1/(n+1)$. The unknowns are the $n$ interior values; the endpoint values are prescribed.

Using [[Discretization and numerical differentiation]],
$$
-\frac{u_{i-1}-2u_i+u_{i+1}}{h^2}=f_i+O(h^2).
$$

Dropping the truncation term gives the approximate equations

$$
-v_{i-1}+2v_i-v_{i+1}=h^2f_i,\qquad i=1,\ldots,n,
$$

with $v_0=v_{n+1}=0$. For **five interior points** ($n=5$, seven grid points including the boundaries),

$$
\begin{pmatrix}
2&-1&0&0&0\\
-1&2&-1&0&0\\
0&-1&2&-1&0\\
0&0&-1&2&-1\\
0&0&0&-1&2
\end{pmatrix}
\begin{pmatrix}v_1\\v_2\\v_3\\v_4\\v_5\end{pmatrix}
=\begin{pmatrix}g_1\\g_2\\g_3\\g_4\\g_5\end{pmatrix},
\qquad g_i=h^2f_i.
$$

The matrix is **tridiagonal** because the central difference couples only neighbouring samples. If the prescribed boundary values are nonzero, their contributions are moved to the first and last right-hand-side entries.

Although the formal solution is $\mathbf v=A^{-1}\mathbf g$, numerical algorithms normally solve the system without explicitly forming the inverse. [[Matrix equations]] describes how to exploit its tridiagonal structure.
