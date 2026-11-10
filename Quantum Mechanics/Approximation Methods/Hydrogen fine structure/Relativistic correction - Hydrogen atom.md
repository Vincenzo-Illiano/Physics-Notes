Parent: [[Hyrdogen fine structure|Hydrogen fine structure]]

In this note, we will show how to correct the [[Hydrogen atom]]'s orbitals and energy levels with a relativistic factor using [[Nondegenerate time-independent perturbation theory]]. We will take the proton to be fixed and let $m_e$ be the electron mass. The unperturbed Hamiltonian and bound-state energies are
$$
H_0=\frac{\mathbf p^2}{2m_e}-\frac{\kappa}{r},
\qquad
E_n^{(0)}=\frac{E_1^{(0)}}{n^2}
=-\frac{m_e\kappa^2}{2\hbar^2n^2},
\qquad
\kappa=\frac{e^2}{4\pi\varepsilon_0}.
$$
It is useful to write the Bohr radius and **fine-structure constant** as
$$
a_0=\frac{\hbar^2}{m_e\kappa},
\qquad
\alpha=\frac{\kappa}{\hbar c}=\frac{\hbar}{m_ec a_0} \approx \frac{1}{137},
\qquad
\frac{\kappa}{a_0}=-2E_1^{(0)}.
$$

In order to get the relativistic correction, we will start by subtracting the rest energy from the total relativistic energy, and then round up to the second order in ${}\mathbf{p}^{2}{}$. This gives
$$
\begin{aligned}
T_{\mathrm{rel}}
&=\sqrt{\mathbf p^2c^2+m_e^2c^4}-m_ec^2\\
&=\frac{\mathbf p^2}{2m_e}
-\frac{(\mathbf p^2)^2}{8m_e^3c^2}
+\mathcal O\!\left(\frac{(\mathbf p^2)^3}{m_e^5c^4}\right).
\end{aligned}
$$
The first term already appears in $H_0$, so the leading correction is
$$
H_{\mathrm{rel}}=-\frac{(\mathbf p^2)^2}{8m_e^3c^2}.
$$
The perturbation is rotationally invariant and independent of spin, so its matrix is diagonal in $\ell,m_\ell$ and spin. Hence the basis ${}\ket{n,\ell, m_{\ell}}\otimes \ket{s, m_{s}}{}$ is a basis of good states, and [[Degenerate time-independent perturbation theory|first-order perturbation theory]] gives us the energy correction. For $|\psi\rangle=|n\ell m_\ell\rangle$ (we can ignore the spin part, since ${}H_\text{rel}{}$ doesn't do any contribution to that), the energy correction is
$$
\begin{aligned}
\Delta E_\text{rel} & =\left< \psi| H_\text{rel}| \psi \right> = -\frac{1}{2m_{e}c^{2}} \bra{\psi} \frac{\mathbf{p}^{2}}{2m} \frac{\mathbf{p}^{2}}{2m} \ket{\psi}  \\
 & = -\frac{1}{2m_{e}c^{2}}\bra{\psi} \left( H_{0}+\frac{\kappa}{r} \right)\left( H_{0}+\frac{\kappa}{r} \right) \ket{\psi}  \\
 & = -\frac{1}{2m_ec^2}
\left[
(E_n^{(0)})^2+2E_n^{(0)}\kappa\left\langle\frac1r\right\rangle
+\kappa^2\left\langle\frac1{r^2}\right\rangle
\right].
\end{aligned}

$$

In order to determine ${}\left< 1 / r \right>{}$ and ${}\left<  1 / r^{2} \right>{}$, we can use the [[Feynman-Hellmann theorem]], which gives the first expectation value by treating $\kappa$ as a parameter. Since $\partial H_0/\partial\kappa=-1/r$,
$$
\left\langle\frac1r\right\rangle
=-\frac{\partial E_n^{(0)}}{\partial\kappa}
=\frac{m_e\kappa}{\hbar^2n^2}
=\frac{1}{a_0n^2}.
$$
The second expectation value can be determined using the same technique, and is
$$
\left\langle\frac1{r^2}\right\rangle
=\frac{1}{a_0^2n^3(\ell+\tfrac12)}.
$$
Using $\kappa/a_0=-2E_1^{(0)}$ and $E_n^{(0)}=-m_ec^2\alpha^2/(2n^2)$, the overall correction is:
$$
\begin{aligned}
\Delta E_{\mathrm{rel}}
=-\frac{2(E_n^{(0)})^2}{m_ec^2}
\left(\frac{n}{\ell+\tfrac12}-\frac34\right)
={E_n^{(0)}\frac{\alpha^2}{n^2}
\left(\frac{n}{\ell+\tfrac12}-\frac34\right).}
\end{aligned}
$$
The shift is negative, as expected from the sign of $H_{\mathrm{rel}}$.

## References

See [[Quantum Mechanics/Sources|Sources]]
