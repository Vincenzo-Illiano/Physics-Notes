Parent: [[Sampling of random variables]]

**Markov chain Monte Carlo (MCMC)** is a family of algorithms that generate samples by constructing a [[Markov chains]] whose stationary distribution is a chosen **target distribution** $p(x)$. Recording the chain's successive states gives a sample that approaches the target distribution in the long-run sense described below.

We write a state as $x$ for simplicity, but MCMC is often used in high-dimensional spaces where $x$ is a vector.

## Proposal and acceptance

In general, MCMC consists in the following steps. Assuming a starting state ${}x_{i}{}$ is chosen:

1. From the current state $x_i$, draw a candidate $x'$ from a **proposal distribution** $T(x_i\to x')$ that depends only on the current state.
2. Apply an acceptance rule: if accepted, set $x_{i+1}=x'$; if rejected, set $x_{i+1}=x_i$.
3. Record $x_{i+1}$ and repeat.

*Every iteration produces a next state, including a repeated state after rejection.* These repeated values are part of the sample and must be counted. In order for MCMC to work, we want to choose an acceptance rule such that regardless of the chosen proposal distribution and initial state, the generated Markov chain will be ergodic and have the target distribution as a stationary state distribution. 

For distinct states, the move probability, or transition density in the continuous case, factorizes as
$$
\operatorname{Prob}(x_i\to x')
=T(x_i\to x')A(x_i\to x'),
$$
where $A$ is the **acceptance probability**. The full transition rule also includes the probability of staying at the current state after rejection.

In this construction, the acceptance rule enforces **detailed balance** with respect to $p$:
$$
p(x_i)T(x_i\to x')A(x_i\to x')
=p(x')T(x'\to x_i)A(x'\to x_i).
$$
If this is true, then in the constructed Markov chain $p$ is stationary. 

Suitable ergodicity conditions are also needed for convergence from the chosen initial state. Detailed balance alone does not guarantee that the chain explores the whole target; it is a sufficient stationarity construction, rather than a requirement for every possible MCMC method.

## The Metropolis–Hastings algorithm

Starting at a state with positive target density ${}p(x){}$:

1. Sample $x'$ from $T(x_i\to x')$.
2. Calculate
$$
A(x_i\to x')=\min\left[1,
\frac{p(x')T(x'\to x_i)}{p(x_i)T(x_i\to x')}\right].
$$
3. Draw $r\sim\mathcal U(0,1)$.
4. If $r<A(x_i\to x')$, accept the candidate; otherwise keep the current state. Record the resulting state and repeat.

If the proposal is **symmetric**,
$$
T(x_i\to x')=T(x'\to x_i),
$$
the method is called the **Metropolis algorithm**, and
$$
A(x_i\to x')=\min\left[1,\frac{p(x')}{p(x_i)}\right].
$$
In this symmetric case, a move to a state with higher target density is always accepted, while a move to lower target density is accepted with probability $p(x')/p(x_i)$. For an asymmetric proposal, the proposal-density ratio also matters, so higher target density alone does not guarantee acceptance.

Only target-density ratios are needed. If $p(x)=\widetilde p(x)/Z$, then
$$
\frac{p(x')}{p(x_i)}=\frac{\widetilde p(x')}{\widetilde p(x_i)}.
$$
The unknown normalizing constant cancels, provided the target is normalizable. This is useful when $Z$ is difficult to compute, as in [[The Ising model]].

For positive forward and reverse target-weighted proposal densities, detailed balance fixes the ratio
$$
\frac{A(x_i\to x')}{A(x'\to x_i)}
=\frac{p(x')T(x'\to x_i)}{p(x_i)T(x_i\to x')}
\equiv R.
$$
It does not determine the two acceptance probabilities separately. Both must lie between zero and one. For a fixed proposal, we can make the pair as large as this constraint allows by setting the larger acceptance probability to one:

- If $R\geq1$, choose $A(x_i\to x')=1$ and $A(x'\to x_i)=1/R$.
- If $R<1$, choose $A(x'\to x_i)=1$ and $A(x_i\to x')=R$.

Thus the forward probability is $\min(1,R)$, giving the Metropolis–Hastings rule. Both probability flows then equal
$$
\min\bigl[p(x_i)T(x_i\to x'),\ p(x')T(x'\to x_i)\bigr],
$$
which verifies detailed balance. A candidate with zero target density, or zero reverse proposal density when the forward one is positive, is rejected.

There is flexibility in choosing $T$, but the resulting chain must be able to explore the relevant target support. The proposal can strongly affect how long a useful run takes. Maximizing pairwise acceptance for a fixed proposal does not by itself select the best proposal or guarantee rapid exploration.

## Burn-in

An infinitely long, appropriately ergodic run gives the correct occupation fractions and expectation values. In a finite run, the initial state can have a substantial effect. Starting in a region that should occur very rarely under $p$ may overrepresent that region in the recorded sample and bias estimated observables.

**Burn-in**, also called an equilibration period, is the pragmatic practice of discarding an initial part of the chain. The idea is to exclude a transient during which the chain is moving from its starting region toward more representative regions of the target.

There is no universal number or fraction of samples to discard. A practical approach is to examine **time-series plots** against iteration number:

- In one dimension, plot the sampled coordinate $x_i$.
- In many dimensions, inspect several coordinates or relevant derived quantities $f(x_i)$.
- Plot a running estimate of an expectation, for example $\overline f_n=n^{-1}\sum_{i=1}^n f(x_i)$.

A systematic early drift can suggest an initial transient. Apparent stabilization is useful evidence, but not proof of adequate exploration. Burn-in cannot repair a chain that remains trapped in an unrepresentative region, and it does not make the remaining samples independent.

![[mcmc-gaussian-burn-in.png]]

*Example of burn-in in the case of a gaussian walk*