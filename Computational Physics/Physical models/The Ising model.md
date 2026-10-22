# The Ising model

Parent: [[Computational physical models]]

The **two-dimensional Ising model**, also called the **Lenz–Ising model**, describes a square lattice of spins $s_i\in\{-1,+1\}$. Each spin interacts with its nearest neighbours horizontally and vertically, not diagonally. We consider ferromagnetic coupling and no external magnetic field.

The system is in thermal contact with a bath at temperature $T$. Thermal fluctuations allow spin configurations to change. Increasing temperature makes energetically unfavourable fluctuations less strongly suppressed; a particular spin-flip probability also depends on the energy change and the chosen dynamics or sampling algorithm.

## Microstates and observables

Let $L$ be the number of sites along each side, so the number of spins is $N=L^2$. A **microstate** specifies every spin:

$$
\mathbf S=(s_1,s_2,\ldots,s_N).
$$

The energy is

$$
E(\mathbf S)=-J\sum_{\langle k,l\rangle}s_ks_l,\qquad J>0,
$$

where each nearest-neighbour bond is counted once. Aligned spins lower the energy, which makes this a **ferromagnetic** model. A boundary convention is needed for a finite lattice; the original notes do not specify one.

The **magnetization** is

$$
M(\mathbf S)=\sum_{i=1}^N s_i.
$$

The **energy degeneracy** $g(E)$ is the number of microstates with energy $E$.

![[Computational Physics/Assets/ising-lattice.png]]

*An illustrative spin configuration. Blue and orange denote $+1$ and $-1$ spins; the inset marks the four nearest neighbours of an interior site. This is a schematic, not an equilibrium simulation.*

## Thermal equilibrium

The Boltzmann probability of a microstate is

$$
p(\mathbf S;T)=\frac{e^{-\beta E(\mathbf S)}}{Z},\qquad
\beta=\frac{1}{k_BT},\qquad
Z=\sum_{\mathbf S}e^{-\beta E(\mathbf S)}.
$$

Here $Z$ is the **partition function**. Grouping microstates with the same energy gives

$$
p_E(E;T)=\frac{g(E)e^{-\beta E}}{Z}.
$$

These distributions determine averages such as $\langle E\rangle$ and $\langle M\rangle$, from which thermodynamic quantities such as heat capacity and magnetic susceptibility can be obtained. [[Monte Carlo methods]] provide a numerical sampling approach.

## Temperature and lattice size

The aim is to study observables as functions of $T$ and $L$, and estimate the critical temperature in the thermodynamic limit $L\to\infty$. Below that temperature, the infinite system can have spontaneous magnetization; above it, spontaneous magnetization vanishes.

A finite lattice has a rounded crossover rather than a true thermodynamic singularity. Moreover, at zero field its fully sampled equilibrium distribution is invariant under flipping every spin, so $\langle M\rangle=0$ even when low-temperature configurations are strongly ordered. Quantities such as $\langle|M|\rangle$ distinguish this order without cancellation between opposite magnetizations.

For comparisons between lattice sizes, use observables per spin, for example $e=E/N$ and $m=M/N$.
