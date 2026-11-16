In order to discretize a PDEs, we need different stepsizes for every variable that we use. For this reason, we will use ${}\Delta x, \Delta y{}$ and ${}\Delta t{}$. 
We then define
$$
\begin{aligned}
u(x_{i}, y_{j}) = u_{ij} \\
u(x_{i}, y_{j}, t_{n})= u_{ij}^{n} \\
\frac{ \partial^{2} u }{ \partial x^{2} } \vert_{(x_{i},y_{j})}= \left(\frac{ \partial^{2} u }{ \partial x^{2} }\right)_{ij}.
\end{aligned}
$$
Similarly to how we do for single-variable functions, we can define the discretized derivative using forward difference, backward difference and central difference: 
$$
\begin{aligned}
 & \left( \frac{ \partial u }{ \partial x }  \right)_{ij} = \frac{u_{i+1,j}-u_{i,j}}{\Delta x} + O(\Delta x), \qquad \text{forward difference} \\
 & \left( \frac{ \partial u }{ \partial x }  \right)_{ij} = \frac{u_{ij}-u_{i-1,j}}{\Delta x} + O(\Delta x), \qquad \text{backward difference} \\
 & \left( \frac{ \partial u }{ \partial x }  \right)_{ij}= \frac{u_{i+1,j}-u_{i-1,j}}{2 \Delta x} + O( \Delta x^{2}). \qquad \text{central difference}
\end{aligned}
$$
When we calculate second partial derivatives, we have to account for mixed derivatives as well. Non mixed partial derivatives can be calculated like in [[Discretization and numerical differentiation]]
$$
\left( \frac{ \partial^{2} u }{ \partial x^{2} }  \right)_{ij}= \frac{u_{i+1,j}-2u_{ij}+u_{i-1,j}}{\Delta x ^{2}}+O(\Delta x^{2}),
$$
whereas 
$$
\left( \frac{ \partial^{2} u }{ \partial x \partial y }  \right)_{ij} = \dots
$$