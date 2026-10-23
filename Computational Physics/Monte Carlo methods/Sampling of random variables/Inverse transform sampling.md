Parent: [[Sampling of random variables]]

Inverse transform sampling is a method to sample random variables from a given distribution ${}f{}$ useful when the cumulative distribution ${}F{}$ is known.

Let $F$ be the target CDF. Draw $u\sim\mathcal U(0,1)$ and set
$$
x=F^{-1}(u).
$$
For a continuous strictly increasing CDF, $F^{-1}$ exists and is the ordinary inverse. In general, use the generalized inverse $F^{-1}(u)=\inf\{x:F(x)\geq u\}$, since a CDF is only guaranteed to be nondecreasing.

To see why this works, set $Y=F(X)$. Conservation of probability (The probability to draw ${}X{}$ between ${}x{}$ and ${}x + dx{}$ is the same as the probability to draw ${}Y{}$ between ${}y = F(x){}$ and ${}y+dy{}$) gives
$$
p_X(x)\,dx=p_Y(y)\,dy,
\qquad \frac{dy}{dx}=F'(x)=p_X(x).
$$

Thus $p_Y(y)=1$ on $(0,1)$. Reversing the transformation maps a uniform variable to the target. This method rejects no samples, but requires an available or numerically computable inverse CDF, which can itself be costly.