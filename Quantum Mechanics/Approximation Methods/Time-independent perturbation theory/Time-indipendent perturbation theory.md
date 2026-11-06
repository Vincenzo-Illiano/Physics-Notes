Parent: [[Approximation methods]]

In this note, we will introduce **time-indipendent perturbation theory** in Quantum Mechanics as a way to estimate the energy of systems with complex Hamiltonians. 

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
\end{aligned} \tag .
$$
These equations are solved in different ways whether ${}\ket{\psi_{n}^{(0)}}{}$ is or isn't a degenerate state. This splits the theory in:
- [[Nondegenerate time-independent perturbation theory]] when ${}E_{n}^{(0)}{}$ is nondegenerate
- [[Degenerate time-independent perturbation theory]] when ${}E_{n}^{(0)}{}$ is degenerate