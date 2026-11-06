Parent: [[Time-indipendent perturbation theory]]

Here we will look at time-indipendent perturbation theory in the case of a Hamiltonian with non degenerate eigenstates. For an application, see [[Anharmonic oscillator example]]. For convenience, we will repeat eq. (,) in [[Time-indipendent perturbation theory]].
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

