# LU decomposition

Parent: [[Computational linear algebra]]

## Factorization

An **LU decomposition** writes a square matrix as

$$
A=LU,
$$

with $L$ lower triangular and $U$ upper triangular. The conventional **Doolittle** normalization sets $l_{ii}=1$. For a $3\times3$ matrix, the triangular factors contain 12 potentially nonzero entries for nine equations; fixing three diagonal entries removes the scaling freedom when the factorization exists with nonzero pivots.

Not every nonsingular matrix admits this form without row exchanges. With partial pivoting, the usual factorization is $PA=LU$, where $P$ is a permutation matrix.

If the pivots are nonzero, define $D=\operatorname{diag}(u_{11},\ldots,u_{nn})$ and $U'=D^{-1}U$. Then $A=LDU'$. If $A$ is symmetric and the unpivoted factorization exists, $U'=L^T$ and

$$
A=LDL^T.
$$

*This is a factorization by congruence, not an eigenvalue diagonalization.* The diagonal entries of $D$ are generally not eigenvalues. Symmetric indefinite matrices may require pivoting and block-diagonal $D$.

Dense LU factorization costs approximately $\frac23n^3$ FLOPs. Once the factors are available, they can be reused for different right-hand sides.

## Solving linear systems

For $A\mathbf x=\mathbf b$, introduce $\mathbf w=U\mathbf x$ and solve

$$
L\mathbf w=\mathbf b,\qquad U\mathbf x=\mathbf w.
$$

With pivoting, replace $\mathbf b$ by $P\mathbf b$. Forward substitution gives

$$
w_i=\frac{1}{l_{ii}}\left(b_i-\sum_{j=1}^{i-1}l_{ij}w_j\right),
\qquad i=1,\ldots,n.
$$

For example, $w_1=b_1/l_{11}$ and $w_2=(b_2-l_{21}w_1)/l_{22}$. Backward substitution gives

$$
x_i=\frac{1}{u_{ii}}\left(w_i-\sum_{j=i+1}^n u_{ij}x_j\right),
\qquad i=n,\ldots,1.
$$

Each triangular solve costs $O(n^2)$. The factorization is still required initially, so the advantage is especially useful for repeated solves. See [[Matrix equations]] for elimination and tridiagonal structure.

## Determinants

With $l_{ii}=1$ and no pivoting,

$$
\det A=\det L\det U=\prod_{i=1}^n u_{ii}.
$$

With $PA=LU$, include the sign of the permutation:

$$
\det A=\det(P)\prod_{i=1}^n u_{ii}.
$$

Direct multiplication can overflow or underflow. For a nonsingular real matrix, compute the sign separately and use

$$
\ln|\det A|=\sum_{i=1}^n\ln|u_{ii}|.
$$

This takes $O(n)$ work after factorization and also handles negative pivots.

## Inverses

Writing $A^{-1}=[\boldsymbol\alpha_1,\ldots,\boldsymbol\alpha_n]$, its columns satisfy

$$
A\boldsymbol\alpha_i=\mathbf e_i.
$$

Thus $n$ triangular-solve pairs produce the inverse in $O(n^3)$ work after LU factorization. Repeating a full elimination independently for every column would instead cost $O(n^4)$; standard inverse algorithms reuse the factorization and do not require that wasteful approach. To solve a linear system, use the factors directly rather than computing the inverse.

## Constructing the factors

For the unit-diagonal convention, matrix multiplication gives

$$
u_{ij}=a_{ij}-\sum_{k=1}^{i-1}l_{ik}u_{kj},\qquad i\leq j,
$$

and

$$
l_{ij}=\frac{1}{u_{jj}}\left(a_{ij}-\sum_{k=1}^{j-1}l_{ik}u_{kj}\right),\qquad i>j.
$$

These formulas must be evaluated in an order in which the required previous factors are available, with nonzero pivots.
