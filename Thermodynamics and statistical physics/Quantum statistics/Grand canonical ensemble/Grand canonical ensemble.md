Parent: [[Thermodynamics and statistical physics]]

In this note, we will derive the probability distribution for the microstates of a system which can exchange particles with a large reservoir. Such a system describes what is known as a **Grand canonical ensemble**, and is described by the **Gibbs distribution**. As an example to apply Gibbs distribution, we will look at [[Carbon monoxide poisoning|carbon monoxide poisoning]].

Let ${}S{}$ be a small system in thermal equilibrium with a reservoir ${}R{}$ which can exchange particles with the reservoir. When deriving [[Canonical ensemble|Boltzmann distribution]] (see eq. (1)), we showed that given two microstates ${}s_{1}{}$ and ${}s_{2}{}$, the ratio between their probability is 
$$
\frac{p(s_{2})}{p(s_{1})}=e^{(S_{R}(s_{2})-S_{R}(s_{1})) / k}, \tag 1
$$
where ${}S_{R}{}$ is the entropy of the reservoir. We can calculate ${}S_{R}(s_{2})- S_{R}(s_{1}){}$ by invoking the thermodynamic identity
$$
dS_{R} = \frac{1}{T}(dU_{R}+PdV_{R}-\mu dN_{R}).
$$
Since the system and the reservoir can exchange particles ${}dN_{R}=-dN_{S} \neq 0{}$. We will however assume that ${}PdV_{R}{}$ is negligible in comparison to the two other terms. We therefore get 
$$
S_{R}(s_{2}) - S_{R}(s_{1}) = -\frac{1}{T}(E(s_{2})-E(s_{1})-\mu N(s_{2})+\mu N(s_{1})),
$$
where ${}E{}$ is the energy of the system, and ${}N{}$ is the number of particles of the system. Combining this equation with eq. (1), we get that 
$$
{p(s) =  \frac{1}{\mathcal Z} e^{-\beta(E(s)-\mu N(s))}\ }, \quad \beta = \frac{1}{kT} \tag 2
$$
where 
$$
\mathcal Z = \sum_{s} e^{-\beta (E(s)-\mu N(s))}
$$
is to ensure that ${}p{}$ is normalized over all the microstates ${}s{}$, and is referred to as the **Grand partition function** or **Gibbs sum**. Eq. (2) describes the **Gibbs distribution**, which is the probability distribution of the **Grand canonical ensemble**. The exponential ${}e^{-\beta(E - \mu N)}{}$ is called the **Gibbs factor**.

Whenever a system is composed of different chemical species with different chemical potentials (say for example ${}\mu_{A}{}$ and ${}\mu_{B}{}$), the thermodynamic identity contains the two species separately. Gibbs factor thus changes to 
$$
e^{-\beta(E(S)- \mu_{A}N_{A}(s) - \mu_{B}N_{B}(s) - \dots)}.
$$

## References

See [[Thermodynamics and statistical physics/Sources|Sources]]