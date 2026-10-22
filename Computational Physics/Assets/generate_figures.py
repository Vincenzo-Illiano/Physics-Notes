"""Rebuild the illustrative figures in this folder with NumPy and Matplotlib.

Run: python3 'Computational Physics/Assets/generate_figures.py'
The figures illustrate the notes; none are measurements from course projects.
"""

from pathlib import Path
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Ellipse, FancyArrowPatch, Rectangle
from matplotlib.colors import ListedColormap
import numpy as np

OUT = Path(__file__).resolve().parent
BLUE = '#246b9e'
ORANGE = '#d17a22'
GREEN = '#319479'
plt.rcParams.update({
    'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False,
    'axes.labelsize': 11, 'figure.facecolor': 'white', 'savefig.facecolor': 'white',
})


def save(fig, filename):
    """Save a figure at a readable resolution and release its resources."""
    fig.savefig(OUT / filename, dpi=180, bbox_inches='tight')
    plt.close(fig)


def finite_differences():
    x0, h = 0.5, 0.4
    x = np.linspace(-0.1, 1.1, 400)
    fig, ax = plt.subplots(figsize=(7.2, 4.2), layout='constrained')
    ax.plot(x, np.exp(x), color='#333333', lw=2, label=r'$u(x)=e^x$')
    ax.plot(x, np.exp(x0) + np.exp(x0)*(x-x0), '--', color=GREEN,
            label='Exact tangent at x = 0.5')
    slopes = [(np.exp(x0+h)-np.exp(x0))/h,
              (np.exp(x0)-np.exp(x0-h))/h,
              (np.exp(x0+h)-np.exp(x0-h))/(2*h)]
    anchors = [np.exp(x0), np.exp(x0), (np.exp(x0-h)+np.exp(x0+h))/2]
    for slope, anchor, label, color in zip(slopes, anchors,
            ['Forward secant', 'Backward secant', 'Central secant'],
            [ORANGE, BLUE, '#9360a6']):
        ax.plot(x, anchor+slope*(x-x0), color=color, alpha=0.85, label=label)
    xp = np.array([x0-h,x0,x0+h])
    ax.scatter(xp, np.exp(xp), color='#222222', zorder=5)
    for xx, label in zip(xp, [r'$x-h$', r'$x$', r'$x+h$']):
        ax.axvline(xx, color='#dddddd', lw=1, zorder=0)
        ax.text(xx, 0.93, label, ha='center')
    ax.set(xlabel='x', ylabel='u(x)', ylim=(0.85,3.1), title='Finite difference slopes')
    ax.legend(fontsize=9, loc='upper left')
    save(fig,'finite-differences.png')


def derivative_error():
    h = np.logspace(-8,-1,300)
    x = np.float64(1.0)
    exact = 4*np.exp(2*x)
    computed = (np.exp(2*(x+h))-2*np.exp(2*x)+np.exp(2*(x-h)))/h**2
    error = np.abs(computed-exact)/exact
    unit_roundoff = np.finfo(np.float64).eps/2
    # For exp(2x), u''''/(12 u'') = 1/3; the rounding curve is a scale estimate.
    truncation = h**2/3
    rounding = unit_roundoff/h**2
    fig, ax = plt.subplots(figsize=(7.2,4.4), layout='constrained')
    ax.loglog(h, np.maximum(error,1e-18), '.', ms=3, color=BLUE, label='Computed relative error')
    ax.loglog(h,truncation,'--',color=GREEN,label=r'Truncation scale $h^2/3$')
    ax.loglog(h,rounding,'--',color=ORANGE,label=r'Round-off scale $u/h^2$')
    ax.loglog(h,truncation+rounding,color='#444444',lw=1.5,label='Sum of model scales')
    ax.set(xlabel='Step size h',ylabel='Relative error',ylim=(1e-11,10),
           title=r'Second derivative of $e^{2x}$ at $x=1$ (binary64)')
    ax.grid(which='major',alpha=0.2)
    ax.legend(fontsize=9)
    save(fig,'derivative-error.png')


def ivp_convergence():
    sizes = np.array([8,16,32,64,128])
    hs = 1/sizes
    errors = {key: [] for key in ['Euler','Heun','RK4']}
    for n in sizes:
        h=1/n
        for method in errors:
            y=1.0
            for _ in range(n):
                k1=-h*y
                if method=='Euler':
                    y+=k1
                elif method=='Heun':
                    k2=-h*(y+k1)
                    y+=(k1+k2)/2
                else:
                    k2=-h*(y+k1/2)
                    k3=-h*(y+k2/2)
                    k4=-h*(y+k3)
                    y+=(k1+2*k2+2*k3+k4)/6
            errors[method].append(abs(y-np.exp(-1)))
    fig,ax=plt.subplots(figsize=(7.2,4.4),layout='constrained')
    for (method,err),order,color in zip(errors.items(),[1,2,4],[ORANGE,GREEN,BLUE]):
        observed=np.log2(err[-2]/err[-1])
        assert abs(observed-order)<0.12, (method, observed)
        ax.loglog(hs,err,'o-',color=color,label=f'{method}: order {observed:.2f}')
        ax.loglog(hs,np.asarray(err[-1])*(hs/hs[-1])**order,':',color=color,alpha=0.6)
    ax.set(xlabel='Step size h',ylabel='Absolute error at t = 1',
           title=r'Global convergence for $y\prime=-y$, $y(0)=1$')
    ax.grid(which='major',alpha=0.2)
    ax.legend()
    save(fig,'ivp-convergence.png')


def jacobi_rotation():
    a=np.array([[2.,1.],[1.,3.]])
    tau=(a[1,1]-a[0,0])/(2*a[0,1])
    t=1/(tau+np.sqrt(1+tau*tau))
    c=1/np.sqrt(1+t*t)
    s=t*c
    rotation=np.array([[c,s],[-s,c]])
    diagonal=rotation.T@a@rotation
    assert abs(diagonal[0,1])<1e-14
    assert np.allclose(np.diag(diagonal),np.linalg.eigvalsh(a))
    fig,axes=plt.subplots(1,2,figsize=(7.2,3.4),layout='constrained')
    for ax,matrix,title in zip(axes,[a,diagonal],[r'$A$',r'$S^T A S$']):
        ax.imshow(matrix,cmap='Blues',vmin=0,vmax=4)
        for i in range(2):
            for j in range(2):
                ax.text(j,i,f'{matrix[i,j]:.3f}',ha='center',va='center',
                        color='white' if matrix[i,j]>2.5 else '#222222',fontsize=16)
        ax.set(xticks=[0,1],yticks=[0,1],xticklabels=['1','2'],yticklabels=['1','2'],
               title=title,xlabel='Column',ylabel='Row')
    fig.suptitle('Jacobi rotation: an orthogonal change of basis')
    save(fig,'jacobi-rotation.png')


def rejection_sampling():
    rng=np.random.default_rng(271828)
    proposals=rng.uniform(size=280)
    heights=rng.uniform(0,1.5,size=280)
    accepted=heights<=6*proposals*(1-proposals)
    x=np.linspace(0,1,400)
    fig,ax=plt.subplots(figsize=(7.2,4.3),layout='constrained')
    ax.fill_between(x,6*x*(1-x),color=BLUE,alpha=0.06)
    ax.scatter(proposals[accepted],heights[accepted],s=14,color=BLUE,alpha=0.65,label='Accepted')
    ax.scatter(proposals[~accepted],heights[~accepted],s=14,color=ORANGE,alpha=0.7,label='Rejected')
    ax.plot(x,6*x*(1-x),color='#222222',lw=2,label=r'Target $p(x)=6x(1-x)$')
    ax.axhline(1.5,ls='--',color=GREEN,label=r'Envelope $Mq(x)=1.5$')
    ax.set(xlabel='Proposed x',ylabel='Sampled height',ylim=(0,1.75),xlim=(0,1),
           title='Rejection sampling with a uniform proposal')
    ax.legend(fontsize=9,loc='upper left',ncol=2)
    save(fig,'rejection-sampling.png')


def buckling_modes():
    x=np.linspace(0,1,300)
    fig,axes=plt.subplots(3,1,figsize=(7.2,5.3),sharex=True,layout='constrained')
    for n,ax,color in zip(range(1,4),axes,[BLUE,GREEN,ORANGE]):
        ax.axhline(0,color='#aaaaaa',lw=1)
        ax.plot(x,np.sin(n*np.pi*x),lw=2,color=color)
        ax.scatter([0,1],[0,0],s=30,color='#222222',zorder=5)
        ax.set(ylim=(-1.25,1.25),ylabel=f'Mode {n}',yticks=[-1,0,1])
        ax.grid(axis='x',alpha=0.2)
    axes[-1].set_xlabel(r'Scaled position $\xi=x/L$')
    fig.suptitle('Pinned-beam eigenmodes (arbitrary normalized amplitude)')
    save(fig,'buckling-modes.png')


def penning_trap():
    fig,ax=plt.subplots(figsize=(7.2,5.7),layout='constrained')
    ax.set(xlim=(-2.8,2.8),ylim=(-2.4,2.5),aspect='equal')
    ax.axis('off')
    for sign in [-1,1]:
        cap=Ellipse((0,sign*1.7),2.8,0.42,facecolor='#c5dfed',edgecolor=BLUE,lw=2)
        ax.add_patch(cap)
        ax.text(0,sign*1.7,'Endcap: higher potential',ha='center',va='center',fontsize=10)
        ring=Rectangle((sign*1.75-0.16,-1.12),0.32,2.24,facecolor='#fde3c2',edgecolor=ORANGE,lw=2)
        ax.add_patch(ring)
        ax.text(sign*2.1,0,'Ring\nlower\npotential',ha='center',va='center',fontsize=10)
    # Electric force directions for a positive test ion.
    for start,end in [((0,1.25),(0,0.45)),((0,-1.25),(0,-0.45)),
                      ((0.35,0),(1.15,0)),((-0.35,0),(-1.15,0))]:
        ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=15,color=BLUE,lw=2))
    ax.scatter([0],[0],s=120,facecolor='white',edgecolor='#333333',zorder=5)
    ax.text(0,0,'+',ha='center',va='center',zorder=6)
    ax.text(0.18,0.8,r'$\mathbf{F}_E$',color=BLUE)
    ax.annotate('',xy=(1.22,1.25),xytext=(1.22,-1.25),
                arrowprops={'arrowstyle':'->','color':GREEN,'lw':2.5})
    ax.text(1.38,0.8,r'$\mathbf{B}$',color=GREEN)
    ax.annotate('',xy=(-2.5,2.2),xytext=(-2.5,1.35),arrowprops={'arrowstyle':'->','color':'#333333'})
    ax.text(-2.5,2.28,'z',ha='center')
    ax.text(0,-2.18,'Positive ion: axial electric restoring force, radial electric defocusing',
            ha='center',fontsize=9)
    ax.set_title('Penning trap: schematic cross-section')
    save(fig,'penning-trap.png')


def ising_lattice():
    rng=np.random.default_rng(314159)
    spins=rng.choice([-1,1],size=(8,8))
    fig,axes=plt.subplots(1,2,figsize=(7.2,3.9),layout='constrained',
                         gridspec_kw={'width_ratios':[1.3,1]})
    ax=axes[0]
    ax.imshow(spins,cmap=ListedColormap([ORANGE,BLUE]),vmin=-1,vmax=1)
    for i in range(8):
        for j in range(8):
            ax.text(j,i,'+' if spins[i,j]>0 else '−',ha='center',va='center',color='white',fontsize=13)
    ax.set(xticks=[],yticks=[],title='Illustrative configuration')
    ax.set_xticks(np.arange(-0.5,8,1),minor=True)
    ax.set_yticks(np.arange(-0.5,8,1),minor=True)
    ax.grid(which='minor',color='white',lw=1)
    ax.tick_params(which='minor',bottom=False,left=False)
    ax=axes[1]
    ax.set(xlim=(-1.5,1.5),ylim=(-1.5,1.5),aspect='equal',title='Nearest neighbours')
    for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
        ax.plot([0,x],[0,y],color='#999999',lw=2)
        ax.scatter([x],[y],s=170,color=BLUE,zorder=3)
    ax.scatter([0],[0],s=210,color=ORANGE,zorder=4)
    ax.axis('off')
    ax.text(0,-1.45,'No diagonal interaction',ha='center',fontsize=10)
    fig.suptitle('Two-dimensional Ising model')
    save(fig,'ising-lattice.png')


if __name__=='__main__':
    for function in [finite_differences,derivative_error,ivp_convergence,jacobi_rotation,
                     rejection_sampling,buckling_modes,penning_trap,ising_lattice]:
        function()
    print('Generated eight figures; RK convergence and Jacobi checks passed.')
