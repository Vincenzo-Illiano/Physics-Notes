Parent: [[Matrix equations]]
Model: [[Physical models/Devices/Buckling beam|Buckling beam]]

In this note, we will discuss how to turn eq. (1) in [[Physical models/Devices/Buckling beam|Buckling beam]] into a matrix equation, in order to solve the equation numerically.

Using $\xi=x/L$ and a consistently scaled deflection, gives
$$
\frac{d^2\hat u}{d\xi^2}=-\lambda_c\hat u,\qquad
\lambda_c=\frac{FL^2}{\gamma},\qquad
\hat u(0)=\hat u(1)=0.
$$
With $n$ interior points and dimensionless $h=1/(n+1)$, discretization gives
$$
A_h\mathbf v=\lambda_h\mathbf v,\qquad
A_h=\frac1{h^2}\operatorname{tridiag}(-1,2,-1).
$$
Which is a matrix equation. For a fixed mode, $\lambda_h$ approximates the corresponding continuum eigenvalue $\lambda_c$ as $h\to0$. If the matrix is instead defined without the $1/h^2$ factor, its eigenvalue is $h^2\lambda_h$; it must be divided by $h^2$ before comparison with $\lambda_c$.

This is a boundary value problem that becomes an eigenvalue problem. Its real symmetric matrix can be treated using the [[Jacobi rotation method]].

![[Computational Physics/Assets/buckling-modes.png]]

*Illustrative normalized shapes $\sin(n\pi\xi)$ for the first three pinned-beam modes of the stated linear model. Amplitudes are arbitrary; this is not a simulated post-buckling deformation.*
