# Physics of the buckling beam

Parent: [[Computational physical models]]

Consider a beam extending along $x\in[0,L]$ and subject to an axial compressive force $F>0$. Its small transverse static deflection is $u(x)$. The ends are pinned:

$$
u(0)=u(L)=0,
$$

but their slopes need not vanish. Thus the endpoints cannot move transversely, but the beam can rotate there.

In the linearized pinned-beam model, the deflection equation reduces to

$$
\gamma\frac{d^2u}{dx^2}=-Fu,\tag{1}
$$

where $\gamma$ is the flexural rigidity. Nonzero buckled shapes occur at the model's buckling eigenvalues; the straight configuration $u=0$ also solves the equation.

Using $\xi=x/L$ and a consistently scaled deflection, [[Equation scaling]] gives

$$
\frac{d^2\hat u}{d\xi^2}=-\lambda_c\hat u,\qquad
\lambda_c=\frac{FL^2}{\gamma},\qquad
\hat u(0)=\hat u(1)=0.
$$

With $n$ interior points and dimensionless $h=1/(n+1)$, [[Discretization and numerical differentiation]] gives

$$
A_h\mathbf v=\lambda_h\mathbf v,\qquad
A_h=\frac1{h^2}\operatorname{tridiag}(-1,2,-1).
$$

For a fixed mode, $\lambda_h$ approximates the corresponding continuum eigenvalue $\lambda_c$ as $h\to0$. If the matrix is instead defined without the $1/h^2$ factor, its eigenvalue is $h^2\lambda_h$; it must be divided by $h^2$ before comparison with $\lambda_c$.

This is a [[Boundary value problems|boundary value problem]] that becomes an eigenvalue problem. Its real symmetric matrix can be treated using the [[Jacobi rotation method]].

![[Computational Physics/Assets/buckling-modes.png]]

*Illustrative normalized shapes $\sin(n\pi\xi)$ for the first three pinned-beam modes of the stated linear model. Amplitudes are arbitrary; this is not a simulated post-buckling deformation.*
