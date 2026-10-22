# Iterative methods

Parent: [[Computational linear algebra]]

Iterative methods solve [[Matrix equations]] by refining a guess for $A\mathbf x=\mathbf b$. They can be useful for large sparse matrices because they avoid storing dense factors. Their convergence depends on the matrix and method; they are not automatically simpler or faster than direct solvers.

## Convergence and stopping criteria

Two possible indicators are the relative change

$$
\epsilon_n=\frac{\|\mathbf x^{(n+1)}-\mathbf x^{(n)}\|}{\|\mathbf x^{(n+1)}\|}
$$

and the relative residual

$$
\mathbf r^{(n)}=A\mathbf x^{(n)}-\mathbf b,\qquad
\eta_n=\frac{\|\mathbf r^{(n)}\|}{\|\mathbf b\|}.
$$

The norm can be an $\ell^p$ norm or the infinity norm. Use an absolute criterion when a denominator is zero. A small change can indicate stagnation rather than accuracy. A small residual measures how well the equations are satisfied, but does not necessarily imply a small solution error for an ill-conditioned matrix. Computing it requires a matrix–vector product unless an update is already available.

## Jacobi iteration

Split $A=L+D+U$, with $L,U$ strictly lower and upper triangular, and $D$ diagonal. For example,

$$
\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}
=\begin{pmatrix}0&0&0\\a_{21}&0&0\\a_{31}&a_{32}&0\end{pmatrix}
+\begin{pmatrix}a_{11}&0&0\\0&a_{22}&0\\0&0&a_{33}\end{pmatrix}
+\begin{pmatrix}0&a_{12}&a_{13}\\0&0&a_{23}\\0&0&0\end{pmatrix}.
$$

Assuming $a_{ii}\neq0$, rearrangement gives

$$
\mathbf x^{(n+1)}=-D^{-1}(L+U)\mathbf x^{(n)}+D^{-1}\mathbf b.
$$

In components,

$$
x_i^{(n+1)}=\frac{1}{a_{ii}}\left(b_i-\sum_{j\neq i}a_{ij}x_j^{(n)}\right).\tag{1}
$$

All new components use the old iterate. A stationary linear iteration has the affine form $\mathbf x^{(n+1)}=T\mathbf x^{(n)}+\mathbf c$. The **error**, rather than the iterate itself, obeys $\mathbf e^{(n+1)}=T\mathbf e^{(n)}$. Such an iteration converges from every initial guess if and only if its **spectral radius** satisfies $\rho(T)<1$. For Jacobi, $T=-D^{-1}(L+U)$.

This Jacobi method solves a linear system; [[Jacobi rotation method]] solves an eigenvalue problem.

## Gauss–Seidel (GS)

Gauss–Seidel uses new components as soon as they are available:

$$
x_i^{(n+1)}=\frac{1}{a_{ii}}\left(b_i-
\sum_{j=1}^{i-1}a_{ij}x_j^{(n+1)}-
\sum_{j=i+1}^{N}a_{ij}x_j^{(n)}\right).\tag{2}
$$

For a $4\times4$ system, the second update is

$$
x_2^{(n+1)}=\frac{b_2-a_{21}x_1^{(n+1)}-a_{23}x_3^{(n)}-a_{24}x_4^{(n)}}{a_{22}}.
$$

The components are evaluated sequentially in the chosen ordering. Its iteration matrix is $T=-(D+L)^{-1}U$. It often converges faster than Jacobi for common discretized problems, but this is not a universal guarantee.

## Successive over-relaxation (SOR)

SOR adds a weighted Gauss–Seidel change to the old value:

$$
x_i^{(n+1)}=x_i^{(n)}+\frac{\omega}{a_{ii}}\left(
b_i-\sum_{j<i}a_{ij}x_j^{(n+1)}-\sum_{j>i}a_{ij}x_j^{(n)}-a_{ii}x_i^{(n)}\right).\tag{3}
$$

For $\omega=1$ this is GS; $0<\omega<1$ is under-relaxation and $1<\omega<2$ is over-relaxation. In matrix form,

$$
\mathbf x^{(n+1)}=(D+\omega L)^{-1}
\left[-\bigl(\omega U+(\omega-1)D\bigr)\mathbf x^{(n)}+\omega\mathbf b\right].
$$

For real symmetric positive-definite $A$, SOR converges for $0<\omega<2$; the endpoints are excluded. For a general matrix, membership in this interval alone does not guarantee convergence. The best parameter minimizes the iteration matrix's spectral radius and depends on the problem.
