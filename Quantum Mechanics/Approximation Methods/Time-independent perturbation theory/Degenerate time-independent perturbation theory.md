Parent: [[Approximation methods]]

In this note, we will briefly discuss perturbation theory in the situation where there are degenerate eigenstates. In particular we will see that the energy of degenerate eigenstates splits when a perturbation is included, and we will see how choosing a convenient base in the subspace of degenerate eigenstates can simplify the calculations.

## Twofold degeneracy

Let $|a^{(0)}\rangle$ and $|b^{(0)}\rangle$ be orthonormal eigenstates of $H_0$ with the same energy $E^{(0)}$. For $H=H_0+\lambda H'$, take 
$$
|\psi^{(0)}\rangle=c_a|a^{(0)}\rangle+c_b|b^{(0)}\rangle.
$$
This is still an eigenstate of ${}H_{0}{}$ with energy ${}E^{(0)}{}$. The first-order equation (see [[Nondegenerate time-independent perturbation theory]]) is
$$
(H_0-E^{(0)})|\psi^{(1)}\rangle
=(E^{(1)}-H')|\psi^{(0)}\rangle.
$$
We can project this onto the two degenerate eigenstates. The left side vanishes because their energy is $E^{(0)}$, so we have
$$
W\begin{pmatrix}c_a\\c_b\end{pmatrix}
=E^{(1)}\begin{pmatrix}c_a\\c_b\end{pmatrix},\qquad
W=\begin{pmatrix}w_{aa}&w_{ab}\\w_{ab}^*&w_{bb}\end{pmatrix},
\qquad w_{ij}=\langle i^{(0)}|H'|j^{(0)}\rangle.
$$
Thus the first-order corrections are the eigenvalues of the perturbation **restricted to the degenerate eigenspace**:
$$
{E_\pm^{(1)}=\frac12\left(
w_{aa}+w_{bb}\pm\sqrt{(w_{aa}-w_{bb})^2+4|w_{ab}|^2}
\right).} \tag{1}
$$
The degeneracy splits at first order if the value in the square root is finite. For higher degeneracy, we have to diagonalize the matrix of $H'$ in the full degenerate eigenspace in the same way, getting higher degree equations as the order of degeneracy increases.

Eq. (1) could be simplified significantly if we chose a basis where ${}w_{ij}=0{}$. This is a basis that diagonalizes $W$, and the eigenstates in this basis are known as **good states**. In that basis the first-order energy corrections are the diagonal expectation values $w_{aa}$ and $w_{bb}$, which is the same as using nondegenerate theory.

To find good states, suppose a Hermitian operator $A$ commutes with both $H_0$ and $H'$. Since $[A,H_0]=0$, we can choose (nondegenerate) eigenstates of $A$ within the degenerate eigenspace of ${}H_{0}{}$. If $A|a^{(0)}\rangle=a|a^{(0)}\rangle$ and $A|b^{(0)}\rangle=b|b^{(0)}\rangle$, then
$$
\begin{aligned}
0&=\langle a^{(0)}|[A,H']|b^{(0)}\rangle\\
&=\langle a^{(0)}|AH'|b^{(0)}\rangle
-\langle a^{(0)}|H'A|b^{(0)}\rangle\\
&=(a-b)\langle a^{(0)}|H'|b^{(0)}\rangle.
\end{aligned}
$$
If $a\ne b$, the off-diagonal element vanishes, so these states form a good basis for the twofold degeneracy.

## Example: two-dimensional oscillator with a $gxy$ perturbation

Consider an oscillator with hamiltonian
$$
H=\underbrace{\frac{p_x^2+p_y^2}{2m}
+\frac12m\omega^2(x^2+y^2)}_{H_0}
+\underbrace{gxy}_{H'}.
$$
The unperturbed states $|n_x,n_y\rangle=|n_x\rangle\otimes|n_y\rangle$ have energies
$$
E_{n_x,n_y}^{(0)}=\hbar\omega(n_x+n_y+1).
$$
The ground state $|0,0\rangle$ is nondegenerate, with energy $\hbar\omega$. The first excited level has energy $2\hbar\omega$ and is spanned by $|0,1\rangle$ and $|1,0\rangle$. 

We can easily calculate the energy correction to the ground state using nondegenerate theory. Using
$$
x=\sqrt{\frac{\hbar}{2m\omega}}(a+a^\dagger),\qquad
y=\sqrt{\frac{\hbar}{2m\omega}}(b+b^\dagger),
$$
where $a$ and $b$ lower the $x$ and $y$ oscillator states, respectively, we have that
$$
E_{0,0}^{(1)}=\langle0,0|gxy|0,0\rangle
=\frac{g\hbar}{2m\omega}
\langle0|(a+a^\dagger)|0\rangle
\langle0|(b+b^\dagger)|0\rangle=0.
$$
Hence the ground-state energy is unchanged to first order.

In order to calculate the first order correction to the first excited state, we need to use twofold degenerate theory. ${}\ket{0,1}{}$ and ${}\ket{1,0}{}$, however, are not good states, but we can find good states if we find a hermitian operator that commutes with both ${}H_{0}{}$ and ${}H'{}$, and whose eigenstates in the degenerate subspace of ${}H_{0}{}$ are nondegenerate. 

Define the permutation operator $P|n_x,n_y\rangle=|n_y,n_x\rangle$. Both $H_0$ and $H'$ are invariant under $x\leftrightarrow y$, so $P$ commutes with both. We can also show that ${}P{}$ is hermitian. Its eigenstates in the first excited subspace are
$$
|\psi_\pm\rangle=\frac{|0,1\rangle\pm|1,0\rangle}{\sqrt2},
\qquad P|\psi_\pm\rangle=\pm|\psi_\pm\rangle.
$$
The two eigenvalues differ, so these are good states. We can thus calculate the first order energy correction for these states.
$$
\begin{aligned}
E_\pm^{(1)}
&=\langle\psi_\pm|gxy|\psi_\pm\rangle\\
&=\frac{g\hbar}{2m\omega}
\left\langle\psi_\pm\left|ab^\dagger+a^\dagger b\right|\psi_\pm\right\rangle
=\pm\frac{g\hbar}{2m\omega}.
\end{aligned}
$$
Where we used 
$$
(a+a^\dagger)(b+b^\dagger)=ab+ab^\dagger+a^\dagger b+a^\dagger b^\dagger
$$
the terms $ab$ and $a^\dagger b^\dagger$ have zero expectation in this subspace.

The first excited energies to the first order are therefore
$$
{E_\pm\simeq2\hbar\omega\pm\frac{g\hbar}{2m\omega}.}
$$
The two branches split by $|g|\hbar/(m\omega)$.

![[gxy oscillator level splitting.png]]

*First-order energies: the ground level stays at $\hbar\omega$, while the first excited level splits into the two exchange eigenstates.*
