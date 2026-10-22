# Runge–Kutta methods

Parent: [[Numerical differential equations]]

**Runge–Kutta methods** solve [[Initial value problems]] by evaluating slopes at several stages within each step. The Euler predictor–corrector described there is the second-order Heun method. Here we consider the classical **fourth-order Runge–Kutta method (RK4)**.

## Classical RK4

For $y'=f(t,y)$, define increments that already include $h$:

$$
\begin{aligned}
k_1&=hf(t_i,y_i),\\
k_2&=hf\left(t_i+\frac h2,y_i+\frac{k_1}{2}\right),\\
k_3&=hf\left(t_i+\frac h2,y_i+\frac{k_2}{2}\right),\\
k_4&=hf(t_i+h,y_i+k_3),\\
y_{i+1}&=y_i+\frac16(k_1+2k_2+2k_3+k_4).
\end{aligned}
$$

The method uses four evaluations of $f$ per step. Under standard smoothness and stability assumptions, its local one-step error is $O(h^5)$ and its global error is $O(h^4)$.

## Relation to Simpson's rule

The exact update is

$$
y(t_{i+1})=y(t_i)+\int_{t_i}^{t_{i+1}}f(t,y(t))\,dt.
$$

Simpson's rule approximates an integral by

$$
\int_a^b g(t)\,dt\approx\frac{b-a}{6}
\left[g(a)+4g\left(\frac{a+b}{2}\right)+g(b)\right].
$$

This gives useful intuition for RK4's weights: the two midpoint stages together have weight four. If $f$ depends only on $t$, RK4 reduces exactly to Simpson quadrature for the update. For general $f(t,y)$, the stage states are approximations, so substituting Simpson's rule alone does **not** derive RK4. Its fourth-order accuracy follows by matching the appropriate Taylor terms.

## Coupled equations

For

$$
\dot x=v,\qquad\dot v=f(t,x,v),
$$

the RK4 stages must be evaluated at consistent intermediate states:

$$
\begin{aligned}
k_1^x&=hv_i,& k_1^v&=hf(t_i,x_i,v_i),\\
k_2^x&=h\left(v_i+\frac{k_1^v}{2}\right),&
k_2^v&=hf\left(t_i+\frac h2,x_i+\frac{k_1^x}{2},v_i+\frac{k_1^v}{2}\right),\\
k_3^x&=h\left(v_i+\frac{k_2^v}{2}\right),&
k_3^v&=hf\left(t_i+\frac h2,x_i+\frac{k_2^x}{2},v_i+\frac{k_2^v}{2}\right),\\
k_4^x&=h(v_i+k_3^v),&
k_4^v&=hf(t_i+h,x_i+k_3^x,v_i+k_3^v).
\end{aligned}
$$

Then

$$
\begin{aligned}
x_{i+1}&=x_i+\frac16(k_1^x+2k_2^x+2k_3^x+k_4^x),\\
v_{i+1}&=v_i+\frac16(k_1^v+2k_2^v+2k_3^v+k_4^v).
\end{aligned}
$$

*Compute the stages in sync across the entire coupled system.* In a many-particle problem, every particle's force at a stage must use the positions and velocities of all particles at that same stage.
