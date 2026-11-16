Parent: [[Time-dependent perturbation theory]]

In this note we will use [[Time-dependent perturbation theory]] to determine the time evolution of a state in a two state system which is perturbed with a harmonic hamiltonian 
$$
H'(t)= V \cos \omega t,
$$
where ${}V{}$ is a constant operator. In particular, 
$$
H'_{nm}(t) = \bra{n} H'(t) \ket{m} = V_{nm} \cos \omega t, \qquad \text{where } V_{nm} = \bra{n} V \ket{m}.
$$
Assume that ${}H_{0}{}$ only has two eigenstates, which we will refer to as ${}\ket{a}{}$ and ${}\ket{b}{}$. Let ${}\ket{\psi(t)}{}$ be such that ${}\ket{\psi(0)}= \ket{a}{}$. Then, from eq. (5) in [[Time-dependent perturbation theory]], we have that 
$$
\begin{aligned}
c_{b}(t) & = \frac{1}{i \hbar} \int_{0}^{t}dt' V_{ba}\cos\omega t' e^{i \omega_{0} t'}  \\
 & = \frac{1}{2i \hbar} \int_{0}^{t}dt' V_{ba}(e^{i(w+w_{0})t'}+e^{i(w_{0}-w)t'})  \\
 & = -\frac{V_{ba}}{2 \hbar} \left[  \frac{e^{i(w + w_{0})t}-1}{w+w_{0}} + \frac{e^{i(w_{0}-w)t}-1}{w_{0}-w}\right]. 
\end{aligned}\tag 1
$$
Where ${}\omega_{0}= (E_{b}-E_{a}) / \hbar{}$ and ${}c_{b}(t){}$ is defined in eq. (2) of [[Time-dependent perturbation theory]]. 

To simplify this solution we will use the **rotating-wave approximation**, which assumes that ${}|\omega - \omega_{0}| \ll \omega + \omega_{0}{}$, meaning that ${}\omega{}$ and ${}\omega_{0}{}$ are close in frequency compared to their size. When this is the case, we can neglect the first term in eq. (1), and we therefore have 
$$
\begin{aligned}
c_{b}(t)  & \approx - \frac{V_{ba}}{2 \hbar}\frac{e^{i(w + w_{0})t}-1}{w+w_{0}}  \\
 &  = -\frac{V_{ba}}{2\hbar} \frac{e^{i \frac{\omega_{0} - \omega}{2}t}\left( e^{i \frac{\omega_{0} - \omega}{2}t}-e^{-i \frac{\omega_{0} - \omega}{2}t} \right)}{w_{0}-w} \\
 &  = \frac{V_{ba}}{i\hbar} \frac{e^{i \frac{\omega_{0}-\omega}{2}t}\sin\left( \frac{\omega_{0}-\omega}{2}t \right)}{\omega_{0}-\omega}.
\end{aligned}
$$
Thus, the probability that we observe our system, which started from ${}\ket{a}{}$, to collapse into state ${}\ket{b}{}$, is given by 
$$
P_{a \to b}(t)= \frac{|V_{ba}|^{2}}{\hbar^{2}} \frac{\sin ^{2}\left(  \frac{\omega_{0}-\omega}{2}t \right)}{(\omega_{0}-\omega)^{2}}.
$$
Because of the ${}\sin{}$, the system oscillates between state ${}\ket{a}{}$ and state ${}\ket{b}{}$ with frequency ${}(\omega_{0}-\omega) / 2{}$. These oscillations are known as **Rabi oscillations**.