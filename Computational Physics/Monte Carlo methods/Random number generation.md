Parent: [[Monte Carlo methods]]

%%This note needs further development%%

In this note, we will discuss how computers can generate random samples from uniform distributions. This is necessary in order to be able to generate random samples from non uniform distributions, using methods such as rejection sampling or inverse transform sampling. 

We will limit our discussion to **pseudorandom number generators**, and will not discuss hardware components specific to random number generation.

The idea of pseudorandom number generators is to sample from deterministic sequences, which appear random. Different sequences can be generated from different **seeds**. We want such sequences to have the following properties:
- The numbers they generate are uniformly distributed
- There is no correlation between different numbers of the sequence
- The period (when the sequence begins to repeat itself) must be larger than the amount of numbers we need to generate

One of the most basic pseudorandom number generators is the **linear cengruential generator (LCG)**. Starting with the current element of the sequence, ${}n_{i}{}$, LCG generates ${}n_{i+1}{}$ with the following rule: 
$$
n_{i+1}= an_{i}+c \text{ mod m}.
$$
Where ${}0 \leq a <m, m > 0{}$ and ${}0 \leq N_{0} < m{}$. The performance and the period of LCG depends crucially on parameter choice. 