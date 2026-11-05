Parent: [[Monte Carlo methods]]

In this note, we will discuss how computers can generate random samples from uniform distributions. This is necessary in order to be able to generate random samples from non uniform distributions, using methods such as rejection sampling or inverse transform sampling. 

We will limit our discussion to **pseudorandom number generators**, and will not discuss hardware components specific to random number generation.

The idea of pseudorandom number generators is to sample from deterministic sequences, which appear random. Different sequences can be generated from different **seeds**. We want such sequences to have the following properties:
- The numbers they generate are uniformly distributed
- There is no correlation between different numbers of the sequence
- The period (when the sequence begins to repeat itself) must be larger than the amount of numbers we need to generate

One of the most used RNGs is the Mersenne-Twister random number generator. The standard version of this generator is called "MT19937" and has a period of ${}2^{19937}-1{}$ (quite a huge period).

## LCG and PCG

One of the most basic pseudorandom number generators is the **linear cengruential generator (LCG)**. Starting with the current element of the sequence, ${}n_{i}{}$, LCG generates ${}n_{i+1}{}$ with the following rule: 
$$
n_{i+1}= an_{i}+c \text{ mod m}.
$$
Where ${}0 \leq a <m, m > 0{}$ and ${}0 \leq N_{0} < m{}$. The performance and the period of LCG depends crucially on parameter choice. 

Another time of random number generator is the **permuted congruential generator** (PCG). This works just like the LCG, but at every sample it performs a permutation on the bits of the generated sample. This reduces the correlation between different samples.

This is the default random number generator of Numpy!!

## RNG testing

In order to test the quality of pseudo RNGs, statistical tests are used. The most trivial one is a **frequency test**, where bins are filled with the generated numbers. If ${}N{}$ numbers are generated and ${}k{}$ bins are used, we expect every bin to have ${}\frac{N}{k} \pm \sqrt{\frac{N}{k} }{}$ samples. This would prove that the samples are uniformly distributed.
A similar test can similarly be done in two dimensions, sampling the couples ${}(x_{i}, x_{i+1}){}$ and testing that they are evenly distributed in the two dimensional space. This can be generalized to any dimension.

The frequency test tests for the uniformity of the generated samples. In order to test for the correlation between the samples, an **autocorrelation test** is used. This tests that the correlation between ${}x_{i}{}$ and ${}x_{i+k}{}$ is compatible with ${}0{}$ for any ${}k{}$. In particular:
$$
r_{k}= \frac{\sum_{i=1}^{N-k}(x_{i}-\bar{x})(x_{i+k}-\bar{x})}{\sum_{i=1}^{N}(x_{i}-\bar{x})^{2}}
$$
must be compatible with ${}0 \pm 1 / \sqrt{ N }{}$ (where ${}N{}$ is the number of samples generated to run the test).
