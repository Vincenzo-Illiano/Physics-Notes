Parent: [[Nondegenerate time-independent perturbation theory]]
Model: [[The Quantum harmonic oscillator]]

In this note, we will apply [[Nondegenerate time-independent perturbation theory]] to a concrete example.

Consider the **anharmonic oscillator**
$$
H=\frac{p^2}{2m}+\frac12m\omega^2x^2+\alpha x^4.
$$
We apply [[Nondegenerate time-independent perturbation theory]], writing
$$
H=H_0+\alpha H',\qquad
H_0=\frac{p^2}{2m}+\frac12m\omega^2x^2,
\qquad H'=x^4.
$$
Here $\alpha$ is the perturbation parameter.

The unperturbed ground-state energy is
$$
E_0^{(0)}=\frac12\hbar\omega.
$$
To first order,
$$
E_0\simeq E_0^{(0)}+\alpha E_0^{(1)},
\qquad
E_0^{(1)}=\langle0|x^4|0\rangle,
$$
where $|0\rangle$ denotes the unperturbed harmonic-oscillator ground state.

Using the **creation and annihilation operators**,
$$
x=\sqrt{\frac{\hbar}{2m\omega}}(a+a^\dagger),
\qquad [a,a^\dagger]=1,
$$
we obtain
$$
\langle0|x^4|0\rangle
=\left(\frac{\hbar}{2m\omega}\right)^2
\langle0|(a+a^\dagger)^4|0\rangle.
$$
Since $(a+a^\dagger)|0\rangle=|1\rangle$ and
$\langle0|(a+a^\dagger)=\langle1|$,
$$
\begin{aligned}
\langle0|(a+a^\dagger)^4|0\rangle
&=\langle1|(a+a^\dagger)^2|1\rangle\\
&=\langle1|a^2+aa^\dagger+a^\dagger a+(a^\dagger)^2|1\rangle.
\end{aligned}
$$
The terms containing $a^2$ and $(a^\dagger)^2$ have zero expectation value in $|1\rangle$. Using $aa^\dagger=a^\dagger a+1$,
$$
\langle1|(aa^\dagger+a^\dagger a)|1\rangle
=\langle1|(2a^\dagger a+1)|1\rangle
=3.
$$
Therefore,
$$
{E_0^{(1)}=\langle0|x^4|0\rangle
=\frac{3\hbar^2}{4m^2\omega^2}.}
$$
The ground-state energy to first order is
$$
{
E_0\simeq\frac12\hbar\omega
+\frac{3\alpha\hbar^2}{4m^2\omega^2}
=\frac12\hbar\omega
\left(1+\frac{3\alpha\hbar}{2m^2\omega^3}\right).
}
$$
