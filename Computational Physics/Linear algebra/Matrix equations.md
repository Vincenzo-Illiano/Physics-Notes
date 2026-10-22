# Matrix equations

Parent: [[Computational linear algebra]]

We want to solve

$$
A\mathbf{v}=\mathbf{b},
$$

where $A$ is an $n\times n$ matrix. A unique solution exists for every $\mathbf b$ if and only if $A$ is nonsingular, equivalently $\det A\neq0$. A singular system can have either no solution or infinitely many solutions, depending on $\mathbf b$.

## Gaussian elimination

Gaussian elimination has two main stages:

1. **Forward elimination** transforms $A$ into an upper triangular matrix, applying the same row operations to $\mathbf b$.
2. **Backward substitution** solves the triangular system, starting with the last unknown.

For example, $R_2\leftarrow R_2-2R_1$ subtracts twice the first row from the second. Row operations preserve the solution because they act on both sides of the equation. In practice, row interchanges (**pivoting**) avoid zero pivots and improve numerical stability.

Backward substitution does not turn $A$ into a lower triangular matrix. Continuing row operations until the matrix becomes the identity is the related **Gauss–Jordan elimination** procedure.

An alternative is [[LU decomposition]], which stores the elimination in reusable triangular factors. For large sparse systems, [[Iterative methods]] may be useful.

## Tridiagonal systems: the Thomas algorithm

Let $b_i$ be the diagonal entries, $a_i$ the entries below the diagonal, and $c_i$ the entries above it. For example,

$$
\begin{pmatrix}
b_1&c_1&0&0\\
a_2&b_2&c_2&0\\
0&a_3&b_3&c_3\\
0&0&a_4&b_4
\end{pmatrix}
\begin{pmatrix}v_1\\v_2\\v_3\\v_4\end{pmatrix}
=\begin{pmatrix}g_1\\g_2\\g_3\\g_4\end{pmatrix}.
$$

To remove $a_2$, use $R_2\leftarrow R_2-(a_2/b_1)R_1$. The new diagonal and right-hand-side entries are

$$
\tilde b_2=b_2-\frac{a_2}{b_1}c_1,\qquad
\tilde g_2=g_2-\frac{a_2}{b_1}g_1.
$$

Continuing along the rows gives the forward-elimination recurrences

$$
\begin{aligned}
\tilde b_1&=b_1,&\tilde g_1&=g_1,\\
m_i&=\frac{a_i}{\tilde b_{i-1}},& i&=2,\ldots,n,\\
\tilde b_i&=b_i-m_ic_{i-1},&
\tilde g_i&=g_i-m_i\tilde g_{i-1}.
\end{aligned}
$$

The resulting matrix is upper triangular, with diagonal $\tilde b_i$ and upper diagonal $c_i$. Backward substitution then gives

$$
v_n=\frac{\tilde g_n}{\tilde b_n},\qquad
v_i=\frac{\tilde g_i-c_iv_{i+1}}{\tilde b_i},
\quad i=n-1,\ldots,1.
$$

This is the **Thomas algorithm**. It uses $O(n)$ work by exploiting tridiagonal structure. These formulas assume that all required pivots are nonzero; arbitrary tridiagonal systems may require pivoting. There is no need to explicitly form $A^{-1}$ to solve the system.
