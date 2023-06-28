import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
plt.style.use('./plcr_stylesheet.txt')

def pdf_f_unnormalized(r, sigma):
    y = np.exp(-(r[:,0]**2 + r[:,1]**2)/(2*sigma**2))
    y = y * np.sinh((r[:,0] - r[:,1])/2)
    y = y * ((r[:,0] - r[:,1]) > 0)
    return y

def rejection_sample(sigma, N_samples, N_candidates):

    R_samples = []

    N_candidates_total = 0
    while len(R_samples) < N_samples:
        # setting up the proposal pdf g
        mu = np.array([1/2*sigma**2, -1/2*sigma**2])
        cov = sigma**2*np.eye(2)    
        # get samples from g
        R_candidates = multivariate_normal.rvs(mu, cov, size=N_candidates)
        # get uniform samples
        U = np.random.rand(N_candidates)
        # set up the test criterium
        num = np.exp(-sigma**2/4) * pdf_f_unnormalized(R_candidates, sigma)
        den = np.pi*sigma**2 * multivariate_normal.pdf(R_candidates, mu, cov)
        # get the idx of the candidate samples that pass the test
        sel = U < num/den
        R_accept = R_candidates[sel]
        # append the samples
        R_samples = R_samples + list(R_accept)
        # monitor the total number of candidate samples
        N_candidates_total = N_candidates_total + N_candidates

    # estimate the probability of acceptance
    prob_acceptance = len(R_samples) / N_candidates_total
    # ensure that we only keep the desired number of samples
    R_samples = np.stack(R_samples[:N_samples])

    return R_samples, prob_acceptance

sigma = 1 # fix the dispersion of the target pdf f
N_samples = 10_000 # how many samples we wish to have
N_candidates = 10_000 # how many candidate samples for each iteration

R_samples, prob_acceptance = rejection_sample(sigma, N_samples, N_candidates)

r1_array = np.linspace(-3, 3, 501)
r2_array = np.linspace(-3, 3, 501)
fig, ax = plt.subplots(figsize=(14.63,4.31), ncols=3)
plt.subplots_adjust(bottom=0.15, wspace=0.30)
for axi, si in zip(ax, [0.5, 1.0, 1.5]):
    R1, R2 = np.meshgrid(r1_array, r2_array)
    r = np.stack([R1.flatten(), R2.flatten()]).T
    f = pdf_f_unnormalized(r, sigma=si)
    f = np.reshape(f, (501, 501))
    axi.contour(r1_array, r2_array, f, levels=8)
    axi.set_title(r'$f(r_1, r_2)$ with $\sigma = $' + f'{si}')
    axi.set_xlabel(r'$r_1$')
    axi.set_ylabel(r'$r_2$')
plt.savefig('rejection-sampling-fig01.svg', format='svg')

r1_array = np.linspace(-3, 3, 101)
r2_array = np.linspace(-3, 3, 101)
fig, ax = plt.subplots(figsize=(5.0,4.31))
plt.subplots_adjust(bottom=0.15)
R1, R2 = np.meshgrid(r1_array, r2_array)
r = np.stack([R1.flatten(), R2.flatten()]).T
f = pdf_f_unnormalized(r, sigma=1.0)
f = np.reshape(f, (101, 101))
ax.hexbin(x=R_samples[:,0], y=R_samples[:,1], bins=10, extent=(-3, +3, -3, +3), cmap='Greys')
ax.contour(r1_array, r2_array, f, levels=8, cmap='viridis')
ax.set_title(r'$f(r_1, r_2)$ with $\sigma = 1.0$')
ax.set_xlabel(r'$r_1$')
ax.set_ylabel(r'$r_2$')
plt.savefig('rejection-sampling-fig02.svg', format='svg')
# fig.show()

sigma_array = np.linspace(0.1, 5, 20)
prob_acceptance_array = []
M_array = []
for si in sigma_array:
    _, prob_acceptance = rejection_sample(si, N_samples, N_candidates)
    r1_array = np.linspace(-50, 50, 501)
    r2_array = np.linspace(-50, 50, 501)
    dr1 = r1_array[1] - r1_array[0]
    dr2 = r2_array[1] - r2_array[0]
    R1, R2 = np.meshgrid(r1_array, r2_array)
    r = np.stack([R1.flatten(), R2.flatten()]).T
    f = pdf_f_unnormalized(r, sigma=si)
    f = np.reshape(f, (501, 501))
    Z = np.sum(f * dr1 * dr2)
    M = np.pi * si**2 * np.exp(si**2 / 4) / Z
    M_array.append(M)
    prob_acceptance_array.append(prob_acceptance)
M_array = np.array(M_array)
prob_acceptance_array = np.array(prob_acceptance_array)

fig, ax = plt.subplots(figsize=(5.0,4.31))
plt.subplots_adjust(bottom=0.15)
ax.plot(sigma_array, 1/M_array, label='theory', c='C1')
ax.scatter(sigma_array, prob_acceptance_array, label='estimated',
           facecolors='none', edgecolors='C0', s=50, linewidth=2)
ax.set_title(r'Probability of acceptance')
ax.set_xlabel(r'$\sigma$')
ax.legend()
plt.savefig('rejection-sampling-fig03.svg', format='svg')