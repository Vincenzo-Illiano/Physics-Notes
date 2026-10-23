Parent: [[Sampling of random variables]]

Rejection sampling is a method to draw random variables from a given distribution ${}p_{X}{}$, especially useful when the given distribution is one dimensional and doesn't have high peaks, or when a similar trial distribution ${}q(x){}$ is known.

## Uniform proposal

Let $f(x)$ be a normalized PDF defined on $[a,b]$, bounded by $H$: $0\leq f(x)\leq H$. The **rectangular rejection algorithm** is:

1. Draw $x'\sim\mathcal U(a,b)$.
2. Independently draw $y'\sim\mathcal U(0,H)$.
3. Accept $x'$ if $y'\leq f(x')$; otherwise reject it and repeat.

Accepted samples follow $f$. For normalized $f$, the acceptance probability is $1/[(b-a)H]$. Choosing the smallest available height, $H=\sup_x f(x)$ avoids unnecessary rejections. A sharply peaked PDF inside a large box is inefficient with this algorithm.

This finite-box version cannot directly sample an unbounded-support target, but this limitation does not apply to rejection sampling with a suitable nonuniform proposal, which is discussed below.

The rectangular method extends to higher dimensions, but its acceptance probability can become very small. If independently accepted coordinates have individual acceptance probabilities $\alpha_j$, accepting an entire proposal only when every coordinate succeeds gives probability $\prod_j\alpha_j$. General high-dimensional rejection can suffer from the **curse of dimensionality**. For these reasons, rejection sampling is not suitable for high dimensional sampling, and other methods such as Markov chain Monte Carlo (MCMC) are more suitable.

## Nonuniform proposal

Let $q(x)$ be a normalized proposal density that we know how to sample from, and let $p(x)$ be the normalized target. Choose an **envelope constant** $M$ such that

$$
p(x)\leq Mq(x)
$$

everywhere on the target support. In particular, note that $q$ is only suitable for this method if it does not vanish where $p>0$. For normalized densities, $M\geq1$.

Then:
1. Draw $x'\sim q$.
2. Draw $u\sim\mathcal U(0,1)$ independently.
3. Accept $x'$ if $u\leq p(x')/[Mq(x')]$; otherwise reject and repeat.

Equivalently, draw a height uniformly between zero and $Mq(x')$ and accept it when it lies below $p(x')$. The joint density of a proposed value and acceptance is
$$
q(x)\text{Prob}(\text{accept}\mid x)=q(x)\frac{p(x)}{Mq(x)}=\frac{p(x)}M.
$$
Integrating gives $\text{Prob}(\text{accept})=1/M$. Conditioning on acceptance therefore gives the target density $p(x)$. A tighter envelope improves efficiency, as it decreases the number of rejections.

![[Computational Physics/Assets/rejection-sampling.png]]

*Rectangular rejection sampling for $p(x)=6x(1-x)$ on $[0,1]$. Blue proposals are accepted and orange proposals rejected; the dashed envelope has height $M=1.5$ for uniform $q=1$.*