Parent: [[Nondegenerate time-independent perturbation theory]]

In this note, we will use non degenerate time-indipendent perturbation theory to calculate the energy of a harmonic oscillator in a uniform electric field.

A particle of mass $m$ and charge $q$ in a one-dimensional harmonic potential and a uniform electric field $E$ along $x$ has Hamiltonian
$$
H=H_0+H',\qquad
H_0=\frac{p^2}{2m}+\frac12m\omega^2x^2,\qquad H'=-qEx.
$$
We can use perturbation theory treating ${}H'{}$ as our perturbation. The unperturbed energies are
$$
E_n^{(0)}=\left(n+\frac12\right)\hbar\omega.
$$

The probability densities of the eigenstates of ${}H_{0}{}$ are Gaussians, and are therefore even around ${}0{}$ for every $n$. Since $x$ is odd,
$$
E_n^{(1)}=-qE\langle n|x|n\rangle=0.
$$
So the first order correction cancels. In order to calculate any energy correction we must then calculate the second order correction 
$$
E_{n}^{2}=\sum_{k\ne n}
\frac{|\langle k|H'|n\rangle|^2}{E_n^{(0)}-E_k^{(0)}}
$$
Using the known results for the harmonic oscillator
$$
x=\sqrt{\frac{\hbar}{2m\omega}}(a+a^\dagger),\qquad
a|n\rangle=\sqrt n\,|n-1\rangle,\qquad
a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle,
$$
only $k=n-1$ and $k=n+1$ can contribute to the second-order sum, so:
$$
\begin{aligned}
E_n^{(2)}
&=\sum_{k\ne n}
\frac{|\langle k|H'|n\rangle|^2}{E_n^{(0)}-E_k^{(0)}}\\
&=\frac{\hbar q^2E^2}{2m\omega}
\left(\frac{n}{E_n^{(0)}-E_{n-1}^{(0)}}
+\frac{n+1}{E_n^{(0)}-E_{n+1}^{(0)}}\right)\\
&=\frac{q^2E^2}{2m\omega^2}\bigl[n-(n+1)\bigr]
=-\frac{q^2E^2}{2m\omega^2}.
\end{aligned}
$$
We can show that this result actually gives the correct value for the energy.
Completing the square gives
$$
H=\frac{p^2}{2m}
+\frac12m\omega^2\left(x-\frac{qE}{m\omega^2}\right)^2
-\frac{q^2E^2}{2m\omega^2}.
$$
The shifted coordinate $\tilde x=x-qE/(m\omega^2)$ describes an oscillator with the same frequency. The energy for this oscillator is thus given by:
$$
{E_n=\left(n+\frac12\right)\hbar\omega-\frac{q^2E^2}{2m\omega^2}.}
$$
Which is exact.
