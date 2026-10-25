Parent: [[Variational method]]

The **hydrogen molecular ion**, $\mathrm H_2^+$, consists of two protons and one electron. We apply the [[Variational method]] to estimate its energy and determine whether molecular binding occurs.

## Hamiltonian and trial state

In the **Born-Oppenheimer approximation**, we calculate the electronic state with the nuclei held fixed. Put the protons at $\mathbf0$ and $\mathbf R$, with separation $R=|\mathbf R|$, and define
$$
r_A=|\mathbf r|,\qquad r_B=|\mathbf r-\mathbf R|.
$$
Including proton-proton repulsion, the Hamiltonian at fixed $R$ is
$$
H=-\frac{\hbar^2}{2m}\nabla^2
-\frac{e^2}{4\pi\varepsilon_0}\left(\frac1{r_A}+\frac1{r_B}\right)
+\frac{e^2}{4\pi\varepsilon_0R}.
$$
Choose a **linear combination of atomic orbitals**:
$$
\Psi(\mathbf r)=A[\phi_A(\mathbf r)+\phi_B(\mathbf r)],
$$
where
$$
\phi_A=\frac{e^{-r_A/a_0}}{\sqrt{\pi a_0^3}},
\qquad
\phi_B=\frac{e^{-r_B/a_0}}{\sqrt{\pi a_0^3}}
$$
are normalized hydrogen ground-state orbitals, each with energy
$$
E_1^{\mathrm H}=-\frac{e^2}{8\pi\varepsilon_0a_0}\simeq-13.6\,\mathrm{eV}.
$$
The electron is in a superposition of states centered on the two protons. We calculate the energy as a function of $R$, then vary $R$ to find the equilibrium separation.

## Normalization

Define the real **overlap integral**
$$
N=\langle\phi_A|\phi_B\rangle.
$$
Then
$$
1=\langle\Psi|\Psi\rangle
=|A|^2(2+2N),
\qquad
\boxed{A=\frac1{\sqrt{2(1+N)}}.}
$$

## Energy expectation value

Remove the constant proton-proton repulsion by defining
$$
H'=H-\frac{e^2}{4\pi\varepsilon_0R}.
$$
Each orbital satisfies its own hydrogen Hamiltonian. Consequently,
$$
H'\Psi=E_1^{\mathrm H}\Psi
-A\frac{e^2}{4\pi\varepsilon_0}
\left(\frac{\phi_A}{r_B}+\frac{\phi_B}{r_A}\right).
$$
Taking the expectation value gives
$$
\begin{aligned}
\langle H\rangle
&=E_1^{\mathrm H}+\frac{e^2}{4\pi\varepsilon_0R}\\
&\quad-|A|^2\frac{e^2}{4\pi\varepsilon_0}
\left[
\left\langle\phi_A\left|\frac1{r_B}\right|\phi_A\right\rangle
+\left\langle\phi_A\left|\frac1{r_A}\right|\phi_B\right\rangle
+\left\langle\phi_B\left|\frac1{r_B}\right|\phi_A\right\rangle
+\left\langle\phi_B\left|\frac1{r_A}\right|\phi_B\right\rangle
\right].
\end{aligned}
$$
The four matrix elements form two equal pairs by interchange of the proton centers. Define the dimensionless integrals
$$
S=a_0\left\langle\phi_A\left|\frac1{r_B}\right|\phi_A\right\rangle,
\qquad
D=a_0\left\langle\phi_A\left|\frac1{r_A}\right|\phi_B\right\rangle,
\qquad x=\frac R{a_0}.
$$
Thus, using $e^2/(4\pi\varepsilon_0a_0)=-2E_1^{\mathrm H}$,
$$
\begin{aligned}
\langle H\rangle
&=E_1^{\mathrm H}+4|A|^2E_1^{\mathrm H}(S+D)
-\frac{2E_1^{\mathrm H}}x\\
&=\boxed{E_1^{\mathrm H}\left[1+\frac{2(S+D)}{1+N}-\frac2x\right].}
\end{aligned}
$$

## Evaluating the integrals

### Coulomb integral $S$

Take spherical coordinates centered on proton $A$, with the polar axis pointing towards $B$. The angular integral is
$$
\int\frac{d\Omega}{r_B}
=\frac{2\pi}{rR}(r+R-|r-R|)
=\frac{4\pi}{\max(r,R)}.
$$
With $t=r/a_0$, this gives
$$
\begin{aligned}
S
&=4\left[\frac1x\int_0^x t^2e^{-2t}\,dt
+\int_x^\infty te^{-2t}\,dt\right]\\
&=\boxed{\frac1x-\left(1+\frac1x\right)e^{-2x}.}
\end{aligned}
$$

### Overlap $N$ and integral $D$

For the product $\phi_A\phi_B$, use coordinates
$$
\mu=\frac{r_A+r_B}{R},\qquad
\nu=\frac{r_A-r_B}{R},
\qquad 1\leq\mu<\infty,\quad -1\leq\nu\leq1.
$$
Here
$$
r_A=\frac R2(\mu+\nu),\quad
r_B=\frac R2(\mu-\nu),\quad
d^3r=\frac{R^3}{8}(\mu^2-\nu^2)\,d\mu\,d\nu\,d\varphi,
$$
and $\phi_A\phi_B=e^{-x\mu}/(\pi a_0^3)$. Integrating over $\varphi$ and $\nu$,
$$
\begin{aligned}
N
&=\frac{x^3}{4}\int_1^\infty e^{-x\mu}\,d\mu
\int_{-1}^1(\mu^2-\nu^2)\,d\nu\\
&=\frac{x^3}{2}\int_1^\infty
\left(\mu^2-\frac13\right)e^{-x\mu}\,d\mu\\
&=\boxed{e^{-x}\left(1+x+\frac{x^2}{3}\right).}
\end{aligned}
$$
Similarly,
$$
\begin{aligned}
D
&=\frac{x^2}{2}\int_1^\infty e^{-x\mu}\,d\mu
\int_{-1}^1(\mu-\nu)\,d\nu\\
&=x^2\int_1^\infty\mu e^{-x\mu}\,d\mu
=\boxed{(1+x)e^{-x}.}
\end{aligned}
$$

## Energy curve and minimum

Substitution gives the explicit energy curve
$$
\boxed{
E(x)=E_1^{\mathrm H}\left[
1+2\frac{\dfrac1x-\left(1+\dfrac1x\right)e^{-2x}+(1+x)e^{-x}}
{1+\left(1+x+\dfrac{x^2}{3}\right)e^{-x}}
-\frac2x\right].
}
$$
Differentiating with respect to $x$ gives
$$
\frac{dE}{dx}=2E_1^{\mathrm H}
\left[
\frac{(S'+D')(1+N)-(S+D)N'}{(1+N)^2}
+\frac1{x^2}\right],
$$
where
$$
\begin{aligned}
N'&=-\frac{x(1+x)}3e^{-x},\\
D'&=-xe^{-x},\\
S'&=-\frac1{x^2}
+\left(2+\frac2x+\frac1{x^2}\right)e^{-2x}.
\end{aligned}
$$
Solving $dE/dx=0$ numerically gives
$$
\boxed{x_{\min}\simeq2.493,\qquad
R_{\min}\simeq2.493a_0\simeq1.32\times10^{-10}\,\mathrm m,}
$$
and
$$
\boxed{E_{\min}\simeq1.12966E_1^{\mathrm H}\simeq-15.36\,\mathrm{eV}.}
$$

![[Hydrogen molecule ion energy.png]]

At small $R$, proton-proton repulsion makes the energy diverge to $+\infty$. At large $R$, $N,D\to0$ and $S\sim1/x$, so $E\to E_1^{\mathrm H}$: the system separates into a hydrogen atom and a proton.

**A negative total energy alone does not establish molecular binding.** The relevant dissociation threshold is $E_1^{\mathrm H}$, rather than zero. Our minimum lies below that threshold, giving a binding-energy estimate
$$
\boxed{D_e=E_1^{\mathrm H}-E_{\min}\simeq1.76\,\mathrm{eV}.}
$$
The variational principle guarantees that the exact fixed-nuclei ground-state energy at this separation is no higher than our trial value. Thus this calculation predicts a bound molecular energy well. Here $D_e$ is the well depth; nuclear vibrational and rotational energies are not included.
