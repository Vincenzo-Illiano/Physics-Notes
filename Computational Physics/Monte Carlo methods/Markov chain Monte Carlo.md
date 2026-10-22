# Markov chain Monte Carlo

Parent: [[Monte Carlo methods]]

Markov chain Monte Carlo constructs a chain whose stationary distribution is the desired target, then uses states of that chain as samples. *The original notes currently cover only the introductory Markov-chain concepts below.*

A **Markov chain** is a random sequence for which the conditional distribution of the next state depends on the history only through the current state:

$$
P(X_{i+1}=x'\mid X_i=x_i,\ldots,X_0=x_0)
=P(X_{i+1}=x'\mid X_i=x_i).
$$

This is the **Markov property**, often described as memorylessness. It does not mean that successive states are independent. A **walker** starts in a state and samples a next state according to the transition rule at every iteration.

## Example: a random walk

The notes propose a walk on the integers $0,1,2,3,4$, with equal probabilities of moving to either neighbouring state in the interior. A boundary rule at $0$ and $4$ is still needed to define the chain fully; no particular rule is specified here.

The distribution does not necessarily lose its dependence on the initial state for an arbitrary chain. For a finite chain, irreducibility and aperiodicity guarantee convergence to a unique stationary distribution from any initial distribution. Boundary rules can affect these properties, so convergence cannot be asserted for the incomplete walk as stated.

## Example: socks in a duvet cover

Treat a sock as either outside or inside a duvet cover. In each washing-machine cycle, suppose an outside sock stays outside with probability $0.99$, while an inside sock exits with probability $0.005$.

With state order (outside, inside), the transition matrix is

$$
A=\begin{pmatrix}0.99&0.01\\0.005&0.995\end{pmatrix}.
$$

This is a simplified model assuming those two states contain all relevant information for the transition rule.

## Transition matrices

Use row-vector distributions and define

$$
A_{ij}=P(X_{m+1}=j\mid X_m=i),\qquad
\sum_j A_{ij}=1.
$$

For a time-homogeneous chain, $A$ does not depend on $m$. Starting from $\mathbf r^{(0)}$,

$$
\mathbf r^{(n)}=\mathbf r^{(0)}A^n.
$$

The element $(A^n)_{ij}$, rather than $A_{ij}$ itself, is the probability of going from $i$ to $j$ in $n$ steps. The vector describes the distribution of possible states, not a single walker's deterministic final state.

Continuous-state chains use a transition kernel in place of a finite matrix.
