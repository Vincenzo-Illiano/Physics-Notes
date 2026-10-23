Parent: [[Computational physics]]

**Monte Carlo methods** use random samples to study a model. Common uses include high-dimensional integration and simulation of uncertain or statistical systems. The basic idea is to work with samples from a distribution instead of explicitly manipulating the full probability density.

## Topics

- [[Probability foundations]] — distributions, conditional probability, expectation values and variance.
- [[Sampling of random variables]] — rejection sampling and inverse transforms.
- [[Markov chains]] — introductory Markov-chain concepts.

## Basic approach

Assuming we can sample from the required distribution $p(x)$, a Monte Carlo approach consists in:

1. Draw a sample $x_i$ from $p(x)$.
2. Compute quantities of interest, such as $f(x_i)$, $g(x_i)$ or $h(f(x_i),g(x_i))$.
3. Store or accumulate the required values.
4. Repeat, then estimate averages, variances or other observables from the samples.

Ordinary software random-number generators are **pseudorandom**: deterministic algorithms produce sequences designed to behave statistically like random samples. Computers can also obtain randomness from physical sources, so true randomness is not fundamentally impossible on a computer. Sampling a nonuniform or high-dimensional target remains a separate algorithmic problem, dealt in [[Sampling of random variables]].

[[The Ising model]] is a physical application in these notes. Specialized Monte Carlo approaches can also treat some differential equations, but random sampling alone is not a general replacement for ordinary time-integration methods.