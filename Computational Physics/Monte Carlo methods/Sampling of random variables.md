# Sampling of random variables

Parent: [[Monte Carlo methods]]

Assume that uniform random numbers are available. We want to generate samples from other distributions, using the PDF and CDF concepts in [[Probability]].

## Projection sampling: a uniform rejection proposal

Let $f(x)$ be a normalized PDF supported on $[a,b]$, bounded by $H$: $0\leq f(x)\leq H$. The rectangular rejection algorithm is:

1. Draw $x'\sim\mathcal U(a,b)$.
2. Independently draw $y'\sim\mathcal U(0,H)$.
3. Accept $x'$ if $y'\leq f(x')$; otherwise reject it and repeat.

Accepted samples follow $f$. For normalized $f$, the acceptance probability is $1/[(b-a)H]$. Choose the smallest valid height, $H=\sup_x f(x)$, to avoid unnecessary rejections. A sharply peaked PDF inside a large box is inefficient.

This finite-box version cannot directly sample an unbounded-support target. That limitation does not apply to rejection sampling with a suitable nonuniform proposal.

The rectangular method extends to higher dimensions, but its acceptance probability can become very small. If independently accepted coordinates have individual acceptance probabilities $\alpha_j$, accepting an entire proposal only when every coordinate succeeds gives probability $\prod_j\alpha_j$. For independent targets, sampling each coordinate separately and retaining accepted coordinates avoids that particular joint rejection loss. General high-dimensional rejection can still suffer from the **curse of dimensionality**.

## A nonuniform proposal

Let $q(x)$ be a normalized proposal density that is easy to sample, and let $p(x)$ be the normalized target. Choose an **envelope constant** $M$ such that

$$
p(x)\leq Mq(x)
$$

everywhere on the target support. In particular, $q$ must not vanish where $p>0$. For normalized densities, $M\geq1$.

1. Draw $x'\sim q$.
2. Draw $u\sim\mathcal U(0,1)$ independently.
3. Accept $x'$ if $u\leq p(x')/[Mq(x')]$; otherwise reject and repeat.

Equivalently, draw a height uniformly between zero and $Mq(x')$ and accept it when it lies below $p(x')$. The joint density of a proposed value and acceptance is

$$
q(x)P(\text{accept}\mid x)=q(x)\frac{p(x)}{Mq(x)}=\frac{p(x)}M.
$$

Integrating gives $P(\text{accept})=1/M$. Conditioning on acceptance therefore gives the target density $p(x)$. A tighter envelope improves efficiency. Simply using $p(x)/q(x)$ without a valid scale factor is generally incorrect.

![[Computational Physics/Assets/rejection-sampling.png]]

*Rectangular rejection sampling for $p(x)=6x(1-x)$ on $[0,1]$. Blue proposals are accepted and orange proposals rejected; the dashed envelope has height $M=1.5$ for uniform $q=1$.*

## Inverse transform sampling

Let $F$ be the target CDF. Draw $u\sim\mathcal U(0,1)$ and set

$$
x=F^{-1}(u).
$$

For a continuous strictly increasing CDF, $F^{-1}$ is the ordinary inverse. In general, use the generalized inverse $F^{-1}(u)=\inf\{x:F(x)\geq u\}$, since a CDF is only guaranteed to be nondecreasing.

To see why this works in the smooth case, set $Y=F(X)$. Conservation of probability gives

$$
p_X(x)\,dx=p_Y(y)\,dy,
\qquad \frac{dy}{dx}=F'(x)=p_X(x).
$$

Thus $p_Y(y)=1$ on $(0,1)$. Reversing the transformation maps a uniform variable to the target. This method rejects no samples, but requires an available or numerically computable inverse CDF, which can itself be costly.
