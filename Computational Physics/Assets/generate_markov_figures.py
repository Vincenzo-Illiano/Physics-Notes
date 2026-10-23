"""Regenerate the Markov-chain and MCMC illustrations with NumPy/Matplotlib.

The figures are explanatory demonstrations, not experimental or project data.
Run this script from any working directory; outputs are written beside it.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
BLUE, ORANGE, GREEN = '#246b9e', '#d17a22', '#319479'
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'figure.facecolor': 'white',
                     'savefig.facecolor': 'white'})


def markov_convergence():
    """Compute distributions by matrix multiplication rather than sample paths."""
    ring = np.zeros((5, 5))
    for i in range(5):
        ring[i, (i - 1) % 5] = 0.5
        ring[i, (i + 1) % 5] = 0.5
    r = np.array([1., 0., 0., 0., 0.])
    history = [r.copy()]
    for _ in range(30):
        r = r @ ring
        history.append(r.copy())
    history = np.asarray(history)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), layout='constrained')
    for i, color in enumerate([BLUE, ORANGE, GREEN, '#9360a6', '#80735d']):
        axes[0].plot(history[:, i], color=color, alpha=0.85, lw=1.5,
                     label=f'State {i}', ls='--' if i >= 3 else '-')
    axes[0].axhline(0.2, color='#333333', ls=':', label='Stationary: 1/5')
    axes[0].set(xlabel='Iteration n', ylabel='State probability',
                title='Five-state ring, starting at state 0', ylim=(-0.03, 1.03))
    axes[0].legend(fontsize=8, ncol=2)
    # The paired ring probabilities coincide by reflection symmetry.
    n = np.arange(501)
    for p0, label, color in [(0, 'Initially outside', BLUE),
                              (1, 'Initially inside', ORANGE)]:
        probability = 2/3 + (p0 - 2/3) * 0.985**n
        axes[1].plot(n, probability, color=color, label=label, lw=2)
    axes[1].axhline(2/3, color='#333333', ls=':', label='Stationary: 2/3')
    axes[1].set(xlabel='Washing-machine cycle n', ylabel='Probability of being inside',
                title='Sock chain: different starts, same limit', ylim=(-0.03, 1.03))
    axes[1].legend(fontsize=9)
    for ax in axes:
        ax.grid(alpha=0.15)
    fig.savefig(OUT / 'markov-convergence.png', dpi=180)
    plt.close(fig)


def gaussian_metropolis(start, rng, count=100):
    """Return every state, including repeats following rejected proposals."""
    states = np.empty(count + 1)
    states[0] = start
    for n in range(count):
        proposal = states[n] + rng.normal()
        log_ratio = -0.5 * (proposal**2 - states[n]**2)
        # Compare logarithms to avoid evaluating a potentially large exponential.
        accept = np.log(rng.uniform()) < min(0., log_ratio)
        states[n+1] = proposal if accept else states[n]
    return states


def mcmc_burn_in():
    """Illustrate a transient and the uncertainty of a short correlated sample."""
    rng = np.random.default_rng(20261023)
    chains = [gaussian_metropolis(8., rng), gaussian_metropolis(0., rng)]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), layout='constrained')
    axes[0].axvspan(0, 20, color='#dddddd', alpha=0.7, label='Illustrative discard')
    for chain, color, label in zip(chains, [ORANGE, BLUE], ['Start at 8', 'Start at 0']):
        axes[0].plot(np.arange(101), chain, color=color, lw=1.3, label=label)
    axes[0].axhline(0., color='#555555', ls=':', lw=1)
    axes[0].set(xlabel='Transition n', ylabel='Recorded state',
                title='Gaussian random-walk Metropolis (100 transitions)')
    axes[0].legend(fontsize=9)
    bins = np.linspace(-4, 4, 17)
    for chain, color, label in zip(chains, [ORANGE, BLUE], ['Start at 8', 'Start at 0']):
        axes[1].hist(chain[21:], bins=bins, density=True, histtype='step',
                     lw=1.8, color=color, label=f'{label}: 80 retained states')
    x = np.linspace(-4, 4, 500)
    axes[1].plot(x, np.exp(-x*x/2)/np.sqrt(2*np.pi), color='#333333',
                 lw=2, label='Target N(0, 1)')
    axes[1].set(xlabel='x', ylabel='Density', title='Short-run histograms after the illustrative discard')
    axes[1].legend(fontsize=8)
    fig.savefig(OUT / 'mcmc-gaussian-burn-in.png', dpi=180)
    plt.close(fig)


if __name__ == '__main__':
    markov_convergence()
    mcmc_burn_in()
    print('Generated two reproducible figures.')
