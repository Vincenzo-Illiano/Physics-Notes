Parent: [[Boltzmann statistics]]

In this note, we will derive a formula for the probability of finding a system in any particular microstate, when that system is in equilibrium with a large reservoir at a given temperature. The set of microstates of such a system is referred to as a **canonical ensemble**, whereas the same set for isolated systems is referred to as a **microcaconical ensemble**. 

Assume that the system ${}S{}$ is in microstate ${}s{}$ and in thermal equilibrium with a large reservoir ${}R{}$ (meaning that the ${}T{}$ of ${}S+R{}$ is held fixed). Clearly, since ${}s{}$ is a microstate, ${}\Omega_{S}(s)=1{}$, where with ${}\Omega_{S}{}$ we refer to the multiplicity of states of the system. Since the system and the reservoir together form an isolated system, from the fundamental assumption of statistical physics we deduce that 
$$
p(s)\propto\Omega _{S}(s)\cdot \Omega_{R}(s)=\Omega_{R}(s),
$$
where ${}p(s){}$ is the probability to find the system in state ${}s{}$. Taking the logarithm of this expression and multiplying by ${}kT{}$ we obtain 
$$
kT \ln(p(s))=kT \ln(\Omega_{R}(s))= S_{R}(s),
$$
where ${}S_{R}{}$ is the entropy of the reservoir. For two states ${}s_{1}{}$ and ${}s_{2}{}$, we thus have 
$$
\frac{p(s_{2})}{p(s_{1})} = e^{(S_{R}(s_{2})-S_{R}(s_{1}))/k}. \tag 1
$$
This can be rewritten using the thermodynamic identity: 
$$
dS_{R}=\frac{1}{T}(dU_{R}+PdV_{R}-\mu dN_{R}).
$$
If we assume that the system and the reservoir don't exchange particles, we can put ${}dN_{R}=0{}$. At the same time, if the system is small in comparison to the reservoir, we can assume that the term ${}P dV_{R}{}$ is negligible compared to the ${}dU_{R}{}$ term. Overall, we thus have 
$$ 
dS_{R}= \frac{dU_{R}}{T}=-\frac{dE}{T}, \tag 2
$$
where ${}dE{}$ is the energy of the system. Integrating this into eq. (1) we get
$$
\frac{p(s_{2})}{p(s_{1})}=e^{-(E(s_{2})-E(s_{1}))/kT}.
$$
Therefore 
$$
p(s_{2}) \propto e^{-\beta E(s_{2})}, \quad \text{where } \beta=\frac{1}{kT}.
$$
We define the inverse of the proportionality constant as the **partition function** ${}Z(T){}$. This way
$$
\boxed{\rule{0pt}{1ex} \ p(s)=\frac{1}{Z}e^{-\beta E(s)},} \tag 3
$$
which represents the probability to find the system in the microstate ${}s{}$ when the system is in thermal equilibrium with a thermal reservoir. 
Note that this does not contradict the fundamental assumption of statistical physics, since the system in question is *not* isolated. 

Since we expect probabilities to be normalized, we have that 
$$
1= \sum_{s}p(s)=\frac{1}{Z}\sum_{s}e^{-\beta E(s)} \implies \boxed{ \rule{0pt}{3ex} \ Z = \sum_{s} e^{- \beta E(s)} \ }
$$
Knowing the partition function of a system turns out to be particularly useful, as the latter can be used to determine a lot of other quantities. Properties of the partition function are discussed in more detail in [[Partition function]].

Also note that the probability distribution in eq. (3) describes the probability distribution of *microstates*, not energies. In other words 
$$
p(E)\neq \frac{1}{Z}e^{-\beta E(s)},
$$
since degeneracies must be accounted for.