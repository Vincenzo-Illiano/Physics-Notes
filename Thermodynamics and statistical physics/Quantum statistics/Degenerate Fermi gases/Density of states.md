Parent: [[Degenerate Fermi gases]]

In the [[Fermi gases at zero temperature]] note, we discussed fermi gases in the case where ${}T = 0{}$. To be able to also discuss other temperatures we have to introduce a new concept, known as the **Density of states.** 

The density of states ${}g(\epsilon){}$ is a function which gives the number of quantum states available from energy ${}\epsilon{}$ to energy ${}\epsilon + d\epsilon{}$. Thus, the number of states in a given range of energies can be obtained by integrating ${}g(\epsilon){}$. The problem of determining the density of states is entirely a problem of quantum mechanics, and does not depend on thermal properties. We can, however, use our discussion about fermi gases at ${}T = 0{}$ to determine the density of states of a gas of free fermions in a volume ${}V{}$.

To do this, starting from the integral in eq. \eqref{eq:DFG_U} of [[Fermi gases at zero temperature]], we can change the variable of integration from ${}n{}$ to ${}\epsilon{}$, using eq. \eqref{eq:DFG_energy} of [[Fermi gases at zero temperature]]. In particular 
$$
n = \sqrt{ \frac{8mL^{2}}{h^{2}} }\sqrt{ \epsilon }, \quad dn = \sqrt{ \frac{8mL^{2}}{h^{2}} } \frac{1}{2\sqrt{ \epsilon }}d\epsilon.
$$
This way, the integral becomes 
$$
U = \int_{0}^{\epsilon_{F}}\epsilon \left[ \frac{\pi}{2} \left( \frac{8mL^{2}}{h^{2}} \right)^{3/2}\sqrt{ \epsilon } \right]d\epsilon.
$$
At the same time, if we knew the density of states, we could calculate the total energy by simply doing 
$$
U = \int_{0}^{\epsilon_{F}}\epsilon \ g(\epsilon)d\epsilon.
$$
Comparing these two equations, we deduce that the density of states of a gas of free fermions must be 
$$
\begin{equation}
g(\epsilon)= \frac{\pi(8m)^{3/2}}{2h^{3}}V \sqrt{ \epsilon }.
\label{eq:DFG_DOS}
\end{equation}
$$
Once we know the density of states, we can calculate all properties of fermi gases at any temperature. In particular, given a quantity ${}x(\epsilon){}$, it's total value in the gas will be 
$$
X = \int_{0}^{\infty}g(\epsilon) x(\epsilon) \frac{1}{1+e^{(\epsilon-\mu)/kT}}d\epsilon.
$$
For every value of the energy, we count how many fermions there are in average. This is given by ${}g(\epsilon)p(\epsilon){}$, where ${}p(\epsilon){}$ is Fermi-Dirac distribution. This we use as a weight for ${}x(\epsilon){}$, and we then sum over all possible energies. For example 
$$
\begin{equation}
N = \int_{0}^{\infty}g(\epsilon) \frac{1}{1+e^{ (\epsilon-\mu)/kT }}d\epsilon.
\label{eq:DFG_N}
\end{equation}
$$
Note that we are integrating from ${}0{}$ to ${}\infty{}$ since in a gas at ${}T > 0{}$ all states can possibly be occupied. Using eq. \eqref{eq:DFG_N}, we can solve for ${}\mu{}$ and find how this depends on the temperature. 

Heuristically, we can deduce that ${}\mu{}$ should decrease with temperature in a gas of free fermions. The reason for this is that we can see from eq. \eqref{eq:DFG_DOS} that the density of states increases with ${}\epsilon{}$. If ${}\mu{}$ were to remain the same, then, since Fermi-Dirac distribution is symmetric, the number of fermions that we would loose at ${}\epsilon < \mu{}$ would be less than the number of fermions that we would gain at ${}\epsilon > \mu{}$. Thus the number of fermions would change simply by changing the temperature. The only way to avoid this is by decreasing ${}\mu{}$ with temperatures.

With the density of states we can also calculate the total energy 
$$
\begin{equation}
U = \int_{0}^{\infty}\epsilon g(\epsilon) \frac{1}{1 + e^{ (\epsilon-\mu)/kT }}d\epsilon.
\label{eq:DFG_Uintegral}
\end{equation}
$$
In general, however, these expressions cannot be computed analytically. We can, however, use a series expansion to simplify the calculations, known as the [[Sommerfeld Expansion]].

## References

See [[Thermodynamics and statistical physics/Sources|Sources]]