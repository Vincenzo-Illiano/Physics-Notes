In this note, we will apply the [[Variational method]] to more precisely determine the ground state energy for the **helium atom**.

The Hamiltonian is
$$
H=-\frac{\hbar^2}{2m}\left(\nabla_1^2+\nabla_2^2\right)
-\frac{e^2}{4\pi\varepsilon_0}\left(\frac{2}{r_1}+\frac{2}{r_2}\right)
+V_{ee}, \tag 1
$$
where ${}\nabla_{1}, \nabla_{2}{}$ are intended respectively to the coordinates of the first and the second electron. The **electron-electron interaction** potential is
$$
V_{ee}=\frac{e^2}{4\pi\varepsilon_0}
\frac{1}{|\mathbf r_1-\mathbf r_2|}.
$$
In order to use the variational method, we need to choose a trial function. One useful option might be to use the trial function for the hamiltonian without the interaction term. In this case, the ground-state spatial wavefunction is the product of two hydrogen-like ground-state wavefunctions with nuclear charge $z=2$:
$$
\psi(\mathbf r_1,\mathbf r_2)
=\psi(\mathbf r_1)\psi(\mathbf r_2)
=\frac{z^3}{\pi a_0^3}
e^{-zr_1/a_0-zr_2/a_0},
$$
where $a_0$ is the Bohr radius.

We use this wavefunction as a trial state, treating $z$ as a **free parameter**. We expect the optimal value to lie between $1$ and $2$ (This is because we expect the "effective charge" to be the nucleus charge, minus some amount due to the electrons masking).

The trial wavefunction is an eigenstate of
$$
H'=-\frac{\hbar^2}{2m}\left(\nabla_1^2+\nabla_2^2\right)
-\frac{e^2}{4\pi\varepsilon_0}\left(\frac{z}{r_1}+\frac{z}{r_2}\right),
$$
with eigenvalue
$$
E=2z^2E_1^{\mathrm H},
\qquad E_1^{\mathrm H}\simeq-13.6\,\mathrm{eV}.
$$
It's useful to write ${}H{}$ in terms of ${}H'{}$, as this will simplify the calculation of the expectation value. We can rewrite the original Hamiltonian as
$$
H=H'+\frac{e^2}{4\pi\varepsilon_0}
\left(\frac{z-2}{r_1}+\frac{z-2}{r_2}\right)+V_{ee}.
$$
Therefore:
$$
\begin{aligned}
\langle H\rangle
&=\langle\psi|H'|\psi\rangle\\
&\quad+\frac{e^2}{4\pi\varepsilon_0}(z-2)
\left(
\left\langle\psi\left|\frac{1}{r_1}\right|\psi\right\rangle
+\left\langle\psi\left|\frac{1}{r_2}\right|\psi\right\rangle
\right)
+\langle\psi|V_{ee}|\psi\rangle\\
&=2z^2E_1^{\mathrm H}
+\frac{2e^2}{4\pi\varepsilon_0}(z-2)
\left\langle\frac{1}{r}\right\rangle
+\langle V_{ee}\rangle,
\end{aligned}
$$
Where we used that, since ${}H{}$ is symmetric for ${}r_{1} \rightarrow r_{2}{}$, we must have 
$$
\left< \frac{1}{r_{1}} \right> = \left< \frac{1}{r_{2}} \right>
$$
