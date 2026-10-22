# Equation scaling

Parent: [[Numerical foundations]]

**Equation scaling** rewrites a physical equation using dimensionless variables. Natural scales also help avoid unnecessarily large or small numerical values.

## Example: radioactive decay

Consider

$$
\frac{dN}{dt}+\lambda N=0,\qquad N(0)=N_0.\tag{1}
$$

$N$ is a count and therefore dimensionless, while $[t]=\mathrm{s}$ and $[\lambda]=\mathrm{s}^{-1}$. Assuming $\lambda>0$, define $\hat t=\lambda t$. By the chain rule,

$$
\frac{d}{dt}=\lambda\frac{d}{d\hat t}.
$$

Equation (1) becomes

$$
\frac{dN}{d\hat t}+N=0.\tag{2}
$$

Strictly, the representation of $N$ as a function has changed: if $N_t(t)$ is the original function and $N_{\hat t}(\hat t)$ its scaled representation, then

$$
N_{\hat t}(\hat t)=N_t(\hat t/\lambda),\qquad
N_{\hat t}(\lambda t)=N_t(t).
$$

Although every quantity in (2) is dimensionless, $N$ may still be large. For $N_0>0$, set $\hat N=N/N_0$. This gives

$$
\frac{d\hat N}{d\hat t}+\hat N=0,\qquad \hat N(0)=1.\tag{3}
$$

The solution is $\hat N(\hat t)=e^{-\hat t}$, and substitution restores $N(t)=N_0e^{-\lambda t}$.

## Why scale an equation?

In a scaled equation, the numerical step size is dimensionless. Its physical value is recovered from the chosen scale: here $\Delta\hat t=\lambda\Delta t$. Thus a change of physical units does not change the dimensionless problem.

Boundary intervals can also become simpler, for example $\hat x\in[0,1]$ instead of $x\in[0,10^8\,\mathrm{m}]$. Scaling prepares equations for [[Discretization and numerical differentiation]].
