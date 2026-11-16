The **forward difference scheme**, also known as **the explicit scheme**, is a scheme to solve PDEs. To illustrate it, we will show how to use it on the diffusion equation 
$$
\frac{ \partial u }{ \partial t } = D \frac{ \partial^{2} u }{ \partial x^{2} },
$$
and for simplicity we will set ${}D = 1{}$. We will use a subscript for the position index and a superscript for the time index, meaning that ${}u(x_{i},t_{n})=u_{i}^{n}{}$. In this scheme, we will use the forward difference formula, which we can use to rewrite the equation as 
$$
\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t} = \frac{u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n}}{(\Delta x)^{2}}.
$$
If we define ${}\alpha = \Delta t / \Delta x ^{2}{}$, we get 
$$
u_{i}^{n+1}=(1-2\alpha)u_{i}^{n}+ \alpha [u_{i+1}^{n}+u_{i-1}^{n}]. \tag 1
$$
Since we can directly and easily calculate ${}u^{n+1}{}$ from ${}u^{n}{}$, this method is also known as the explicit method. If we use vector notation 
$$
\vec{u}^{n} = (u_{0}^{n}, u_{1}^{n}, \dots),
$$
then eq. (1) can be rewritten as 
$$
\vec{a}^{n+1}=(I-\alpha B)\vec{u}^{n},
$$
where ${}B = \text{tridiag(-1, 2, -1)}{}$. 