# Floating point errors and FLOPs

Parent: [[Numerical foundations]]

Floating point arithmetic represents only finitely many real numbers. Its format is explained in [[Binary representation]]. Algorithmic approximations introduce additional errors even in exact arithmetic.

## Counting floating point operations

A **FLOP** is a floating point arithmetic operation. Addition, subtraction, multiplication and division are usually counted individually. FLOP counts roughly estimate arithmetic work, but memory access, hardware and operation latency also affect execution time.

A **fused multiply-add** computes $ab+c$ in one instruction with one final rounding; it is conventionally counted as **two FLOPs**. Division, square roots and transcendental functions have different costs, so counting operations is not the same as predicting runtime.

The loop

```python
for i in range(n):
    y[i] = a * y[i] + i
```

requires $2n$ arithmetic FLOPs, ignoring indexing and conversion overhead.

For dense $n\times n$ matrix multiplication,

$$
a_{ij}=\sum_{k=1}^n b_{ik}c_{kj}.
$$

Each element requires $n$ multiplications and $n-1$ additions. The direct algorithm therefore uses $n^2(2n-1)=2n^3-n^2$ FLOPs. Algorithms with lower asymptotic counts exist, but this count describes the direct method.

## Truncation and round-off

**Truncation error** comes from replacing an exact mathematical expression by an approximation, such as a finite Taylor expansion or finite difference. Reducing $h$ decreases the truncation error of a consistent finite difference formula.

**Round-off error** comes from finite numerical precision. For a normal result rounded to nearest, excluding overflow and underflow, a standard model is

$$
\operatorname{fl}(a)=a(1+\delta),\qquad |\delta|\leq u,
$$

where $u$ is the **unit roundoff** ($2^{-53}$ for binary64). Equivalently,

$$
|\operatorname{fl}(a)-a|\leq u|a|.
$$

For positive $a$, the reverse bound is

$$
\frac{\operatorname{fl}(a)}{1+u}\leq a\leq
\frac{\operatorname{fl}(a)}{1-u}.
$$

Relative accuracy is not a fixed absolute spacing: the spacing of representable numbers depends on their magnitude.

## Catastrophic cancellation

Consider rounding to four significant decimal digits:

$$
a=1.0054321,\qquad b=1.0040001,
$$

so $\operatorname{fl}(a)=1.005$ and $\operatorname{fl}(b)=1.004$. Their respective relative errors are approximately $4.30\times10^{-4}$ and $9.96\times10^{-8}$. However,

$$
a-b=0.0014320,\qquad
\operatorname{fl}(a)-\operatorname{fl}(b)=0.001.
$$

The difference has relative error

$$
\frac{|0.001-0.0014320|}{0.0014320}\approx0.302.
$$

Subtracting nearby approximations exposes their existing rounding errors and can destroy relative accuracy. This is **catastrophic cancellation**.

## Error analysis for a second derivative

For $u(x)=e^{2x}$, the exact derivative is $u''(x)=4e^{2x}$. Approximate it by

$$
D_h^2u(x)=\frac{u(x+h)-2u(x)+u(x-h)}{h^2}.
$$

Define the signed total error as the computed value minus the exact derivative:

$$
\Delta(h)=\Delta_{\mathrm{tr}}(h)+\Delta_{\mathrm{ro}}(h),\qquad
|\Delta(h)|\leq|\Delta_{\mathrm{tr}}(h)|+|\Delta_{\mathrm{ro}}(h)|.
$$

Taylor expansion gives

$$
\Delta_{\mathrm{tr}}(h)=\frac{h^2}{12}u^{(4)}(x)+O(h^4).
$$

The rounded numerator subtracts nearby function values. Treating their rounding errors as order $u|u(x)|$ gives the estimate

$$
|\Delta_{\mathrm{ro}}(h)|\lesssim C\frac{u|u(x)|}{h^2}.
$$

Here $u$ without an argument is unit roundoff, whereas $u(x)$ denotes the function; $C$ accounts for the evaluations and arithmetic. The exact error also depends on operation order. For a nonzero second derivative, a relative error model is

$$
|\epsilon(h)|\lesssim C_1h^2+C_2\frac{u}{h^2}.
$$

Thus reducing $h$ first improves truncation error, but eventually amplifies round-off. The two terms have log–log slopes $+2$ and $-2$ within the small-step approximation. Their balance predicts an optimal scale $h\sim(C_2u/C_1)^{1/4}$; the observed rounding error fluctuates around this model.

![[Computational Physics/Assets/derivative-error.png]]

*Binary64 second differentiation of $e^{2x}$ at $x=1$. The curves show the competing error scales; they are not a strict pointwise error bound.*

The triangle inequality used above does not require errors to be random, independent or systematic.
