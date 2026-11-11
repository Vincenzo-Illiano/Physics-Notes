Parent: [[Hydrogen fine structure]]

In this note, we will add a correction to the [[Hydrogen atom|hydrogen atom]] orbitals energies, which introduces a very small energy splitting called **hyperfine splitting**. 

Because both proton and electron are spin-1/2 particles with magnetic moments
$$
\boldsymbol{\mu}_p = \frac{g_p e}{2m_p}\mathbf{S}_p,
\qquad
\boldsymbol{\mu}_e = -\frac{g_e e}{2m_e}\mathbf{S}_e,
$$
where ${}g_{p} \approx 5.59{}$ and ${}g_{e} \approx 2{}$, there is an interaction between the electron magnetic moment and proton $B$-field
$$
\begin{aligned}
H_{\mathrm{hf}}
&= -\frac{\mu_0}{4\pi r^3}
\bigl[3(\boldsymbol{\mu}_p\cdot\hat{\mathbf{r}})(\boldsymbol{\mu}_e\cdot\hat{\mathbf{r}})-\boldsymbol{\mu}_p\cdot\boldsymbol{\mu}_e\bigr]
-\frac{2\mu_0}{3}\boldsymbol{\mu}_p\cdot\boldsymbol{\mu}_e\,\delta^3(\mathbf{r}) \\
&= \frac{\mu_0g_pg_e e^2}{16\pi m_pm_e}
\left[\frac{3(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})-\mathbf{S}_p\cdot\mathbf{S}_e}{r^3}\right]
+\frac{2\mu_0g_pg_e e^2}{3m_pm_e}\mathbf{S}_p\cdot\mathbf{S}_e\,\delta^3(\mathbf{r})
\end{aligned}
$$
In general, the effect of this on the total energy is hard to compute exactly for any state. We can simplify the problem by only considering spherically symmetric $\ell = 0$ and $m_\ell = 0$ states $|n00\rangle$.

For these the dipole–dipole interaction simplifies
$$
\begin{aligned}
&\langle n00|\frac{3(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})}{r^3}|n00\rangle \\
&\qquad= 3\int d^3r\,\psi_{n00}^{*}(r)\frac{(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})}{r^3}\psi_{n00}(r) \\
&\qquad= 3\int dxdydz\,\psi_{n00}^{*}(r)\frac{(S_{px}x+S_{py}y+S_{pz}z)(S_{ex}x+S_{ey}y+S_{ez}z)}{r^5}\psi_{n00}(r).
\end{aligned}
$$
Multiplying out the parentheses we get cross-terms, e.g.
$$
S_{px}S_{ey}\int dxdydz\,\psi_{n00}^{*}(r)\frac{xy}{r^5}\psi_{n00}(r),
$$
which all vanish since $\psi_{n00}(r)$ is symmetric while $xy$ is antisymmetric under $x\to -x$. The only remaining terms are
$$
\begin{aligned}
  & \langle n00|\frac{3(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})}{r^3}|n00\rangle
 \\  & =
 3\int dxdydz\,\psi_{n00}^{*}(r)\frac{S_{px}S_{ex}x^2+S_{py}S_{ey}y^2+S_{pz}S_{ez}z^2}{r^5}\psi_{n00}(r).
\end{aligned}
$$

This can be simplified by considering that, for a general spherically symmetric function $f(r)$:
$$
\int d^3r\,x^2 f(r) = \int d^3r\,y^2 f(r) = \int d^3r\,z^2 f(r) = \frac{1}{3}\int d^3r\,r^2 f(r),
$$
and thus
$$
\langle n00|\frac{3(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})}{r^3}|n00\rangle
= \mathbf{S}_p\cdot\mathbf{S}_e\int d^3r\,\psi_{n00}^{*}(r)\frac{1}{r^3}\psi_{n00}(r).
$$
Using this, we have that
$$
\langle n00|\frac{3(\mathbf{S}_p\cdot\hat{\mathbf{r}})(\mathbf{S}_e\cdot\hat{\mathbf{r}})-\mathbf{S}_p\cdot\mathbf{S}_e}{r^3}|n00\rangle = 0.
$$
Therefore for $\ell = 0$ states the only surviving term in $H_{\mathrm{hf}}$ is $\delta^3(\mathbf{r})\mathbf{S}_p\cdot\mathbf{S}_e$.

If we further specialise to ground state $n = 1$, our degenerate state space is
$$
|100\rangle\otimes|m_{sp}\rangle\otimes|m_{se}\rangle\,,
$$
where $m_{sp}$ and $m_{se}$ take values $\pm 1/2$. The scalar product $\mathbf{S}_p\cdot\mathbf{S}_e$ means that the good states are the eigenstates $|S_{\mathrm{tot}},M_{\mathrm{tot}}\rangle$ of the total spin squared operator $S_{\mathrm{tot}}^2$ and $S_{z,\mathrm{tot}}$
$$
\mathbf{S}_{\mathrm{tot}}\equiv \mathbf{S}_p+\mathbf{S}_e\,,
$$
The first-order perturbation matrix is then diagonal, and its values are
$$
\begin{aligned}
&\frac{2\mu_0 g_p g_e e^2}{3m_p m_e}\langle 100|\,\delta^3(\mathbf{r})\,|100\rangle\,\langle S_{\mathrm{tot}},M_{\mathrm{tot}}|\mathbf{S}_p\cdot\mathbf{S}_e|S_{\mathrm{tot}},M_{\mathrm{tot}}\rangle \\
&= \frac{2\mu_0 g_p g_e e^2}{3m_p m_e}|\psi_{100}(0)|^2\,\langle S_{\mathrm{tot}},M_{\mathrm{tot}}|\frac{1}{2}\left(S_{\mathrm{tot}}^2-S_p^2-S_e^2\right)|S_{\mathrm{tot}},M_{\mathrm{tot}}\rangle \\
&= \frac{2\mu_0 g_p g_e e^2}{3m_p m_e}\frac{1}{\pi a_0^3}\frac{\hbar^2}{2}\left[S_{\mathrm{tot}}(S_{\mathrm{tot}}+1)-\frac{3}{4}-\frac{3}{4}\right] \\
&= -E_1\frac{4}{3}g_p g_e\frac{m_e}{m_p}\alpha^2\left[S_{\mathrm{tot}}(S_{\mathrm{tot}}+1)-\frac{3}{2}\right].
\end{aligned}
$$
Possible values for $S_{\mathrm{tot}}$ are 0 and 1, thus energy splits into two levels
$$
E_{\mathrm{hf}} = -E_1\frac{4}{3}g_p g_e\frac{m_e}{m_p}\alpha^2
\begin{cases}
\frac{1}{4}, & S_{\mathrm{tot}} = 1, \\
-\frac{3}{4}, & S_{\mathrm{tot}} = 0
\end{cases}
$$
with splitting
$$
\Delta E_{\mathrm{hf}} = -E_1\frac{4}{3}g_p g_e\frac{m_e}{m_p}\alpha^2 = 5.88\cdot 10^{-6}\ \mathrm{eV}
$$

Although of same order $\alpha^2$ as fine-structure splitting, the ratio of the electron to proton mass ($\sim 1/2000$) makes this splitting even smaller than fine structure, justifying the name **hyperfine splitting**.

Converting the energy difference to a frequency
$$
\Delta E_{\mathrm{hf}} = h\nu,\qquad \nu = 1420\ \mathrm{MHz},\qquad \text{or}\quad \lambda = 21\ \mathrm{cm}.
$$
Converting energy to a temperature (dividing by Boltzmann’s constant) gives 0.068 K.

The background temperature in the universe is about 2.7 K, thus both hyperfine levels of hydrogen will be populated everywhere in the universe. When spontaneous de-excitations of the upper level happens, the hydrogen atoms will send out radiation with a wavelength 21 cm. Looking for 21 cm radiation with radiotelescopes has been used with great success to map out the occurrence of hydrogen in our galaxy. This is an example of how science is interconnected in quite surprising ways: Knowing the (hyper)finest details in the spectrum of hydrogen is needed for the very big: Mapping our galaxy.

## References

See [[Quantum Mechanics/Sources|Sources]].
Note: this note was mostly copied from Olav Syljuåsen notes, which Are Raklev's notes (mentioned in [[Quantum Mechanics/Sources|Sources]]) are based on.