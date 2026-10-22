# Jacobi rotation method

Parent: [[Computational linear algebra]]

The **Jacobi rotation method** finds eigenvalues and eigenvectors of a real symmetric matrix by successively eliminating off-diagonal elements.

## Similarity transformations

A **similarity transformation** has the form $S^{-1}AS$ for an invertible $S$. If $S$ is real orthogonal, $S^{-1}=S^T$ and $SS^T=S^TS=I$.

For real symmetric $A$, the spectral theorem guarantees an orthogonal $S$ such that

$$
S^TAS=D,\qquad AS=SD,\tag{1}
$$

with $D$ diagonal. Comparing columns gives $A\mathbf S_i=d_i\mathbf S_i$: the columns of $S$ are eigenvectors, and the diagonal entries of $D$ are eigenvalues.

## Successive plane rotations

Start with $A^{(0)}=A$ and $R^{(0)}=I$. At each iteration,

$$
A^{(m+1)}=S_m^TA^{(m)}S_m,\qquad
R^{(m+1)}=R^{(m)}S_m.
$$

Ideally $A^{(m)}\to D$ and $R^{(m)}\to S$, rather than $A^{(m)}\to A$. Each $S_m$ is the identity except for a rotation in a coordinate plane $(k,l)$.

Use the following sign convention throughout:

$$
(S_m)_{kk}=(S_m)_{ll}=c,\quad
(S_m)_{kl}=s,\quad (S_m)_{lk}=-s,
\qquad c=\cos\theta,\quad s=\sin\theta.
$$

For $n=4$, $k=2$, $l=3$, this is

$$
S_m=\begin{pmatrix}1&0&0&0\\0&c&s&0\\0&-s&c&0\\0&0&0&1\end{pmatrix}.
$$

The algorithm selects the largest absolute off-diagonal entry in the upper triangle, chooses $\theta$ to make that entry zero, and repeats until the maximum is below a tolerance. Symmetry makes the corresponding lower-triangle entry vanish as well.

## The $2\times2$ case

Let

$$
A=\begin{pmatrix}a_{11}&a_{12}\\a_{12}&a_{22}\end{pmatrix},\qquad
S=\begin{pmatrix}c&s\\-s&c\end{pmatrix}.
$$

Then $A'=S^TAS$ has entries

$$
\begin{aligned}
a'_{11}&=a_{11}c^2-2a_{12}cs+a_{22}s^2,\\
a'_{22}&=a_{22}c^2+2a_{12}cs+a_{11}s^2,\\
a'_{12}&=a'_{21}=(a_{11}-a_{22})cs+a_{12}(c^2-s^2).
\end{aligned}\tag{2}
$$

For $a_{12}\neq0$, set

$$
\tau=\frac{a_{22}-a_{11}}{2a_{12}},\qquad t=\tan\theta=s/c.
$$

Setting $a'_{12}=0$ gives $t^2+2\tau t-1=0$, so

$$
t=-\tau\pm\sqrt{1+\tau^2}.
$$

Both roots eliminate the element, but the smaller $|t|$ gives the smaller rotation. Direct evaluation of that root suffers cancellation when $|\tau|$ is large. A stable equivalent is

$$
t=\begin{cases}
\displaystyle\frac{1}{\tau+\sqrt{1+\tau^2}},&\tau\geq0,\\[6pt]
\displaystyle-\frac{1}{-\tau+\sqrt{1+\tau^2}},&\tau<0.
\end{cases}
$$

For $\tau=0$, the chosen branch gives $t=1$; $t=-1$ is equally valid. Then

$$
c=\frac{1}{\sqrt{1+t^2}},\qquad s=tc.
$$

One rotation diagonalizes a $2\times2$ symmetric matrix in exact arithmetic. If the off-diagonal entry is already zero, no rotation is needed.

## General algorithm

1. Set $A^{(0)}=A$ and $R^{(0)}=I$.
2. Find $(k,l)$, $k<l$, maximizing $|a_{kl}^{(m)}|$.
3. If that maximum is below $\epsilon$, stop.
4. Compute $\tau=(a_{ll}^{(m)}-a_{kk}^{(m)})/(2a_{kl}^{(m)})$, followed by the stable $t,c,s$ above.
5. Apply $A^{(m+1)}=S_m^TA^{(m)}S_m$ and $R^{(m+1)}=R^{(m)}S_m$.
6. Repeat from step 2.

The diagonal of the final matrix approximates the eigenvalues; the columns of the accumulated $R$ are the corresponding eigenvectors. This is different from [[Iterative methods|Jacobi iteration for linear systems]].

![[Computational Physics/Assets/jacobi-rotation.png]]

*A single rotation diagonalizes $A=\begin{pmatrix}2&1\\1&3\end{pmatrix}$. Colours show the matrix entries before and after rotation.*
