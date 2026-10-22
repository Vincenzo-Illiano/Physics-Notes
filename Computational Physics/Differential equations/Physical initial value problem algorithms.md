# Physical initial value problem algorithms

Parent: [[Numerical differential equations]]

**Leapfrog** and **Verlet** are useful for mechanical [[Initial value problems]], especially equations of the form

$$
\ddot x=a(t,x),\tag{1}
$$

where acceleration does not depend on velocity. They apply componentwise to coupled particle systems.

## Time symmetry and symplecticity

A time-symmetric method reverses a step when the step size is reversed, including the correct reversal of stage times and stored variables.

For a separable Hamiltonian $H(q,p)=T(p)+V(q)$, the standard fixed-step leapfrog/Verlet splitting is **symplectic**: it preserves the canonical symplectic structure and consequently phase-space volume. It does not exactly conserve the original energy in general, nor does symplecticity alone guarantee all statistical properties.

Forward Euler, Heun and classical RK4 are generally not time-symmetric or symplectic. This statement concerns these explicit methods, not every [[Runge-Kutta methods|Runge–Kutta method]]. For forward Euler, a step followed by a negative step gives

$$
\hat y_i=y_i+h\bigl[f(t_i,y_i)-f(t_i+h,y_{i+1})\bigr],
$$

which is generally different from $y_i$.

## Central two-step leapfrog

For $dy/dt=f(t,y)$, the central first difference gives

$$
\frac{y(t_i+h)-y(t_i-h)}{2h}=f(t_i,y(t_i))+O(h^2).
$$

Neglecting the remainder leads to

$$
y_{i+1}=y_{i-1}+2hf(t_i,y_i).
$$

Its local unnormalized defect is $O(h^3)$ and its global order is two under suitable stability and starting-value assumptions. It is a **two-step method**: computing $y_{i+1}$ requires $y_i$ and $y_{i-1}$. It is not self-starting; an additional method must provide the first step with sufficient accuracy. One Euler step has $O(h^2)$ starting error and can retain second-order convergence, though a second-order starter is often preferable. The general two-step formula should not itself be assumed symplectic for arbitrary $f$.

## Staggered leapfrog for mechanics

Write (1) as $\dot x=v$, $\dot v=a(t,x)$. Positions and velocities can be stored half a step apart:

$$
\begin{aligned}
v_{i+1/2}&=v_{i-1/2}+h\,a(t_i,x_i),\\
x_{i+1}&=x_i+hv_{i+1/2}.
\end{aligned}
$$

An initial half-step velocity is obtained from $v_{1/2}=v_0+\frac h2a(t_0,x_0)$. The staggered storage makes quantities such as energy less direct to evaluate, but it does not make their evaluation impossible: a synchronized velocity can be reconstructed. Velocity Verlet stores synchronized states explicitly.

## Velocity Verlet

The **kick–drift–kick** formulation is

$$
\begin{aligned}
v_{i+1/2}&=v_i+\frac h2a(t_i,x_i)&&\text{(kick)},\\
x_{i+1}&=x_i+hv_{i+1/2}&&\text{(drift)},\\
v_{i+1}&=v_{i+1/2}+\frac h2a(t_{i+1},x_{i+1})&&\text{(kick)}.
\end{aligned}
$$

Both $x_i$ and $v_i$ are available at the same time. The full-state local one-step error is $O(h^3)$ and the global error is $O(h^2)$ for smooth problems.

## Position Verlet

Applying the central second difference directly to (1) gives

$$
x_{i+1}=2x_i-x_{i-1}+h^2a(t_i,x_i).
$$

Substituting the exact solution into this unnormalized recurrence leaves a defect $O(h^4)$. This does not imply third-order global accuracy: after division by $h^2$, the differential-equation residual is $O(h^2)$, and position Verlet is globally second-order with consistent starting data.

Position and velocity Verlet produce the same position recurrence in exact arithmetic with consistent initialization. Velocity Verlet also supplies velocities; position Verlet needs separate reconstruction. These methods are not directly applicable to a velocity-dependent Lorentz acceleration without modification, so the general RK4 formulation is useful for the [[Penning trap]].
