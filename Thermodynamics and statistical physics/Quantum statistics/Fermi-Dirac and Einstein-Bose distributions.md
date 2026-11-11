Parent: [[Quantum statistics]]

In a quantum systems, particles can find themselves in different **quantum states,** which are often discretized. For this reason, variables such as energy are not continuous, but can only assume discrete values (e.g. multiples of ${}\epsilon{}$). 

Given a system with discretized quantum states, each with a different energy, an important quantity to calculate is the **occupancy** of a state with energy ${}\epsilon,{}$ which describes the *average number of particles in that state*. 
To compute this quantity the [[Grand canonical ensemble]] turns out to be particularly useful, as one can *take the quantum state itself as a system* which can have from ${}0{}$ to ${}N{}$ particles. This approach is interesting, as the system, being a quantum state, is not spatially distinct from the reservoir. This is not a problem, as these notions haven't been used in the derivation for Gibbs distribution.

Let then the system be a quantum state with energy ${}\epsilon{}$, which can contain some number of particles. In particular, a microstate of this system is solely defined by how many particles there are in that state. If the system has ${}n{}$ particles and we neglect the interaction between these particle, its energy is going to be ${}n \epsilon{}$. If we assume that the system is in thermal equilibrium with a reservoir (which in this case is simply the other states), then we can apply [[Grand canonical ensemble|Gibbs distribution]]: 
$$
p(n)= \frac{1}{\mathcal Z} e^{-(n\epsilon - \mu n)/ kT}, \tag 1
$$
and we can use this to compute the occupancy of that state.

The calculation of the occupancy is different whether the particles that make up the system are [[Bosons and fermions|bosons or fermions]], as in the latter case due to **Pauli exclusion principle** a state can only have 0 or 1 particle, whereas in the former case a state can have any number of particles.

## Fermi-Dirac distribution

In a system made entirely of fermions, ${}n{}$ can only be ${}0{}$ or ${}1{}$. In this case, the occupancy of a state is simply the probability of that state to have a particle, which is given by Eq. (1) 
$$
\boxed{p( \text{full}) = \bar{n}(\epsilon) = \frac{e ^{-( \epsilon - \mu )/kT}}{1 + e^{-(\epsilon - \mu)/ k T}}= \frac{1}{1+ e^{(\epsilon - \mu)/ kT}}}.
$$
This formula is known as the **Fermi-Dirac distribution**, and is very important to compute the properties of fermi gases, such as electron gases, which are fundamental to model electrons in metals.

## Bose-Einstein distribution

In a system made entirely of bosons, ${}n{}$ can go from ${}0{}$ to ${}\infty{}$. In this case, the grand partition function is 
$$
\mathcal Z = 1 + e^{-(\epsilon - \mu)/kT}+e^{-2(\epsilon - \mu)/kT}+\dots = \frac{1}{1 - e^{-(\epsilon-\mu)/kT}},
$$
where the sum only converges if ${}\epsilon > \mu{}$, which is a fundamental condition in boson gases. The occupation is thus given by 
$$
\bar{n}(\epsilon) = \sum_{n=0}^{\infty} nP(n)= \frac{1}{\mathcal Z} \sum_{n=0}^{\infty} ne^{-n(\epsilon - \mu) / kT}.
$$
This sum can be computed by defining ${}x = (\epsilon - \mu)/kT{}$. Then: 
$$
\sum_{n=0}^{\infty}ne^{-nx}= - \frac{ \partial  }{ \partial x } \sum_{n=0}^{\infty}e^{-nx}= - \frac{ \partial  }{ \partial x } \frac{1}{1-e^{-x}}=-\frac{ \partial \mathcal Z }{ \partial x },
$$
so 
$$
\boxed{\bar{n}(\epsilon) = -\frac{1}{\mathcal Z} \frac{ \partial \mathcal Z }{ \partial x } = \frac{1}{e^{(\epsilon - \mu)/kT}-1}}.
$$
This formula is known as **Bose-Einstein distribution**, and describe the occupancy of a system made of bosons. Interestingly, this goes to infinity as ${}\epsilon{}$ goes to ${}\mu{}$. 