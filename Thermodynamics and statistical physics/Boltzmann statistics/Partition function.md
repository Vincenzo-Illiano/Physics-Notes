Parent: [[Boltzmann statistics]]

In this note, we will find some useful properties of the partition function ${}Z{}$ defined in the [[Canonical ensemble]] note as 
$$
\begin{equation}
Z = \sum_{s}e^{-\beta E(s)}, \qquad \text{where } \beta = \frac{1}{kT}.
\label{eq:PF_Z}
\end{equation}
$$
In particular, we will see how to use it in order to calculate quantities such as ${}\langle E \rangle{}$, ${}\mu{}$, ${}P{}$, etc. In addition, we will discuss how to calculate the partition function for composite systems, which will be particularly useful when working with the [[Ideal gas]].

## Average energy

We can use ${}Z{}$ to calculate ${}\langle E \rangle{}$ starting from eq. \eqref{eq:CE_avgvalue} in [[Canonical ensemble]] 
$$
\langle E \rangle = \frac{1}{Z}\sum_{s}E(s)e^{-\beta E(s)}.
$$
This formula can be conveniently rewritten as 
$$
\begin{equation}
\langle E \rangle =-\frac{1}{Z}\frac{ \partial  }{ \partial \beta } \sum_{s}e^{-\beta E(s)} = -\frac{1}{Z}\frac{ \partial Z }{ \partial \beta }.
\label{eq:PF_avgen}
\end{equation}
$$
This shows that the average energy can be computed by knowing the partition function alone. Similar identities can be found with ${}\langle E^{2} \rangle{}$ and other functions of the energy.

## Partition function and free energy

We have shown how to compute ${}\langle E \rangle{}$ using only the partition function, but we still don't know how to use it to calculate other quantities such as ${}S{}$, ${}P{}$ or ${}\mu.{}$In order to do this, we'll have to prove a relationship which links the partition function with **Helmoltz free energy** 
$$
\begin{equation}
F = U - TS. 
\label{eq:PF_helmoltz}
\end{equation}
$$
In particular, we will prove that
$$
\boxed{F = -kT \ln Z}
$$
In order to prove this, we will start with the partial derivative relation 
$$
\left( \frac{ \partial F }{ \partial T }  \right)_{V,N}=-S.
$$
Rewriting ${}S{}$ in terms of ${}U, T{}$ and ${}F{}$ using eq. \eqref{eq:PF_helmoltz}, we can rewrite this as 
$$
\begin{equation}
\left( \frac{ \partial F }{ \partial T }  \right)_{V,N}=\frac{F-U}{T}.
\label{eq:PF_Helmoltz_relation}
\end{equation}
$$
Since at fixed ${}V{}$ and ${}N{}$, ${}U{}$ and ${}F{}$ are functions of ${}T{}$, this is a differential equation for ${}F(T){}$. Let's now define ${}\tilde{F}= -kT\ln Z{}$. We can see that 
$$
\begin{aligned}
\left( \frac{ \partial \tilde{F} }{ \partial T }  \right)_{V,N} & =-k\ln Z -\frac{kT}{Z}\left( \frac{ \partial Z }{ \partial T }  \right)_{V,N}  \\
 & = -k\ln Z  -\frac{k\beta}{Z} \left( \frac{ \partial Z }{ \partial \beta }  \right)_{V,N}  \\
 & = \frac{\tilde{F}}{T} - \frac{U}{T} = \frac{\tilde{F} - U}{T}.

\end{aligned}
$$
In other words, ${}\tilde{F}(T){}$ follows the same differential equation as ${}F(T){}$. These equations are first order equations, so we can prove that ${}F(T)=\tilde{F}(T){}$ for any ${}T{}$ if we prove that they are equal for only one ${}T{}$. This is because of [[Cauchy's uniqueness and existence theorem]]. 

Let's prove then prove that ${}F(0)= \tilde{F}(0){}$. As we can see from eq. \eqref{eq:PF_helmoltz}, at this temperature 
$$
	F= U(0) := U_{0}.
$$
Since ${}T=0{}$, the only possible energy state is ${}U_{0}{}$. We must thus have 
$$
Z(0)= e^{-U_{0}/kT}.
$$
Therefore 
$$
\tilde{F}(0)=-kT \ln(Z(0))= U_{0}.
$$
Finishing our proof.

Now that we know the relationship between ${}Z{}$ and ${}F{}$, we can use ${}Z{}$ to find all other quantities using all the known relationships for ${}F{}$
$$
S = -\left( \frac{ \partial F }{ \partial T }  \right)_{V,N}, \quad P = -\left( \frac{ \partial F }{ \partial V }  \right)_{T,N}, \quad \mu= \left( \frac{ \partial F }{ \partial N }  \right)_{T,V},
$$
and substituting ${}F = -kT \ln Z{}$.

## Composite systems

We will now discuss how to find the partition function of composite systems. Let the system be composed of ${}N{}$ subsystems, which individually have partition functions ${}Z_{1}, Z_{2},\dots{}$. If these subsystems are single particles, we will refer to their states as **single particle states**. The partition function of the composite system is given by eq. \eqref{eq:PF_Z} 
$$
Z = \sum_{s}e^{-\beta E(s)},
$$
Where ${}s{}$ is the state of the system. Let's now assume that the subsystems which make up the system are non-interacting, meaning that ${}E(s)=E(s_{1})+E(s_{2})+ \dots{}$, where ${}s_{1}{}$, ${}s_{2}, \dots{}$, are the states of the single subsystems. Therefore 
$$
Z = \sum_{s}e^{-\beta E(s_{1})}e^{-\beta E(s_{2})}\dots.
$$
We will now distinguish between the case where the subsystems are **distinguishible** and the case where they are **indistinguishible**. In the first case, a microstate of the system ${}s{}$ is simply given by ${}s = (s_{1}, s_{2}, \dots){}$. Thus 
$$
\begin{aligned}
Z  & = \sum_{(s_{1}, s_{2}, \dots)}e^{-\beta E(s_{1})}e^{-\beta E(s_{2})}\dots  \\
 & = \sum_{s_{1}}e^{-\beta E(s_{1})}\sum_{s_{2}}e^{-\beta E(s_{2})}\dots  \\
 & = \prod_{i}Z_{i}.  \\
\end{aligned}
$$
In the case where the particles are indistinguishable, we need to pay attention to the fact that permutations of the states of the subsystems do not change the state of the overall composite system. Using the equation above would thus double count some of the states. To overcome this we should divide by ${}N!{}$. If we also consider the fact that for indistinguishable subsystems ${}Z_{1} = Z_{2} = \dots{}$, we have that 
$$
Z = \frac{1}{N!}Z_{1}^{N}.
$$
This, however, is only true if two subsystems cannot be in the same state. In general, this formula is only valid for non dense systems, where this assumption is generally true.

## References

See [[Thermodynamics and statistical physics/Sources|Sources]]