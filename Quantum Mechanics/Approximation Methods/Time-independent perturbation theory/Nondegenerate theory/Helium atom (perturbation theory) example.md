Parent: [[Nondegenerate time-independent perturbation theory]]
Model: [[The Helium atom]]

In this note, we will look at the example of the Helium atom using non degenerate time-indipendent perturbation theory.

We estimate the helium ground-state energy by treating the **electron–electron repulsion** as a perturbation:
$$
H=H_0+\lambda V_{ee},\qquad
V_{ee}=\frac{e^2}{4\pi\varepsilon_0|\mathbf r_1-\mathbf r_2|}.
$$
Here $H_0$ describes the two noninteracting electrons in the field of a nucleus of charge $+2e$ (see [[The Helium atom]]). We set $\lambda=1$ after computing the correction.

## First-order ground-state energy

The unperturbed spatial ground state $|\psi_0^{(0)}\rangle$ is the product of two hyrdogen $1s$ orbitals with $Z=2$. Each orbital has energy $Z^2 E_1^{\mathrm H}$, so
$$
E_0^{(0)}=2Z^2 E_1^{\mathrm H}=8E_1^{\mathrm H},
\qquad E_1^{\mathrm H}\simeq-13.6\,\mathrm{eV}.
$$
The first-order correction is
$$
E_0^{(1)}
=\langle\psi_0^{(0)}|V_{ee}|\psi_0^{(0)}\rangle.
$$
In the variational helium example, we derived the expectation value for a product of hydrogen orbitals with charge parameter $z$:
$$
\langle V_{ee}\rangle=-\frac54 E_1^{\mathrm H}z.
$$
Here we use $z=2$, the nuclear charge in $H_0$, rather than the optimized charge from the variational calculation. Therefore,
$$
E_0^{(1)}=-\frac52E_1^{\mathrm H}\simeq+34.0\,\mathrm{eV},
$$
and
$$
{E_0\simeq E_0^{(0)}+E_0^{(1)}
=\frac{11}{2}E_1^{\mathrm H}\simeq-74.8\,\mathrm{eV}.}
$$
The variational estimate was about $-77.5\,\mathrm{eV}$, closer to the experimental value of about $-79.0\,\mathrm{eV}$. Despite this, with perturbation theory we can calculate higher order corrections and get closer to the experimental value, whereas with the variational method we can't estimate the error from our result.
