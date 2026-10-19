The **variational method** is an approximation method ([[Approximation methods]]) to estimate the ground energy of a system.

## Variational principle
For a Hamiltonian $H$ with ground-state energy $E_0$, any normalized state $|\psi\rangle$ satisfies
$$
{\langle\psi|H|\psi\rangle\geq E_0.}\tag 1
$$
To prove this, expand $|\psi\rangle$ in a complete orthonormal set of eigenstates of $H$:
$$
|\psi\rangle=\sum_n c_n|\psi_n\rangle,
\qquad H|\psi_n\rangle=E_n|\psi_n\rangle,
\qquad \sum_n|c_n|^2=1.
$$
Then:
$$
\begin{aligned}
\langle\psi|H|\psi\rangle
&=\sum_{m,n}c_m^*c_n\langle\psi_m|H|\psi_n\rangle\\
&=\sum_{m,n}c_m^*c_n E_n\delta_{mn}\\
&=\sum_n|c_n|^2E_n\\
&\geq E_0\sum_n|c_n|^2=E_0.
\end{aligned}
$$
Thus, choosing different normalized trial states and calculating their energy expectation values gives **upper bounds** on $E_0$. The smallest value found is our estimate of the ground-state energy; its accuracy depends on the choice of trial states.

## Procedure
The procedure of the variational method can be generalized with the following steps:

1. Choose a **normalized trial function** $|\psi\rangle$ with one or more free parameters.
2. Compute $\langle H\rangle=\langle\psi|H|\psi\rangle$.
3. Minimize $\langle H\rangle$ with respect to those parameters.