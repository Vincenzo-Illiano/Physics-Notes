Parent: [[Variational method]]

In this note, we will apply the [[Variational method]] to the harmonic oscillator.

Consider the Hamiltonian for a harmonic oscillator:
$$
H=\frac{p^2}{2m}+\frac12m\omega^2x^2.
$$
Choose the trial function
$$
\psi_a(x)=
\begin{cases}
A\left(1+\cos\dfrac{\pi x}{a}\right),& |x|<a,\\
0,& |x|\geq a,
\end{cases}
\qquad a>0.
$$
The exact ground-state wave function is a Gaussian, but it can still be useful to see how well a different trial function approximates the ground energy.

In order for $\psi_{a}(x)$ to be normalized, we have to impose $\int_{-\infty}^{\infty}|\psi_a(x)|^2\,dx=1$, which gives
$$
\begin{aligned}
1
&=|A|^2\int_{-a}^{a}\left(1+\cos\frac{\pi x}{a}\right)^2dx\\
&=|A|^2\int_{-a}^{a}\left(1+\cos^2\frac{\pi x}{a}
+2\cos\frac{\pi x}{a}\right)dx\\
&=3a|A|^2.
\end{aligned}
$$
Choosing $A$ real and positive,
$$
A=\frac{1}{\sqrt{3a}}.
$$
Once ${}A{}$ is known, we can calculate the expectation value of ${}H{}$. We have
$$
\langle H\rangle
=\frac{1}{2m}\langle p^2\rangle
+\frac12m\omega^2\langle x^2\rangle.
$$
The momentum contribution is
$$
\begin{aligned}
\langle p^2\rangle
&=-\hbar^2\left\langle\psi_a\left|\frac{d^2}{dx^2}\right|\psi_a\right\rangle\\
&=-\frac{\hbar^2}{3a}\int_{-a}^{a}
\left(1+\cos\frac{\pi x}{a}\right)
\frac{d^2}{dx^2}\left(1+\cos\frac{\pi x}{a}\right)dx\\
&=\frac{\pi^2\hbar^2}{3a^3}\int_{-a}^{a}
\left(1+\cos\frac{\pi x}{a}\right)\cos\frac{\pi x}{a}\,dx\\
&=\frac{\pi^2\hbar^2}{3a^2}.
\end{aligned}
$$
Similarly, 
$$
\langle x^2\rangle
=\frac{1}{3a}\int_{-a}^{a}x^2\left(1+\cos\frac{\pi x}{a}\right)^2dx
=\frac{a^2}{3}\left(1-\frac{15}{2\pi^2}\right).
$$
Therefore,
$$
{\langle H\rangle(a)
=\frac{\pi^2\hbar^2}{6ma^2}
+\frac{m\omega^2a^2}{6}\left(1-\frac{15}{2\pi^2}\right).}
$$
The stationary-point condition is
$$
\frac{d\langle H\rangle}{da}
=-\frac{\pi^2\hbar^2}{3ma^3}
+\frac{m\omega^2a}{3}\left(1-\frac{15}{2\pi^2}\right)=0.
$$
Which gives:
$$
a=b\sqrt{\frac{\pi\hbar}{m\omega}},
\qquad \text{where} \ \  
b=\left(1-\frac{15}{2\pi^2}\right)^{-1/4}.
$$
Substituting into the energy expectation value,
$$
\boxed{\langle H\rangle_{\min}
=\frac{\pi}{3b^2}\hbar\omega
\simeq0.513\,\hbar\omega.}
$$
Of course, the value calculated with this procedure is slightly larger than the exact value, which we expect to be ${}0.5 \hbar \omega {}$. This must be the case because of eq. 1 in [[Variational method]].