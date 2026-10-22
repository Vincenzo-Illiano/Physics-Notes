# Initial value problems

Parent: [[Numerical differential equations]]

An **initial value problem** specifies a differential equation and the required data at one initial value of the independent variable. For $y'=f(t,y)$ this is $y(t_0)=y_0$. Unlike [[Boundary value problems]], the data are not imposed at separate boundaries. The independent variable is often time, but this is not part of the mathematical definition.

## Reducing higher-order equations

For

$$
\frac{d^2y}{dt^2}=f(t,y,\dot y),
$$

define $v=\dot y$ and rewrite the problem as

$$
\begin{cases}
\dot y=v,\\
\dot v=f(t,y,v).
\end{cases}
$$

The initial data are $y(t_0)$ and $v(t_0)$. More generally, a regular higher-order ODE solved for its highest derivative can be written as a system of first-order equations by introducing additional variables. We therefore focus on first-order systems.

## Local and global errors

Here **local error** means the one-step solution error when starting that step from the exact solution. A method of order $p$ has local error $O(h^{p+1})$ and, under the usual smoothness and stability assumptions, global error $O(h^p)$ over a fixed time interval.

There are $n\propto1/h$ steps, which helps explain why the global order is one lower than the one-step error order. This is not a universal rule for every multistep recurrence or every definition of local truncation error.

## Forward Euler

For $y'=f(t,y)$, Taylor expansion gives

$$
\frac{y(t_i+h)-y(t_i)}{h}=f(t_i,y(t_i))+O(h).
$$

Neglecting this derivative approximation error gives

$$
y_{i+1}=y_i+hf(t_i,y_i).\tag{1}
$$

This is **forward Euler**, a first-order method with local error $O(h^2)$ and global error $O(h)$. It is a **one-step method** because only the current state is needed. In increment notation,

$$
k_1=hf(t_i,y_i),\qquad y_{i+1}=y_i+k_1.
$$

## Euler predictor–corrector (Heun's method)

Euler estimates the slope across the whole interval using its left endpoint. Averaging the endpoint slopes instead suggests the implicit trapezoidal equation

$$
y_{i+1}=y_i+\frac h2\bigl[f(t_i,y_i)+f(t_{i+1},y_{i+1})\bigr].
$$

The second slope depends on the unknown $y_{i+1}$. One explicit correction uses an Euler prediction:

$$
\begin{aligned}
y_{i+1}^*&=y_i+hf(t_i,y_i),\\
y_{i+1}&=y_i+\frac h2\bigl[f(t_i,y_i)+f(t_{i+1},y_{i+1}^*)\bigr].
\end{aligned}
$$

Equivalently,

$$
\begin{aligned}
k_1&=hf(t_i,y_i),\\
k_2&=hf(t_i+h,y_i+k_1),\\
y_{i+1}&=y_i+\frac12(k_1+k_2).
\end{aligned}
$$

This particular predictor–corrector is **Heun's method**, an explicit second-order Runge–Kutta method. It is one-step, with local error $O(h^3)$ and global error $O(h^2)$. Predictor–corrector methods as a whole are a broader family.

See [[Runge-Kutta methods]] for RK4 and [[Physical initial value problem algorithms]] for leapfrog and Verlet.

![[Computational Physics/Assets/ivp-convergence.png]]

*Global error at $t=1$ for $y'=-y$, $y(0)=1$. The measured orders approach 1, 2 and 4 for Euler, Heun and RK4.*
