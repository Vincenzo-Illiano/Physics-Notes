Parent: [[Mathematics of QM]]

In this note, we will state and proof **Feynman-Hellmann** theorem.

Let ${}H_{\lambda}{}$ be a Hamiltonian which depends on parameter ${}\lambda{}$ and let ${}\ket{\psi_{\lambda}}{}$ be its normalized eigenstates. Then: 
$$
{\frac{dE_{\lambda}}{d \lambda}= \left< \psi_{\lambda} | \frac{dH_{\lambda}}{d \lambda} | \psi_{\lambda} \right> }.
$$

**Proof:** Using the Leibniz rule:
$$
\begin{aligned}
\frac{dE_{\lambda}}{d\lambda}  &  = \frac{d}{d \lambda} \left<  \psi_{\lambda} | H_{\lambda} | \psi_{\lambda} \right> = \frac{d\bra{\psi_{\lambda}}}{d \lambda} E_{\lambda} \ket{\psi_{\lambda}} + \bra{\psi_{\lambda}} \frac{dH_{\lambda}}{d \lambda} \ket{\psi_{\lambda}} + \bra{\psi_{\lambda}} E_{\lambda} \frac{d\ket{\psi_{\lambda}}}{d\lambda} \\
 & = \bra{ \psi_{\lambda}} \frac{dH_{\lambda}}{d \lambda} \ket{\psi_{\lambda}} + E_{\lambda} \frac{d}{d \lambda}(\left< \psi_{\lambda}| \psi_{\lambda} \right> ) = \bra{ \psi_{\lambda}} \frac{dH_{\lambda}}{d \lambda} \ket{\psi_{\lambda}}.  
\end{aligned} 
$$
Where we used that ${}\ket{\psi_{\lambda}}{}$ are normalized to 1.