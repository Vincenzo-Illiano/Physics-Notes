Parent: [[Boltzmann statistics]]

In this note, we will state and prove the **equipartition theorem** using [[Boltzmann statistics]].

The equipartition theorem states that given a system in thermal equilibrium at temperature ${}T{}$, every *quadratic degree of freedom* contributes to the average energy of the system a term 
$$
\Delta U = \frac{1}{2}kT.
$$
This is, however, only true in the classical limit, where the states that the system can take are continuous. This is usually true at ${}T \gg 0{}$.

## Proof

Let ${}q{}$ be a variable of the system (like position or momentum) which contributes quadratically to the system's energy, meaning that 
$$
E(q)= cq^{2},
$$
where ${}c{}$ is some constant. The partition function of this system is given by 
$$
Z = \sum_{q}e^{-\beta cq^{2}}.
$$
Let's now assume that ${}q{}$ can take continuous values that range from ${}-\infty{}$ to ${}\infty{}$. Then, multiplying and dividing by ${}\Delta q{}$ and having ${}\Delta q \to 0{}$, we have that 
$$
Z = \frac{1}{\Delta q} \sum_{q}e^{-\beta cq^{2}}\Delta q = \frac{1}{\Delta q } \int_{-\infty}^{+\infty} e^{-\beta c q^{2}}dq.
$$
This is a **Gaussian integral**, and it evaluates to 
$$
Z = \frac{1}{\Delta q} \sqrt{ \frac{\pi}{\beta c} }=C \beta^{-1/2}.
$$
Using eq. \eqref{eq:PF_avgen} in [[Partition function]], we have that the contribution of ${}q{}$ to the average energy of the system is given by 
$$
\Delta U = - \frac{ \partial \ln Z }{ \partial \beta } =\frac{1}{2} kT.
$$
## References

See [[Thermodynamics and statistical physics/Sources|Sources]]