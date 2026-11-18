Parent: [[Degenerate Fermi gases]]

In this note, we will discuss how to approximate the solutions for the integrals in eq. \eqref{eq:DFG_N} and \eqref{eq:DFG_Uintegral} in the [[Density of states]] note using a series expansion known as **Sommerfeld expansion**. These approximations will be valid in the limit ${}kT \ll \epsilon_{F}{}$. 

We want to calculate 
$$
\begin{equation}
N = \int_{0}^{\infty}g(\epsilon)p(\epsilon)d\epsilon=\int_{0}^{\infty}g(\epsilon) \frac{1}{1+e^{ (\epsilon-\mu)/kT }}d\epsilon.
\end{equation}
$$
The idea of Sommerfeld expansion is to use the fact that the derivative of Fermi-Dirac probability distribution is negligible when ${}\epsilon{}$ is far away from ${}\mu{}$. In order to use this, we will first integrate by parts. For simplicity, we will write ${}g(\epsilon)= g_{0} \sqrt{ \epsilon }{}$, where ${}g_{0}{}$ does not depend on ${}\epsilon{}$. 
$$
N = \frac{2}{3}g_{0}\epsilon^{3/2}p(\epsilon)\Big|_{0}^{\infty} + \frac{2}{3}g_{0}\int_{0}^{\infty}\epsilon^{3/2}\left( -\frac{dp(\epsilon)}{d\epsilon} \right)d\epsilon.
$$
Since ${}p(\epsilon){}$ goes to ${}0{}$ at ${}\infty{}$ exponentially, and ${}\epsilon^{3/2}{}$ goes to ${}0{}$ at ${}0{}$, the first term evaluates to ${}0{}$. The derivative of Fermi-Dirac distribution is given by 
$$
-\frac{dp(\epsilon)}{d\epsilon}= \frac{1}{kT} \frac{e^{ x }}{(e^{ x }+1)^{2}},
$$
where we defined ${}x = (\epsilon - \mu) / kT{}$. Thus, we want to calculate 
$$
N = \frac{2}{3}g_{0} \int_{-\mu / kT}^{\infty}  \frac{e^{ x }}{(e^{ x }+1)^{2}} \epsilon^{3/2}dx,
$$
where we changed integration variable to ${}x{}$. Since ${} \frac{e^{ x }}{(e^{ x }+1)^{2}} {}$ goes to ${}0{}$ at ${}-\infty{}$, we can as well calculate the integral from ${}-\infty{}$. In addition, we can expand ${}\epsilon^{3/2}{}$ in series around ${}\mu{}$, since this is the only place where the integrand is non negligible 
$$
\epsilon^{3/2}= \mu^{3/2} + (\epsilon - \mu) \frac{d}{d\epsilon} \epsilon^{3/2} \Big|_{\epsilon = \mu}+ \frac{1}{2}(\epsilon - \mu)^{2} \frac{d^{2}}{d\epsilon^{2}}\epsilon^{3/2}\Big|_{\epsilon = \mu} + \dots
$$
Using all these approximations we can calculate the integral for ${}N{}$. The final result is 
$$
N = \frac{2}{3}g_{0} \mu^{3/2} + \frac{1}{4}g_{0} (kT)^{2} \mu^{-1/2} \frac{\pi^{2}}{3} + \dots.
$$
Substituting the expression for the Fermi energy, we get that 
$$
\frac{\mu}{\epsilon_{F}} \approx 1 - \frac{\pi^{2}}{12}\left( \frac{kT}{\epsilon_{F}} \right)^{2}.
$$
As predicted in the [[Density of states]] note, ${}\mu{}$ decreases with temperature. 

Using the same ideas we can also approximate the integral for the energy to get the dependence of ${}U{}$ on ${}T{}$. This is particularly useful for estimating the heat capacity. 
$$
U \approx \frac{3}{5}N \epsilon_{F} + \frac{\pi^{2}}{4}N \frac{(kT)^{2}}{\epsilon_{F}}.
$$
From this, we deduce that the heat capacity goes to ${}0{}$ linearly as ${}T{}$ goes to ${}0{}$. 

## References

See [[Thermodynamics and statistical physics/Sources|Sources]].