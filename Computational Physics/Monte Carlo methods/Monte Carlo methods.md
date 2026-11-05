Parent: [[Computational physics]]

**Monte Carlo methods** use random samples to study a model. Common uses include high-dimensional integration and simulation of uncertain or statistical systems. The basic idea is to work with samples from a distribution instead of explicitly manipulating the full probability density.

## Topics

- [[Probability foundations]] — distributions, conditional probability, expectation values and variance.
- [[Random number generation]] — generation of random numbers in computers.
- [[Sampling of random variables]] — rejection sampling, inverse transforms and Markov-Chain Monte Carlo.
- [[Markov chains]] — introductory Markov-chain concepts.
- [[Monte Carlo integration]] — usage of Monte Carlo methods for numerical integration 

## Basic approach

Assuming we can sample from the required distribution $p(x)$, a Monte Carlo approach consists in:

1. Draw a sample $x_i$ from $p(x)$.
2. Compute quantities of interest, such as $f(x_i)$, $g(x_i)$ or $h(f(x_i),g(x_i))$.
3. Store or accumulate the required values.
4. Repeat, then estimate averages, variances or other observables from the samples.

Ordinary software random-number generators are **pseudorandom**: deterministic algorithms produce sequences designed to behave statistically like random samples. This is discussed in [[Random number generation]]. Sampling a nonuniform or high-dimensional target remains a separate algorithmic problem, dealt in [[Sampling of random variables]].

[[The Ising model]] is a physical application in these notes. Specialized Monte Carlo approaches can also treat some differential equations, but random sampling alone is not a general replacement for ordinary time-integration methods.