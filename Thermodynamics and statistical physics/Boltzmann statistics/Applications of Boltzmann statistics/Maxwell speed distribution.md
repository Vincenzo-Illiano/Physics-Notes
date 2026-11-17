Parent: [[Applications of Boltzmann statistics]]

In this note we will use [[Boltzmann statistics]] to derive the speed distribution of molecules in an ideal gas. 

Let ${}D(v){}$ be the probability distribution of the speed of molecules in an ideal gas. We must have that 
$$
D(v) = C \cdot \text{Prob}(\vec{v}) \cdot (\text{n of } \vec{v} \text{ such that } |\vec{v}| = v)
$$
where ${}C{}$ is a normalization constant and ${}\text{Prob}(\vec{v}){}$ is the probability that a molecule has velocity ${}\vec{v}{}$.

The first term is simply given by Boltzmann distribution 
$$
\text{Prob}(\vec{v}) = \frac{1}{Z}e^{-\beta E(\vec{v})}= \frac{1}{Z}e^{-m v^{2}/2kT},
$$
since the molecules are non interacting. 

To find the second term, we should think that, given a ${}v{}$, the number of vectors ${}\vec{v}{}$ such that ${}|\vec{v}|=v{}$ must be proportional to the area of a sphere in ${}v{}$-space, assuming that all directions are equally probable. Thus 
$$
D(v) = Cv^{2} e^{-mv^{2}/2kT},
$$
Where we included ${}1 / Z{}$ in the constant ${}C{}$. Imposing normalization, we get that 
$$
D(v)= \left( \frac{m}{2\pi kT} \right)^{3/2}4\pi v^{2}e^{-mv^{2}/2kT}.
$$
Using this result, we can compute a lot of useful quantities, such as the average speed of a molecule in the gas 
$$
\bar{v}=\sqrt{ \frac{8kT}{\pi m} }.
$$