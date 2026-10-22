# Probability

Parent: [[Monte Carlo methods]]

## Interpretations

In a **frequentist interpretation**, probability describes the limiting relative frequency of an outcome in repeated trials under the same conditions. For an event $A$, the observed frequency is $n_A/n$. Under independent identical trials, the law of large numbers relates it to $P(A)$ as $n\to\infty$. This is a mathematical convergence statement about random frequencies, not a guarantee for every possible sequence of outcomes.

In a **Bayesian interpretation**, probability quantifies uncertainty or plausibility given information. Subjective Bayesian approaches emphasize degrees of belief, while objective approaches seek rules for assigning probabilities with less dependence on personal judgment. Coherent betting odds provide one way to interpret numerical degrees of belief.

## Distributions

For a discrete random variable $X$, the probability mass function is $p_X(a)=P(X=a)$ and

$$
\sum_a p_X(a)=1.
$$

For a continuous variable with a probability density function (**PDF**) $p_X(x)$,

$$
P(a\leq X\leq b)=\int_a^b p_X(x)\,dx,\qquad
\int_{-\infty}^{\infty}p_X(x)\,dx=1.
$$

For a small interval, $P(a\leq X\leq a+dx)\approx p_X(a)\,dx$. A density is not itself a probability at a point. The notation $X\sim p_X$ means that $X$ follows that distribution.

The **cumulative distribution function (CDF)** is

$$
F_X(x)=P(X\leq x)=\int_{-\infty}^x p_X(t)\,dt.
$$

Where the derivative exists, $F_X'(x)=p_X(x)$: the **PDF is the derivative of the CDF**.

## Joint, marginal and conditional distributions

For two continuous variables, $p(x,y)$ is the **joint density**. The **marginal densities** are

$$
p_X(x)=\int p(x,y)\,dy,\qquad
p_Y(y)=\int p(x,y)\,dx.
$$

The conditional density $p(x\mid y)$ describes $X$ given $Y=y$. The product rule gives

$$
p(x,y)=p(x\mid y)p_Y(y)=p(y\mid x)p_X(x).
$$

Rearranging yields **Bayes' theorem**:

$$
p(x\mid y)=\frac{p(y\mid x)p_X(x)}{p_Y(y)},\qquad p_Y(y)>0.
$$

For discrete variables, use probability masses and sums instead of densities and integrals.

## Expectation values and moments

For a function $g(X)$,

$$
E[g(X)]=\langle g(X)\rangle=\int_D g(x)p_X(x)\,dx,
$$

when the expectation exists. Replace the integral with a sum for a discrete variable.

The $n$th **raw moment** is $E[X^n]$; the zeroth is one and the first is the mean $\mu=E[X]$. Moments about a reference $c$ are $E[(X-c)^n]$. For $c=\mu$, these are **central moments** $\mu_n$, with $\mu_0=1$ and $\mu_1=0$.

The **variance** is the second central moment, not the second raw moment:

$$
\operatorname{Var}(X)=\sigma^2=
\int_D(x-\mu)^2p_X(x)\,dx
=E[X^2]-E[X]^2.
$$

Its units are the square of the units of $X$. The **standard deviation** $\sigma=\sqrt{\operatorname{Var}(X)}$ has the same units as $X$.
