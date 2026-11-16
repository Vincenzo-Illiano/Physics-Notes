Parent: [[Approximation methods]]

In this topic, we will discuss how to find approximate solutions to Schrödinger's equation for time-dependent hamiltonians, using a technique known as **time dependent perturbation theory**. 

## Schrödinger's equation in terms of ${}c_{n}{}$

In order to introduce time dependent perturbation theory, we first have to rewrite Schrödinger's equation in a more convenient way
$$
i \hbar \frac{ \partial  }{ \partial t } \ket{\psi(t)} = H \ket{\psi(t)}. \tag 1
$$
For a time indipendent hamiltonian, the solution is given by 
$$
\ket{\psi(t)}  = \sum_{n} c_{n}e^{ -iE_{n}t / \hbar} \ket{n},
$$
where ${}c_{n} = \left< n | \psi(0) \right>{}$ and ${}\ket{n}{}$ are the solutions to the **time-indipendent SE** 
$$
H \ket{n} = E_{n} \ket{n} .
$$
For a time dependent hamiltonian that can be written as 
$$
H(t) = H_{0} + \lambda H'(t),
$$
we might speculate the solution can be written as 
$$
\ket{\psi(t)} = \sum_{n} c_{n}(t) e^{-iE_{n}t/\hbar}\ket{n} , \tag 2
$$
where ${}c_{n}(t){}$ must be the solution of some differential equation and ${}c_{n}(0)=c_{n}{}$. To find this differential equation, we substitute eq. (2) into eq. (1). Doing so we get 
$$
\begin{aligned}
  i\hbar \frac{ \partial  }{ \partial t } \ket{\psi(t)}  & = i \hbar \frac{ \partial  }{ \partial t } \sum_{n}c_{n}(t)e^{-iE_{n}t/\hbar} \ket{n}  \\
 &  = i \hbar \sum_{n}\left( \dot{c}_{n}(t) -\frac{iE_{n}}{\hbar}c_{n}(t) \right)e^{-iE_{n}t / \hbar} \ket{n}  \\
 &  =(H_{0}+\lambda H'(t))\sum_{n}c_{n}(t)e^{-iE_{n}t / \hbar} \ket{n}.  
\end{aligned}
$$
Multiplying by ${}\bra{m}{}$ from the left, we get 
$$
\begin{aligned}
i \hbar \dot{c}_{m}(t)e^{-iE_{m}t / \hbar}+ E_{m}c_{m}(t)e^{-i E_{m}t/\hbar} \\
=  E_{m}c_{m}(t)e^{-i E_{m}t / \hbar} + \lambda \sum_{n} H'_{mn}(t)e^{-iE_{n}t / \hbar}c_{n}(t),
\end{aligned}
$$
from which we get 
$$
\dot{c}_{m}(t)= \frac{\lambda}{i \hbar} \sum_{n} H'_{mn}(t)e^{i\omega_{mn}t}c_{n}(t). \tag 3
$$
Where we defined 
$$
\omega_{mn} = \frac{E_{m} - E_{n}}{\hbar}, \qquad H'_{mn}= \bra{m} H'(t) \ket{n} .
$$
In general, solving eq. (3) for every ${}m{}$ gives us the exact solution to eq. (1). Doing this analytically might be very hard, especially as ${}m{}$ gets higher. Now we will therefore show how to find approximate perturbative solutions.

## Perturbative solutions

In order to find perturbative solutions, we will first write the integral solution of eq. (3) 
$$
c_{n}(t) = c_{n}(0) + \frac{\lambda}{i \hbar}\sum_{m}\int_{0}^{t}dt' H'_{nm}(t')e^{i \omega_{nm}t'}c_{m}(t'). \tag 4
$$
The problem in solving this is that to find ${}c_{n}(t){}$ we need to known ${}c_{m}(t'){}$, which is what we are looking for in the first place. We could, at the first order, assume that ${}c_{m}(t') \approx c_{m}(0){}$, and plug it in eq. (4). This gives us a solution in the first order of ${}\lambda{}$: 
$$
\text{first order: } \qquad c_{n}^{(1)}(t) \approx c_{n}(0) + \frac{\lambda}{i \hbar} \sum_{m}\int_{0}^{t}dt' H'_{nm}(t')e^{i\omega_{nm}t'}c_{m}(0). \tag 5
$$
This is not an exact solution, but is better than simply ${}c_{n} \approx c_{n}(0){}$. Thus if we now plug this in eq. (4) we should get an even better solution, this time to the second order of ${}\lambda{}$: 
$$
\text{second order:} \qquad c_{n}^{(2)}(t) \approx c_{n}(0) + \frac{\lambda}{i \hbar} \sum_{m} \int_{0}^{t}dt' H'_{nm}(t')e^{i \omega_{nm}t'}c_{m}^{(1)}(t).
$$
Ideally, if we keep doing this, we should converge to an exact solution. In most of these notes, we will stop to the first order. These solutions are known as **perturbative solutions**.

## Two state systems

Let's look for example at a system with only two states, ${}\ket{a}{}$ with energy ${}E_{a}{}$ and ${}\ket{b}{}$ with energy ${}E_{b}{}$. Let's assume that the initial state is an eigenstate with energy ${}E_{a}{}$, thus ${}c_{a}(0)=1, c_{b}(0)= 0{}$. Then: 
$$
c_{b}(t) \approx \frac{1}{i \hbar} \int_{0}^{t}dt'H'_{ba}(t')e^{i\omega_{0}t'},
$$
where ${}\omega_{0} = (E_{b}-E_{a}) / \hbar{}$. Since we started with an eigenstate ${}\ket{a}{}$, ${}c_{b}{}$ represents the probability that our system collapses into state ${}\ket{b}{}$ when observed after time ${}t{}$ 
$$
P_{a \to b}(t)= |c_{b}(t)|^{2} = \left|\frac{1}{\hbar} \int_{0}^{t}dt'H'_{ba}(t')e^{i\omega_{0}t'}  \right| ^{2}.
$$