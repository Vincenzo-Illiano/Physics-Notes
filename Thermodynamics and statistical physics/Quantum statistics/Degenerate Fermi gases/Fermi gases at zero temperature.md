Parent: [[Degenerate Fermi gases]]

In this note we will discuss how to calculate some properties of fermi gases at zero temperature. In doing so, we will introduce the concept of **Fermi energy.** In addition, we will also calculate the pressure in a degenerate fermi gas due to the overlap of wavefunctions, known as **degenerate pressure**.

## Fermi energy

To calculate properties of degenerate fermi gases, we will start by assuming ${}T = 0{}$. In this case, eq. \eqref{eq:FDEB_Fermidirac} in [[Fermi-Dirac and Einstein-Bose distributions]] becomes a step function, meaning that all states with energy ${}\epsilon < \mu{}$ are full, while all the others are empty. At ${}T=0{}$, we will refer to ${}\mu(T=0){}$ as the **Fermi energy** ${}\epsilon_{F}{}$. 

The Fermi energy is determined by the number of fermions in the gas ${}N{}$, meaning that if we add more fermions we expect more states to be full and the Fermi energy to increase. To find the relationship between ${}\epsilon_{F}{}$ and ${}N{}$, assume that the fermions are in a cubic box of sidelength ${}L{}$. Then, the wave-functions of the fermions must be stationary waves (in the assumption that they are free) 
$$
\lambda_{n}=\frac{2L}{n}, \qquad n=1,2,\dots
$$
and this applies separately to ${}x, y{}$ and ${}z{}$. In other words, the state of a fermion is fully determined by ${}(n_{x},n_{y},n_{z}){}$, and its energy is given by de Broglie relation 
$$
\begin{equation}
\epsilon = \frac{p^{2}}{2m}=\frac{h^{2}}{8mL^{2}}(n_{x}^{2}+n_{y}^{2}+n_{z}^{2}).
\label{eq:DFG_energy}
\end{equation}
$$
When ${}N{}$ fermions are in the box, they fill states such that ${}\epsilon \leq \epsilon_{F}{}$, so 
$$
n_x^{2}+n_{y}^{2}+n_{z}^{2} \leq \frac{8mL^{2}\epsilon_{F}}{h^{2}}.
$$
This describes an eight of a sphere in ${}n{}$ space. Let ${}n_\text{max}{}$ be the radius of this sphere. Then 
$$
\epsilon_{F}= \frac{n_\text{max}^{2}h^{2}}{8mL^{2}}.
$$
At the same time, if there are many fermions, we expect the volume of this eight of sphere to be equal to ${}N / 2{}$ (because two fermions with opposite spin can occupy the same state). This is only true if the sphere is so large that we can neglect the fact that ${}n_{x,y,z}{}$ only take integer values. In this assumption
$$
\frac{2}{8}\frac{4}{3}\pi n_\text{max}^{3}=N \implies n_\text{max}=\left( \frac{3N}{\pi} \right)^{1/3}.
$$
Thus 
$$
\boxed{\epsilon_{F}= \left( \frac{3N}{\pi V} \right)^{2/3} \frac{h^{2}}{8m},}
$$
where we used ${}V = L^{3}{}$.

We define the **Fermi temperature** as the temperature where ${}kT = \epsilon_{F}{}$. In an electron gas, this temperature is usually much higher than room temperature. In general, we can assume that below the Fermi temperature we cannot apply Boltzmann statistics and treat the fermion gas as an ideal gas, as discussed in [[Ideal gas - Boltzmann statistics]].
## Average energy

The Fermi energy is the largest energy that a fermion in a degenerate fermi gas at zero temperature has. We thus expect the average energy to be somewhat less than the fermi energy. To calculate the total energy, we have to sum all the fermion energies in the gas 
$$
U = 2 \sum_{n_{x},n_{y},n_{z}} \epsilon (n_{x}, n_{y}, n_{z}),
$$
where ${}\epsilon{}$ is given by eq. \eqref{eq:DFG_energy}. This sum doesn't have a closed form solution. However, in the assumption that there are many fermions, we can approximate it with a volume integral in ${}n{}$ space 
$$
U = 2 \int_{n_{x}}\int_{n_{y}}\int_{n_{z}}d^{3} n\ \epsilon(\vec{n}).
$$
Since, as discussed above, the integration volume is an eight of a sphere, it's convenient to switch to spherical coordinates 
$$
dn_{x}dn_{y}dn_{z}=n^{2}\sin \theta  \ dn\  d\theta\ d\phi,
$$
thus 
$$
U = 2 \int_{0}^{n_\text{max}}n^{2} \epsilon(n^{2}) dn \int_{0}^{\pi/2}d\theta \int_{0}^{\pi/2}d \phi.
$$
Using that ${}\epsilon{}$ doesn't depend on ${}\theta{}$ or ${}\phi{}$, this simplifies to 
$$
\begin{equation}
U = 2 \pi \int_{0}^{n_\text{max}} n^{2} \epsilon (n^{2})dn = \frac{\pi h^{2}}{8mL^{2}}\int_{0}^{n_\text{max}}n^{4}dn= \frac{\pi h^{2}n_\text{max}^{5}}{40mL^{2}}=\frac{3}{5}N\epsilon_{F}.
\label{eq:DFG_U}
\end{equation}
$$
The average energy in a fermi gas at ${}T = 0{}$ is thus given by 
$$
\langle \epsilon \rangle  = \frac{3}{5}\epsilon_{F}.
$$
## Degeneracy pressure

Using the definition of pressure 
$$
P = -\left( \frac{ \partial U }{ \partial V }  \right)_{S,N},
$$
we can calculate the pressure in a degenerate fermi gas, known as **degeneracy pressure**. We get 
$$
P = \frac{2N\epsilon_{F}}{5V}=\frac{2}{3} \frac{U}{V}.
$$
This pressure is extremely higher than the pressure we measure experimentally, and the reason for this is that in reality fermions are, in most cases, not free particles. The degeneracy pressure, which is exclusively caused by the quantum properties of fermions and by Pauli exclusion principle, is thus cancelled by electrostatic forces. 

## References

See [[Thermodynamics and statistical physics/Sources|Sources]]