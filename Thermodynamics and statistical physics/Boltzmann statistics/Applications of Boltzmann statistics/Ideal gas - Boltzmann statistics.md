Parent: [[Applications of Boltzmann statistics]]

In this note we will use Boltzmann statistics to study the Ideal gas. In particular, we will assume that our gas is composed of ${}N{}$ indistinguishable non interacting particles, and that these particles are in a volume big enough such that we can consider them as generally being in separate quantum states. 

## Partition function of the ideal gas

Let ${}Z_{1}{}$ be the partition function of a single particle. The energy of such a particle can either internal (e.g. due to rotation, due to excited electrons, etc...) or due to its translational state. Since the internal and the translational states are interdependent, we can write 
$$
Z_{1} = \sum_{\text{trans. states}} \sum_{\text{int. states}} e^{-\beta (E_\text{tr}+E_\text{int})}= Z_\text{tr}Z_\text{int}.
$$
${}Z_\text{int}{}$ depends on the molecules which make up the gas. For now, we will only consider ${}Z_\text{tr}{}$. 

To calculate ${}Z_\text{tr}{}$, we need to count all the possible quantum states in which a particle can be. To do so, we'll start by considering a particle in a one dimensional box of size length ${}L{}$. Since the particle is free, its wave function is going to be a plane wave. In addition, since it cannot be on either side of the box, its wave length has to be
$$
\lambda = \frac{2L}{n}, \quad \text{ where } n = 1, 2, \dots
$$
Using De Broglie relation[^1], we can find the energy associated with each wave length 
$$
E_{n}= \frac{p_{n}^{2}}{2m}= \frac{h^{2}}{2m \lambda_{n}}= \frac{h^{2}n^{2}}{8mL^{2}}.
$$
Note that every ${}n{}$ corresponds to a different state of the particle and, in this case, there are no degeneracies. For a particle in three dimensions in a box with side length ${}L{}$ we must consider separately each dimension, so 
$$
E_{n_{x},n_{y},n_{z}} = \frac{h^{2}}{8mL^{2}}(n_{x}^{2} + n_{y}^{2} + n_{z}^{2}).
$$
The partition function is then given by 
$$
\begin{aligned}
Z_\text{tr} & = \sum_{n_{x}}\sum_{n_{y}}\sum_{n_{z}}e^{-h^{2}(n_{x}^{2} + n_{y}^{2} + n_{z}^{2})/8mL^{2}kT} \\
 & = \left( \sum_{n_{x}} e^{-h^{2}n_{x}^{2}/8mL^{2}kT} \right)\left( \sum_{n_{y}}\dots \right)\left( \sum_{n_{z}}\dots \right).
\end{aligned}
$$
If we assume that the energy levels are very close to one another, which is the case unless ${}L{}$ or ${}T{}$ are very small, we can approximate the sum with an integral 
$$
\sum_{n_{x}} e^{-h^{2}n_{x}^{2}/8mL^{2}kT} \approx \int_{0}^{\infty}e^{-h^{2}n_{x}^{2}/8mL^{2}kT}dn = \sqrt{ \frac{2\pi mkT}{h^{2}} }L = \frac{L}{\ell_{Q}},
$$
where we defined the **quantum length**
$$
\ell_{Q}= \sqrt{ \frac{h^{2}}{2\pi mkT} },
$$
which (roughly) represents the average length occupied by one wave in the box. Overall we have that 
$$
Z_\text{tr}= \frac{L^{3}}{\ell_{Q}^{3}} \implies Z_{1} = \frac{L^{3}}{\ell_{Q}^{3}}Z_\text{int}.
$$
To calculate the partition function of the entire gas, we can use eq. \eqref{eq:PF_composite_ind} in [[Partition function]], which describes the partition function of a composite system made of indistinguishable particles, in the assumption that these particles are generally in different states 
$$
Z = \frac{1}{N!}\left( \frac{VZ_\text{int}}{v_{Q}} \right)^{N}.
$$
Where ${}V{}$ is the volume of the box and ${}v_{Q}=\ell_{Q}^{3}{}$ is the **quantum volume**. When ${}V \gg v_{Q}{}$it means that many states are, in average, available, and we might assume that all the approximations that we made up to this point are more or less valid. These stop being true for very high density of particles or very low temperatures, where we necessarily need to resort to [[Quantum statistics]].

## Predictions

Now that we know the partition function of the ideal gas, we can use it to predict its statistical quantities. It's convenient to calculate ${}\ln Z{}$ first. This is 
$$
\ln Z= N[\ln V + \ln Z_\text{int} - \ln N-\ln v_{Q}+1],
$$
where we used [[Stirling's approximation]]. 

The energy ${}U{}$ is given by 
$$
U = -\frac{ \partial \ln Z }{ \partial \beta } =-N \frac{ \partial \ln Z_\text{int} }{ \partial \beta } +\frac{N}{v_{Q}}\frac{ \partial v_{Q} }{ \partial \beta } = U_\text{int}+\frac{3}{2}NkT,
$$
where we defined ${}U_\text{int}= N E_\text{int}{}$, where ${}E_\text{int}{}$ is the average energy of a particle due to its internal degrees of freedom. The second term is as we would expect from the [[Equipartition theorem]]. The first term usually also adds ${}kT/2{}$ terms for each internal degree of freedom, but these degree of freedoms usually freeze at very low temperatures. 

If we compute Helmoltz free energy we can compute the remaining quantities, as shown in [[Partition function]]. 
$$
F = -kT \ln Z= -NkT(\ln V-\ln N - \ln v_{Q}+1)+F_\text{int},
$$
where ${}F_\text{int}= -kT \ln Z_\text{int}{}$. Then 
$$
P = - \left( \frac{ \partial F }{ \partial V }  \right)_{T,N}=\frac{NkT}{V}.
$$
This is the equation of state of the ideal gas! In addition, we can compute the entropy and the chemical potential as well 
$$
S = -\left( \frac{ \partial F }{ \partial T }  \right)_{V,N}=Nk\left[ \ln\left( \frac{V}{Nv_{Q}} \right) + \frac{5}{2} \right]- \frac{ \partial F_\text{int} }{ \partial T },
$$
and
$$
\mu = \left( \frac{ \partial F }{ \partial N }  \right)_{V,T}= -kT\ln\left( \frac{VZ_\text{int}}{Nv_{Q}} \right).
$$
[^1]: In this context, using the de Broglie relation is the same as using more formally quantum mechanics

## References

See [[Thermodynamics and statistical physics/Sources|Sources]]