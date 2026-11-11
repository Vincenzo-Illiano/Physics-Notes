Parent: [[Hydrogen fine structure]]

In this note, we will at the effect on the orbitals of the [[Hydrogen atom|hydrogen atom]] due to external magnetic fields. This is known as the **Zeeman effect**. 

When an hydrogen atom is in a magnetic field ${}\mathbf{B}{}$, the electron interacts with the field, adding a term to the hamiltonian known as the **Zeeman term**:
$$
H_{Z}= -(\mathbf{\mu}_{\ell}+\mu_{s}) \cdot \mathbf{B},
$$
where ${}\mu_{\ell}{}$ is the magnetic dipole that comes from the electron's angular momentum, while ${}\mu_{s}{}$ is the spin magnetic dipole 
$$
\mu_{\ell} = - \frac{e}{2m} \mathbf{L}, \qquad \mu_{s}=-g \frac{e}{2m} \mathbf{S}.
$$
In this note, we will assume ${}g \approx 2{}$. If we choose a coordinate system such that ${}\mathbf{B}{}$ is along the ${}z{}$ axis, we have 
$$
H_{Z} = \frac{e}{2m}B(L_{z}+2S_{z})=\frac{e}{2m}B(J_{z}+S_{z}).
$$
We will now distinguish between the case where ${}H_{Z}{}$ is comparable to ${}H_\text{rel}{}$, ${}H_{D}{}$, and ${}H_\text{so}{}$, which are respectively due to the [[Relativistic correction - Hydrogen atom|relativistic correction]], the [[Darwin term - Hydrogen atom|Darwin term]] and the [[Spin-Orbit interaction - Hydrogen atom|spin-orbit correction]], and the case where the other effects are negligible in comparison with ${}H_{Z}{}$. These two cases are known as the **weak field Zeeman effect** and the **strong field Zeeman effect**. In practice, the term "weak" is a little bit exaggerate in this case, since ${}H_{Z}{}$ does not dominate the other terms until ${}B > 12 \text{ T}{}$, which is far from a weak field.

## Weak field Zeeman effect

To determine the correction to the energies in a weak field, we will use [[Time-indipendent perturbation theory]]. The unperturbed hamiltonian in this case is 
$$
H_{0} = \frac{\mathbf{p}^{2}}{2m}-\frac{e^{2}}{4\pi \epsilon_{0}r}+H_\text{rel}+H_\text{so}+H_\text{D},
$$
with unperturbed energies 
$$
E_{nj}=E_{n}\left( 1+\frac{\alpha^{2}}{n^{2}}\left( \frac{n}{j+\frac{1}{2}}-\frac{3}{4} \right) \right).
$$
In order to be able to safely use [[Time-indipendent perturbation theory]], we should first check that the eigenstates of ${}H_{0}{}$ ${}\ket{n \ell j m_{j}}{}$ are good states, meaning that they diagonalize ${}H_{Z}{}$ in the degenerate subspace, which is obtained by varying ${}\ell{}$ and ${}m_{j}{}$ (since ${}E_{nj}{}$ doesn't depend on these two parameters). In other words, we must show that 
$$
\bra{n \ell' j m_{j}'} H_{Z} \ket{n \ell j m_{j}} \propto \delta_{\ell' \ell} \delta_{m_{j}'m_{j}}.
$$
We can do this explicitly 
$$
\begin{aligned}
\bra{n \ell' j m_{j}'} H_{Z} \ket{n \ell j m_{j}}   & = \frac{eB}{2m} \bra{n \ell' j m_{j}'} J_{z} + S_{z} \ket{n \ell j m_{j}}  \\
 & = \frac{eB}{2m}( \hbar m_{j}\delta_{\ell'\ell} \delta_{m_{j}'m_{j}}+ \bra{n \ell' j m_{j}'} S_{z} \ket{n \ell j m_{j}}).
\end{aligned}
$$
To calculate the second term, it's convenient to switch to a composite basis using Clebsch-Gordan coefficients 
$$
\ket{n \ell j m_{j}} = \alpha \ket{n \ell, m_{j}+1 / 2} \otimes \ket{\downarrow} + \beta \ket{n \ell, m_{j} - 1 / 2} \otimes \ket{ \uparrow}.
$$
Thus 
$$
\begin{aligned}
\bra{n \ell' j m_{j}'} S_{z} \ket{n \ell j m_{j}}   & = -\frac{\hbar}{2}|\alpha|^{2} \delta_{\ell \ell'}\delta_{m_{j}m_{j}'}+   \frac{\hbar}{2}|\beta|^{2} \delta _{\ell \ell'}\delta_{m_{j}m_{j}'}  \\
 & = \frac{\hbar}{2}( |\beta|^{2} - |\alpha|^{2})\delta_{\ell \ell'}\delta_{m_{j}m_{j}'}. 
\end{aligned}

$$
This shows that ${}H_{Z}{}$ is diagonal in the degenerate subspace and that ${}\ket{n \ell j m_{j}}{}$ are hence good states. 

Given this fact, we can calculate the energy correction 
$$
E_{Z}^{(1)} = \bra{n \ell j m_{j}}H_{Z} \ket{n \ell j m_{j}} = \frac{e\hbar B}{2m}\left( m_{j}+ \frac{1}{2}(2 |\beta|^{2} - 1) \right),
$$
where we used that ${}|\alpha|^{2} + |\beta|^{2} = 1{}$. In this case, it can be derived using Clebsch-Gordan tables (to find ${}\beta{}$) that this can be written as 
$$
E_{Z}^{(1)} = \frac{e\hbar}{2m}B\left( 1 \pm \frac{1}{2 \ell + 1} \right) m_{j}= \mu_{B}Bg_{\ell}m_{j},
$$
where we choose the ${}+{}$ when ${}j = \ell + 1 / 2{}$ and the ${}-{}$ when ${}j = \ell - 1 / 2{}$. Here we introduced the **Bohr magneton** 
$$
\mu_{B} = \frac{e\hbar}{2m} \approx 5.8 \cdot 10^{-5} \text{ eV/T},
$$
and the **Landé g-factor** 
$$
g_{\ell} = 1 \pm \frac{1}{2\ell + 1}.
$$
As we can see, external magnetic fields induce another split in the energies, which depends on ${}m_{j}{}$. 

## Strong field Zeeman effect

The strong field Zeeman effect is easier to treat than its weaker counterpart, as the only non negligible elements in the Hamiltonian are ${}H_{0}{}$ and ${}H_{Z}{}$ 
$$
H = H_{0} + H_{z} = \frac{p^{2}}{2m} - \frac{e^{2}}{4 \pi \epsilon_{0} r} + H_{Z}.
$$
In this case it's more convenient to use as unperturbed eigenstates ${}\ket{n \ell m_{\ell} m_{s}}{}$. Since ${}H_{Z}{}$ can be rewritten in terms of ${}L_{z}{}$ and ${}S_{z}{}$, it's trivial to see that these states are good states. The energy correction is then 
$$
\begin{aligned}
E_{Z}^{(1)}  &  = \bra{n \ell m_{\ell} m_{s}} H_{Z} \ket{n \ell m_{\ell} m_{s}}  \\
 & = \frac{eB}{2m}(\bra{n \ell m_{\ell} m_{s}} L_{z} + 2 S_{z} \ket{n \ell m_{\ell} m_{s}})  \\
 & = \frac{e\hbar B}{2m}(m_{\ell} + 2 m_{s}) = \mu_{B}B(m_{\ell}+ 2 m_{s}).
\end{aligned}
$$
These energy corrections are also known as the **Paschen-Back effect**.

## References

See [[Quantum Mechanics/Sources|Sources]].