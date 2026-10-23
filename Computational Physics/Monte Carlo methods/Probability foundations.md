Parent: [[Monte Carlo methods]]

In this note, we will discuss the basics of probability theory in order to develop further into Monte carlo methods.
## Interpretations

There are different interpretation of probability. Regardless of interpretation, however, the results remain identical.

In a **frequentist interpretation**, probability describes the limiting relative frequency of an outcome in repeated trials under the same conditions. For an event $A$, the observed frequency is $n_A/n$. Under independent identical trials, the probability of event ${}A{}$ is defined as the limit as ${}n \to \infty{}$ of the observed frequency.

In a **Bayesian interpretation**, probability quantifies uncertainty or plausibility given information. Subjective Bayesian approaches emphasize degrees of belief, while objective approaches seek rules for assigning probabilities with less dependence on personal judgment. Coherent betting odds provide one way to interpret numerical degrees of belief.

## Distributions

For a discrete random variable $X$, the probability mass function is $p_X(a)=\text{Prob}(X=a)$. The probability is normalized:
$$
\sum_a p_X(a)=1.
$$
For a continuous variable, we define the probability density function (**PDF**) $p_X(x)$. Again, the probability is normalized:
$$
\text{Prob}(a\leq X\leq b)=\int_a^b p_X(x)\,dx,\qquad
\int_{-\infty}^{\infty}p_X(x)\,dx=1.
$$
For a small interval, $P(a\leq X\leq a+dx)\approx p_X(a)\,dx$. A density is not itself a probability at a point. The notation $X\sim p_X$ means that $X$ follows that probability distribution.

The **cumulative distribution function (CDF)** is defined as
$$
F_X(x)=P(X\leq x)=\int_{-\infty}^x p_X(t)\,dt.
$$
Where the derivative exists, $F_X'(x)=p_X(x)$: the *PDF is the derivative of the CDF.*

## Joint, marginal and conditional distributions

For two continuous variables, $p(x,y)$ is the **joint density**, which describes the probability distribution for variable ${}x{}$ and ${}y{}$ symultaneously. The **marginal densities** are
$$
p_X(x)=\int p(x,y)\,dy,\qquad
p_Y(y)=\int p(x,y)\,dx.
$$
The conditional density $p(x\mid y)$ describes $X$ given that $Y=y$. The product rule gives
$$
p(x,y)=p(x\mid y)p_Y(y)=p(y\mid x)p_X(x).
$$
Rearranging yields a famous result, known as **Bayes' theorem**:
$$
p(x\mid y)=\frac{p(y\mid x)p_X(x)}{p_Y(y)},\qquad p_Y(y)>0.
$$
For discrete variables, use probability masses and sums instead of densities and integrals.

## Expectation values and moments

For a function $g(X)$, we define the expectation value of ${}g(X){}$
$$
E[g(X)]=\langle g(X)\rangle=\int_D g(x)p_X(x)\,dx,
$$
when integral exists. Replace the integral with a sum for a discrete variable.

The $n$-th **raw moment** is $E[X^n]$; the zeroth is one (due to normalization) and the first is the mean $\mu=E[X]$. Moments about a reference $c$ are $E[(X-c)^n]$. For $c=\mu,$these are **central moments** $\mu_n$, with $\mu_0=1$ and $\mu_1=0$.

The **variance** is defined as the second central moment:

$$
\operatorname{Var}(X)=\sigma^2=
\int_D(x-\mu)^2p_X(x)\,dx
=E[X^2]-E[X]^2.
$$

Where the last equality is obtained by expanding the square. Its units are the square of the units of $X$. The **standard deviation** $\sigma=\sqrt{\operatorname{Var}(X)}$ has the same units as $X$, and is often used to quantify how much ${}X{}$ fluctuates about its expectation value.
