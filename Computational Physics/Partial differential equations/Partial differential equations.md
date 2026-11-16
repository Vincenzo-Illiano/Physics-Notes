Parent: [[Computational physics]]

In this note, we will introduce the concept of partial differential equation and explain the notions needed to treat them from a computational standpoint. A **partial differential equation** is a differential equations in more than one variable. In physics, these variables may be position variables and time, but in general they can be anything. PDEs are fundamental in the description of **dynamical systems**.

In this topic, we will limit our discussion to PDEs of two variables, which in general form look like this: 
$$
A \frac{ \partial^{2} u }{ \partial x^{2} } + B \frac{ \partial^{2} u }{ \partial x \partial y } + C \frac{ \partial^{2} u }{ \partial y^{2} }  + (\text{first order terms}) = g(x,y).
$$
Note that here ${}x{}$ and ${}y{}$ do not necessarily represent position variables. We define the **discriminant** ${}Q = B^{2} - 4AC{}$. With this we distinguish between different types of PDEs:

- **Hyperbolic** PDEs, with ${}Q > 0{}$,
- **Parabolic** PDEs, with ${}Q=0{}$,
- **Elliptic** PDEs, with ${}Q < 0{}$.

Given a PDE, its solution ${}u(x,y){}$ and a point in its domain ${}(x',y'){}$, we define **the domain of dependence** as all points where a change in ${}u(x,t){}$ can affect the solution value ${}u(x',t'){}$ at the point ${}(x',t'){}$. Similarly, we define the **domain of dependence** as all ${}(x,t){}$ points whose solution value ${}u(x,t){}$ can be affected by a change in ${}u(x',t'){}$.

We will now make examples of these three different types.

## Hyperbolic PDE example: the wave equation

An important example of a hyperbolic PDE known as the **wave equation**, which describes the propagation of physical waves, like electromagnetic waves or sound waves. This has the form
$$
v^{2} \frac{ \partial^{2} u }{ \partial x^{2} } - \frac{ \partial^{2} u }{ \partial t^{2} } =0,
$$
where ${}A = v^{2}{}$, ${}B=0{}$ and ${}C=-1{}$. Clearly, ${}4V^{2}>0{}$, so this is a hyperbolic equation.  Domain of influence and domain of dependence together define something very similar to a **light cone**:

![[Pasted image 20261112111138.png|center]]

## Parabolic PDE example

An example of a parabolic PDE is the **diffusion equation** in 1+1 dimensions: 
$$
D \frac{ \partial^{2} u }{ \partial x^{2} } - \frac{ \partial u }{ \partial t } =0.
$$
In this case, ${}A = D, B = 0{}$ and ${}C = 0{}$. The discriminant is given by ${}Q = B^{2} - 4AC = 0{}$, which makes this a parabolic PDE. In this equation, the domain of dependence and domain of influence look like this:

![[Pasted image 20261112111600.png]]

The solution ${}u(x',t'){}$ depends on some boundary conditions, given by: 
$$
\begin{aligned}
u(x,t=0)=f(x) \\
u(x=x_\text{min},t)=g(t) \\
u(x=x_\text{max},t)=h(t), 
\end{aligned}
$$
where ${}f, g {}$ and ${}h{}$ are given functions. 

## Elliptic PDE example

An example of a very famous elliptic example is the Poisson equation: 
$$
\frac{ \partial^{2} u }{ \partial x^{2} } + \frac{ \partial^{2} u }{ \partial y^{2} } = \rho(x,y).
$$
This has ${}A = 1, B = 0{}$ and ${}C = 1{}$, meaning it has discriminant ${}Q = B^{2} - 4AC = -4 < 0.{}$

In this case, the domain of dependence and the domain of influence are the whole domain space:

![[Pasted image 20261112112122.png]]

In this case, a solution at ${}(x',y'){}$ can depend on the solution at all other points ${}(x,y){}$, and similarly the solution at ${}(x',y'){}$ can impact the solution at any other point.

