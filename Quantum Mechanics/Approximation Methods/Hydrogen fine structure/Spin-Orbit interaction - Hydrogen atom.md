Parent: [[Hyrdogen fine structure|Hydrogen fine structure]]

In the [[Hydrogen atom]], the electron's spin magnetic moment interacts with the magnetic field associated with its motion relative to the proton. In this note we will use [[Time-indipendent perturbation theory]] to find a correction to the orbital energies which accounts for this effect. The dipole interaction is $-\boldsymbol\mu_e\cdot\mathbf B$, with
$$
\boldsymbol\mu_e=-g\frac{e}{2m_e}\mathbf S,
\qquad g\simeq2,
$$
where $e>0$ is the elementary charge.

## Spin–orbit Hamiltonian

For a heuristic picture, consider a circular orbit of radius $r$ and period $T$. In the electron's instantaneous rest frame, the proton's apparent motion gives a current $I=e/T$. Using the field $\mu_0 I/(2r)$ at the centre of a circular loop and $|\mathbf L|=m_e r^2(2\pi/T)$ gives
$$
\mathbf B=\frac{\mu_0 e}{4\pi m_e r^3}\mathbf L.
$$
The electron's rest frame accelerates, so the naive dipole result must be corrected for something referred as **Thomas precession**. At this order the correction changes the prefactor from $g$ to $g-1$. With $\mu_0\varepsilon_0=c^{-2}$ and $\kappa=e^2/(4\pi\varepsilon_0)$,
$$
H_{\mathrm{so}}=(g-1)\frac{\kappa}{2m_e^2c^2r^3}\,\mathbf L\cdot\mathbf S.
$$
We use $g-1\simeq1$ below. This is just a heuristic picture, and a complete overview of this would require quantum electrodynamics.

## Good states basis for ${}H_\text{so}{}$

The product states $|n\ell m_\ell\rangle\otimes|s m_s\rangle$ are eigenstates of $H_0$, but $\mathbf L\cdot\mathbf S$ is not diagonal in that basis, which makes the calculation of the energy correction more cumbersome. To make matters simpler, we would like to find good states for ${}H_\text{so}{}$ (a basis where ${}H_\text{so}{}$ is diagonal) and then apply [[Degenerate time-independent perturbation theory]]. 

Using $\mathbf J=\mathbf L+\mathbf S$ we have that
$$
\mathbf L\cdot\mathbf S=\frac12(\mathbf J^2-\mathbf L^2-\mathbf S^2).
$$
This immediately shows that $|n\ell s j m_j\rangle$ forms a good states basis, where the operator on the right has eigenvalue $\frac{\hbar^2}{2}[j(j+1)-\ell(\ell+1)-s(s+1)]$. For the electron, $s=\tfrac12$, so the first-order shift is
$$
\Delta E_{\mathrm{so}}
=\frac{\kappa\hbar^2}{4m_e^2c^2}
\left[j(j+1)-\ell(\ell+1)-\frac34\right]
\langle n\ell s j m_j|r^{-3}|n\ell s j m_j\rangle. \tag 1
$$
Note that for $\ell=0$, $\mathbf L$ annihilates the orbital state, so the spin–orbit term vanishes. So we will only evaluate the radial expectation below for $\ell>0$.

We now want to find ${}\langle n\ell s j m_j|r^{-3}|n\ell s j m_j\rangle{}$, for which it is easier to come back to the product basis we were initially using. This can be done using **Clebsch–Gordan coefficients**
$$
|n\ell s j m_j\rangle
=C_+|n\ell,m_j-\tfrac12\rangle \otimes|\uparrow\rangle
+C_-|n\ell,m_j+\tfrac12\rangle \otimes|\downarrow\rangle, \tag 2
$$
since ${}m_{j}= m_{\ell} + m_{s}{}$ and where $|\uparrow\rangle=|\tfrac12,+\tfrac12\rangle$ and $|\downarrow\rangle=|\tfrac12,-\tfrac12\rangle$. The product states are orthonormal, so $|C_+|^2+|C_-|^2=1$.

Substituting (2) into (1) and using that 
$$
\bra{nlm} \frac{1}{r^{3}} \ket{ nlm} =\frac{1}{a_{0}^{3} n^{3}l\left( l+\frac{1}{2} \right)(l+1)},
$$
which can be found using [[Feynman-Hellmann theorem]], as shown in [[Relativistic correction - Hydrogen atom]], we find that
$$
\begin{aligned}
\langle n\ell s j m_j|r^{-3}|n\ell s j m_j\rangle
&=(|C_+|^2+|C_-|^2)
\frac{1}{a_0^3 n^3\ell(\ell+\tfrac12)(\ell+1)}\\
&=\frac{1}{a_0^3 n^3\ell(\ell+\tfrac12)(\ell+1)}.
\end{aligned}
$$
Also note that cross terms such as
$$
C_+^*C_-\,
\langle n\ell,m_j-\tfrac12|r^{-3}|n\ell,m_j+\tfrac12\rangle
\underbrace{\langle\uparrow|\downarrow\rangle}_{0}
$$
vanish.

## Energy shifts for the two branches

The angular factor 
$$
j(j+1)-\ell(\ell +1)-\frac{3}{4}
$$
in (1) is $\ell$ for $j=\ell+\tfrac12$ and $-(\ell+1)$ for $j=\ell-\tfrac12$. Using the definitions of $a_0$ and $\alpha$, we get, for $\ell>0$,
$$
{
\Delta E_{\mathrm{so}}=
\begin{cases}
-\dfrac{E_n^{(0)}\alpha^2}{2n^2}\,
\dfrac{n}{(\ell+\tfrac12)(\ell+1)}, & j=\ell+\tfrac12,\\[6pt]
+\dfrac{E_n^{(0)}\alpha^2}{2n^2}\,
\dfrac{n}{\ell(\ell+\tfrac12)}, & j=\ell-\tfrac12.
\end{cases}}
$$
Interestingly, the spin-orbit correction introduces an additional splitting, which depends on the value of ${}j{}$.

## References

See [[Quantum Mechanics/Sources|Sources]]