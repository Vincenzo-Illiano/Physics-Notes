Parent: [[Approximation methods]]

In this note, we will introduce **time-indipendent perturbation theory** in Quantum Mechanics as a way to estimate the energy of systems with complex Hamiltonians. Here we will look at the case of a Hamiltonian with non degenerate eigenstates. For an application, see [[Anharmonic oscillator example]].

Let $H_0$ be a Hamiltonian whose eigenvalues and eigenstates are known:
$$
H_0|\psi_n^{(0)}\rangle=E_n^{(0)}|\psi_n^{(0)}\rangle.
$$
We consider
$$
H=H_0+\lambda H',
$$
where $\lambda H'$ is a small **perturbation**, switched off when $\lambda\to0$. We want to solve
$$
H|n\rangle=E_n|n\rangle , \tag 1
$$
in the assumption that unperturbed energies $E_n^{(0)}$ are **nondegenerate**.

## Expansion in the perturbation parameter

Write the perturbed state and energy as
$$
\begin{aligned}
|n\rangle
&=|\psi_n^{(0)}\rangle
+\lambda|\psi_n^{(1)}\rangle
+\lambda^2|\psi_n^{(2)}\rangle+\cdots,\\
E_n
&=E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2E_n^{(2)}+\cdots.
\end{aligned}
$$
These are called **perturbative expansions**. The heuristic idea is the following: since ${}H{}$ is a "smooth" function of ${}\lambda{}$, we expect the solutions of (1) to be a smooth function of ${}\lambda{}$ as well. For this reason, it makes sense to write the Taylor expansion of ${}\ket{n}(\lambda){}$ and of ${}E_{n}(\lambda){}$ around ${}\lambda = 0{}$, and expect that this series is going to converge. Of course, a more precise mathematical explanation would be necessary in this case.

Substituting into equation (1) gives
$$
\begin{aligned}
&(H_0+\lambda H')
\left(|\psi_n^{(0)}\rangle+\lambda|\psi_n^{(1)}\rangle
+\lambda^2|\psi_n^{(2)}\rangle+\cdots\right)\\
&\quad=
\left(E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2E_n^{(2)}+\cdots\right)
\left(|\psi_n^{(0)}\rangle+\lambda|\psi_n^{(1)}\rangle
+\lambda^2|\psi_n^{(2)}\rangle+\cdots\right).
\end{aligned}
$$
Since we expect this to be true for any ${}\lambda{}$, we can equate coefficients of equal powers of $\lambda$ 
$$
\begin{aligned}
\lambda^0:\quad
H_0|\psi_n^{(0)}\rangle
&=E_n^{(0)}|\psi_n^{(0)}\rangle,\\
\lambda^1:\quad
H_0|\psi_n^{(1)}\rangle+H'|\psi_n^{(0)}\rangle
&=E_n^{(0)}|\psi_n^{(1)}\rangle
+E_n^{(1)}|\psi_n^{(0)}\rangle,\\
\lambda^2:\quad
H_0|\psi_n^{(2)}\rangle+H'|\psi_n^{(1)}\rangle
&=E_n^{(0)}|\psi_n^{(2)}\rangle
+E_n^{(1)}|\psi_n^{(1)}\rangle
+E_n^{(2)}|\psi_n^{(0)}\rangle. \\ &\dots
\end{aligned}
$$
## First-order energy correction

By solving the eq. for ${}\lambda^{1}{}$, we get the **first order correction**, which enables us to find the values of ${}E_{n}^{(1)}{}$ and of ${}\ket{\psi_{n}^{(1)}}{}$. This is also referred to as **first order theory**. 

#### Energy correction
Multiply the first-order equation by $\langle\psi_n^{(0)}|$:
$$
\begin{aligned}
&\langle\psi_n^{(0)}|H_0|\psi_n^{(1)}\rangle
+\langle\psi_n^{(0)}|H'|\psi_n^{(0)}\rangle
=E_n^{(0)}\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle
+E_n^{(1)}.
\end{aligned}
$$
Since $H_0$ is Hermitian,
$$
\langle\psi_n^{(0)}|H_0
=E_n^{(0)}\langle\psi_n^{(0)}|.
$$
The terms involving $\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle$ cancel, giving
$$
{E_n^{(1)}=\langle\psi_n^{(0)}|H'|\psi_n^{(0)}\rangle.}
$$
#### Eigenstate correction
In order to find the correction to the state ${}\ket{\psi_{n}^{(1)}},{}$ rearrange the first-order equation:
$$
(H_0-E_n^{(0)})|\psi_n^{(1)}\rangle
=(E_n^{(1)}-H')|\psi_n^{(0)}\rangle.
\tag{2}
$$
Since the eigenstates of ${}H_{0}{}$ form a complete basis, we can expand the correction in the unperturbed basis:
$$
|\psi_n^{(1)}\rangle
=c_n|\psi_n^{(0)}\rangle
+\sum_{m\ne n}c_m|\psi_m^{(0)}\rangle.
$$
We will now prove that ${}c_{n} = 0{}$, as this will be useful later.
Normalization of the perturbed state implies
$$
\begin{aligned}
1=\langle n|n\rangle
&=\left< \psi_{n}^{(0)}|\psi_{n}^{(0)} \right> +\lambda\left(
\langle\psi_n^{(1)}|\psi_n^{(0)}\rangle
+\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle\right)
+O(\lambda^2)\\
&=1+2\lambda\operatorname{Re}c_n+O(\lambda^2).
\end{aligned}
$$
Thus $\operatorname{Re}c_n=0$. We can show that the imaginary part can be chosen to be ${}0{}$ as well: if we change the physically irrelevant overall phase:
$$
\begin{aligned}
|n\rangle\longrightarrow e^{i\lambda\alpha}|n\rangle
&=|\psi_n^{(0)}\rangle
+\lambda\left(|\psi_n^{(1)}\rangle
+i\alpha|\psi_n^{(0)}\rangle\right)
+O(\lambda^2).
\end{aligned}
$$
This is equivalent to replacing ${}\ket{\psi_{n}^{(1)}}{}$ with ${}\ket{\psi_{n}^{(1)}+ i\alpha \psi_{n}^{(0)}}{}$, which is equivalent to replacing $c_n$ by $c_n+i\alpha$. Choosing $\alpha=-\operatorname{Im}c_n$ gives
$$
c_n=0,\qquad
\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle=0.
$$
Hence
$$
|\psi_n^{(1)}\rangle=\sum_{m\ne n}c_m|\psi_m^{(0)}\rangle.
$$
Substituting this into (2) we get
$$
\sum_{m\ne n}(E_m^{(0)}-E_n^{(0)})c_m|\psi_m^{(0)}\rangle
=(E_n^{(1)}-H')|\psi_n^{(0)}\rangle.
$$
Taking the inner product with $\langle\psi_\ell^{(0)}|$, for $\ell\ne n$,
$$
(E_\ell^{(0)}-E_n^{(0)})c_\ell
=-\langle\psi_\ell^{(0)}|H'|\psi_n^{(0)}\rangle.
$$
Therefore,
$$
{
|\psi_n^{(1)}\rangle
=\sum_{m\ne n}
\frac{\langle\psi_m^{(0)}|H'|\psi_n^{(0)}\rangle}
{E_n^{(0)}-E_m^{(0)}}|\psi_m^{(0)}\rangle.
}\tag{3}
$$
The nondegeneracy assumption ensures that the denominators do not vanish.

## Second-order energy correction

Sometimes it's necessary to calculate the second order correction ${}E_{n}^{(2)}{}$ as well, as the first order correction may vanish.

In order to do so, we multiply the second-order equation by $\langle\psi_n^{(0)}|$:
$$
\begin{aligned}
&\langle\psi_n^{(0)}|H_0|\psi_n^{(2)}\rangle
+\langle\psi_n^{(0)}|H'|\psi_n^{(1)}\rangle\\
&\quad=E_n^{(0)}\langle\psi_n^{(0)}|\psi_n^{(2)}\rangle
+E_n^{(1)}\langle\psi_n^{(0)}|\psi_n^{(1)}\rangle
+E_n^{(2)}.
\end{aligned}
$$
Since ${}H_{0}{}$ is hermitian, the terms involving $|\psi_n^{(2)}\rangle$ cancel. Using our phase convention (${}c_{n }=0{}$) and eq. (3),
$$
\begin{aligned}
E_n^{(2)}
=\langle\psi_n^{(0)}|H'|\psi_n^{(1)}\rangle
=\sum_{m\ne n}
\frac{\langle\psi_m^{(0)}|H'|\psi_n^{(0)}\rangle
\langle\psi_n^{(0)}|H'|\psi_m^{(0)}\rangle}
{E_n^{(0)}-E_m^{(0)}}.
\end{aligned}
$$
Since $H'$ is Hermitian,
$$
{
E_n^{(2)}=\sum_{m\ne n}
\frac{|\langle\psi_m^{(0)}|H'|\psi_n^{(0)}\rangle|^2}
{E_n^{(0)}-E_m^{(0)}}.
}
$$

