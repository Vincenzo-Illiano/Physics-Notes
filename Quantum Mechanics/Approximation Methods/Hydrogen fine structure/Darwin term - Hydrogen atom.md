Parent: [[Hydrogen fine structure|Hydrogen fine structure]]

The **Darwin term** is a relativistic contact interaction obtained from the Dirac equation. In this note, we will use it to find a correction to the energies on the [[Hydrogen atom]] orbitals. This is done by using [[Time-indipendent perturbation theory]] with perturbation
$$
H_{\mathrm D}=\frac{\pi\alpha\hbar^3}{2m_e^2c}\,\delta^{(3)}(\mathbf r),
$$
where $m_e$ is the electron mass and $\alpha=e^2/(4\pi\varepsilon_0\hbar c) \approx 1 / 137$.

## First-order energy shift

The perturbation is independent of spin, and within the fixed-$n$ eigenspace it is diagonal. Thus
$$
\begin{aligned}
\Delta E_{\mathrm D}
&=\frac{\pi\alpha\hbar^3}{2m_e^2c}
\int d^3\mathbf r\,\psi_{n\ell m_\ell}^*(\mathbf r)
\,\delta^{(3)}(\mathbf r)\,\psi_{n\ell m_\ell}(\mathbf r)\\
&=\frac{\pi\alpha\hbar^3}{2m_e^2c}\,|\psi_{n\ell m_\ell}(\mathbf 0)|^2.
\end{aligned}
$$
For $\ell>0$ the wavefunction vanishes at the origin, whereas $|\psi_{n00}(\mathbf 0)|^2=1/(\pi a_0^3 n^3)$, with $a_0$ the Bohr radius. Using $\hbar/(m_e c a_0)=\alpha$ and $E_n^{(0)}=-\hbar^2/(2m_ea_0^2n^2)$ gives
$$
{\Delta E_{\mathrm D}=-E_n^{(0)}\frac{\alpha^2}{n}\,\delta_{\ell0}.}
$$
For $\ell=0$ the shift is positive since $E_n^{(0)}<0$. No separate $\delta_{m_\ell0}$ is needed because $\ell=0$ already implies $m_\ell=0$.

## References

See [[Quantum Mechanics/Sources|Sources]]
