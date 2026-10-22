# Penning trap

Parent: [[Computational physical models]]

A **Penning trap** uses electric and magnetic fields to confine charged particles in a region of space. In the idealized positive-ion configuration, two endcap electrodes are held at a higher electric potential than the surrounding ring electrode. What determines the field is the potential difference, rather than an absolute sign assigned to each electrode's net charge.

![[Computational Physics/Assets/penning-trap.png]]

*Schematic cross-section: the endcaps provide axial electrostatic confinement, while the electric field is radially defocusing. A uniform magnetic field is applied along $z$. Electrode shapes are illustrative.*

The electric field restores a positive ion toward the centre along $z$, but pushes it away from the axis in the transverse plane. A static magnetic field along $z$ supplies the transverse Lorentz force,

$$
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B).
$$

The magnetic part bends transverse motion and can provide radial confinement when the field strengths satisfy the stability requirements. It does no work on the particle. The combined electric and magnetic motion is generally more complicated than a single circle.

The equations form coupled [[Initial value problems]]. [[Runge-Kutta methods|RK4]] can integrate the position and velocity together; the magnetic force depends on velocity, so the elementary velocity-independent Verlet formulas do not apply directly.
