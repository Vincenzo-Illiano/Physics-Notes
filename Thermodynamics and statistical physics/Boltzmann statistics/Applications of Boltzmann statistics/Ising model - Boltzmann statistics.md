%%This note has been partially reviewed but it's still mostly incomplete%%

Parent: [[Applications of Boltzmann statistics]]

In this note we will calculate the average energy and the average magnetization of a ferromagnet using the [[Ising model|2D Ising Model]]. 

## Microstates and observables

Let $L$ be the number of sites along each side, so the number of spins is $N=L^2.$A **microstate** specifies every spin:
$$
\mathbf s=(s_1,s_2,\ldots,s_N).
$$
The energy is given by
$$
E(\mathbf S)=-J\sum_{\langle k,l\rangle}s_ks_l,\qquad J>0,
$$
where each nearest-neighbour bond is counted once. Aligned spins lower the energy, which makes this a **ferromagnetic** model. In addition, we will use *periodic boundary conditions*, meaning that every spin has exactly four neighbours.

The **magnetization** is
$$
M(\mathbf S)=\sum_{i=1}^N s_i.
$$
The **energy degeneracy** $g(E)$ is the number of microstates with energy $E$.

![[Computational Physics/Assets/ising-lattice.png]]

*An illustrative spin configuration. Blue and orange denote $+1$ and $-1$ spins; the inset marks the four nearest neighbours of an interior site. This is a schematic, not an equilibrium simulation.*