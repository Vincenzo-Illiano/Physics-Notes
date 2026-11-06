## The device

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

## Topics

- In [[Buckling beam matrix equations|Buckling beam matrix equations]] it's discussed how to discretize eq. (1) in order to turn it into a matrix equation and solve it numerically.