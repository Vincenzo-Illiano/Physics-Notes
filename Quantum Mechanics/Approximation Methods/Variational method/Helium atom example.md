Parent: [[Variational method]]

In this note, we will apply the [[Variational method]] to more precisely determine the ground state energy for the **helium atom**.

## Hamiltonian

The Hamiltonian is
$$
H=-\frac{\hbar^2}{2m}\left(\nabla_1^2+\nabla_2^2\right)
-\frac{e^2}{4\pi\varepsilon_0}\left(\frac{2}{r_1}+\frac{2}{r_2}\right)
+V_{ee}, \tag 1
$$
where $\nabla_1$ and $\nabla_2$ act on the coordinates of the first and second electron, respectively. The **electron-electron interaction** potential is
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
Here we used the symmetry of the chosen trial wavefunction under interchange of the two electrons, which gives
$$
\left< \frac{1}{r_{1}} \right> = \left< \frac{1}{r_{2}} \right>
$$
To complete the calculation, we need $\langle1/r\rangle$ and $\langle V_{ee}\rangle$.

## Expectation value of $1/r$

Since the trial wavefunction factorizes and each one-electron orbital is normalized, the integration over the second electron gives $1$. Thus, ${}\langle  \psi(\mathbf{r_{1}},\mathbf{r_{2}}) | 1/r_{1} | \psi(\mathbf{r_{1}},\mathbf{r_{2}}) \rangle= \left< \psi(\mathbf{r_{1}}), 1 / r_{1}, \psi( \mathbf{r}_{1}) \right>{}$ and
$$
\begin{aligned}
\left\langle\frac1r\right\rangle
&=\int |\psi(\mathbf r)|^2\frac1r\,d^3r\\
&=\frac{4z^3}{a_0^3}\int_0^\infty r e^{-2zr/a_0}\,dr\\
&=\frac{z}{a_0}\int_0^\infty u e^{-u}\,du
={\frac{z}{a_0}},
\end{aligned}
$$
where $u=2zr/a_0$ and we used
$$
\int_0^\infty u^n e^{-u}\,du=n!.
$$

## Electron-electron interaction

The expectation value of the interaction is
$$
\langle V_{ee}\rangle
=\frac{e^2}{4\pi\varepsilon_0}
\left(\frac{z^3}{\pi a_0^3}\right)^2
\iint\frac{e^{-2z(r_1+r_2)/a_0}}{|\mathbf r_1-\mathbf r_2|}
\,d^3r_1\,d^3r_2.
$$
This integral is not trivial, as it is effectively a 6 dimensional integral. In order to simplify it, we first calculate
$$
I_2(r_1)=\int\frac{e^{-2zr_2/a_0}}{|\mathbf r_1-\mathbf r_2|}\,d^3r_2,
\qquad
I_1=\int e^{-2zr_1/a_0}I_2(r_1)\,d^3r_1.
$$
For fixed $\mathbf r_1$, we can choose the polar axis parallel to $\mathbf r_1$. Then, using spherical coordinates
$$
I_2(r_1)=2\pi\int_0^\infty r_2^2e^{-2zr_2/a_0}\,dr_2
\int_0^\pi
\frac{\sin\theta_2\,d\theta_2}
{\sqrt{r_1^2+r_2^2-2r_1r_2\cos\theta_2}}.
$$
With $u=r_1^2+r_2^2-2r_1r_2\cos\theta_2$, the angular integral becomes
$$
\begin{aligned}
\int_0^\pi
\frac{\sin\theta_2\,d\theta_2}
{\sqrt{r_1^2+r_2^2-2r_1r_2\cos\theta_2}}
&=\frac{1}{2r_1r_2}\int_{(r_1-r_2)^2}^{(r_1+r_2)^2}\frac{du}{\sqrt u}\\
&=\frac{r_1+r_2-|r_1-r_2|}{r_1r_2}.
\end{aligned}
$$
Hence,
$$
I_2(r_1)=2\pi\int_0^\infty
\frac{r_2}{r_1}(r_1+r_2-|r_1-r_2|)e^{-2zr_2/a_0}\,dr_2.
$$
Since ${}I_{2}(r_{1}){}$ only depends on the radius ${}r_{1}{}$ and not on any angle, we can calculate ${}I_{1}{}$ by integration over the angles, which amounts to a multiplications by ${}4\pi{}$:
$$
I_1=8\pi^2\int_0^\infty\int_0^\infty
r_1r_2(r_1+r_2-|r_1-r_2|)
e^{-2z(r_1+r_2)/a_0}\,dr_1\,dr_2. \tag{2}
$$
Now use
$$
u=r_1+r_2,\qquad v=r_1-r_2,
\qquad r_1=\frac{u+v}{2},\quad r_2=\frac{u-v}{2}.
$$
This is useful as it enables us to get rid of the absolute value in (2). The absolute value of the Jacobian is
$$
\left|\det\frac{\partial(r_1,r_2)}{\partial(u,v)}\right|
=\left|\det\begin{pmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{pmatrix}\right|
=\frac12,
$$
and the integration region is $0\leq u<\infty$, $-u\leq v\leq u$. This can be easily noted by considering that this transformation rotates the ${}x{}$ and ${}y{}$ axis by ${}45 \degree{},$ therefore,
$$
\begin{aligned}
I_1
&=\pi^2\int_0^\infty e^{-2zu/a_0}\,du
\int_{-u}^{u}(u^2-v^2)(u-|v|)\,dv\\
&=2\pi^2\int_0^\infty e^{-2zu/a_0}\,du
\int_0^u(u^3-u^2v-uv^2+v^3)\,dv\\
&=2\pi^2\frac{5}{12}\int_0^\infty u^4e^{-2zu/a_0}\,du\\
&=2\pi^2\frac{5}{12}\left(\frac{a_0}{2z}\right)^5 4!
=\frac58\pi^2\left(\frac{a_0}{z}\right)^5.
\end{aligned}
$$
Substituting into the interaction expectation value,
$$
\langle V_{ee}\rangle
=\frac{e^2}{4\pi\varepsilon_0}
\left(\frac{z^3}{\pi a_0^3}\right)^2 I_1
=\frac58\frac{e^2}{4\pi\varepsilon_0}\frac{z}{a_0}
=-\frac54E_1^{\mathrm H}z.
$$

## Minimization

Using $e^2/(4\pi\varepsilon_0a_0)=-2E_1^{\mathrm H}$,
$$
\begin{aligned}
\langle H\rangle
&=2z^2E_1^{\mathrm H}
+2(z-2)\frac{e^2}{4\pi\varepsilon_0}\frac{z}{a_0}
-\frac54E_1^{\mathrm H}z\\
&=E_1^{\mathrm H}\left[2z^2-4z(z-2)-\frac54z\right]\\
&=E_1^{\mathrm H}\left(-2z^2+\frac{27}{4}z\right).
\end{aligned}
$$
The stationary-point condition is
$$
\frac{d\langle H\rangle}{dz}
=E_1^{\mathrm H}\left(-4z+\frac{27}{4}\right)=0,
$$
so
$$
\boxed{z_{\min}=\frac{27}{16}\simeq1.69.}
$$
As expected, $1<z_{\min}<2$.

The resulting energy is
$$
\boxed{\langle H\rangle_{\min}
=\frac{729}{128}E_1^{\mathrm H}\simeq-77.5\,\mathrm{eV},}
$$
close to the experimental value of approximately $-79.0\,\mathrm{eV}$.
