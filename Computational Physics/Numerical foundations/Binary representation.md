# Binary representation

Parent: [[Numerical foundations]]

A **bit** stores one of two logical values, conventionally $0$ and $1$. Computers represent numbers using finite sequences of bits.

## Integer representation

For a nonnegative integer, positional notation gives

$$
a=\sum_i d_{10}^i10^i=\sum_i d_2^i2^i,
$$

where $d_2^i\in\{0,1\}$. To convert from decimal to binary, repeatedly divide by two and read the remainders from bottom to top:

| Division | Quotient | Remainder |
| --- | ---: | ---: |
| $137/2$ | 68 | 1 |
| $68/2$ | 34 | 0 |
| $34/2$ | 17 | 0 |
| $17/2$ | 8 | 1 |
| $8/2$ | 4 | 0 |
| $4/2$ | 2 | 0 |
| $2/2$ | 1 | 0 |
| $1/2$ | 0 | 1 |

Thus $(137)_{10}=(10001001)_2$. A separate sign bit is one possible signed representation; ordinary signed integers are commonly represented using **two's complement**, rather than a separate sign and magnitude.

## Fractional binary digits

The same positional rule applies to negative powers of two:

$$
(0.5625)_{10}=(0.1001)_2=2^{-1}+2^{-4}.
$$

Repeated multiplication by two produces the fractional digits in their usual order:

$$
\begin{aligned}
0.5625\times2&=1+0.125,\\
0.125\times2&=0+0.25,\\
0.25\times2&=0+0.5,\\
0.5\times2&=1+0.
\end{aligned}
$$

## Floating point representation

A floating point number has a sign, a **significand** (often called a mantissa), and an exponent. In the usual IEEE binary convention, a normal number is

$$
x=(-1)^s(1.f)_2\,2^e.
$$

The stored exponent is biased; the leading $1$ of a normal significand is implicit. Alternative mathematical conventions normalize the significand to $[1/2,1)$, but this is not the stored IEEE $1.f$ convention.

| Format | Total bits | Sign | Exponent | Stored fraction | Normal significand precision |
| --- | ---: | ---: | ---: | ---: | ---: |
| Binary32, single precision | 32 | 1 | 8 | 23 | 24 bits |
| Binary64, double precision | 64 | 1 | 11 | 52 | 53 bits |

For binary64 normal numbers, $-1022\leq e\leq1023$. The largest finite value is $(2-2^{-52})2^{1023}\approx1.798\times10^{308}$. The smallest positive **normal** value is $2^{-1022}\approx2.225\times10^{-308}$; **subnormal** values extend down to $2^{-1074}\approx4.941\times10^{-324}$.

The hidden bit is the leading **one** of normal numbers, not a leading zero. Subnormal numbers use a leading zero instead and have reduced relative precision. Binary64 offers roughly 15–16 significant decimal digits; its normal significand contains 53 bits, with $\log_{10}(2^{53})\approx15.95$.

The numerical consequences are discussed in [[Floating point errors and FLOPs]].
