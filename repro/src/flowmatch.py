"""Clean-room diffusion flow matching from "Diffusion Flow Matching: Dimension-Improved KL Bounds"
(arXiv 2606.16610). numpy, CPU. Flow matching maps source N(0,I) to target N(mu,Sigma) via an ODE.
For Gaussian targets, the velocity field is linear; discretize with step h; measure KL to target.
c1: constant-step KL convergence; c3: non-uniform schedule faster; c6: dim improvement O(d^4)->O(d^3).
"""
from __future__ import annotations
import numpy as np


def flow_match_gaussian(mu_target, Sigma_target, N_particles, steps, dt, schedule="uniform", seed=0):
    """Flow matching: transport N(0,I) to N(mu,Sigma) via ODE dX/dt = v(X,t).
    For Gaussian target, v(X,t) = (mu - X)/(1-t) (the conditional flow). Discretize."""
    rng = np.random.default_rng(seed); d = len(mu_target)
    X = rng.standard_normal((N_particles, d))  # source N(0,I)
    for k in range(steps):
        if schedule == "uniform":
            t = (k + 0.5) / steps
            hk = dt
        elif schedule == "non_uniform":
            t = (k + 0.5) / steps
            hk = dt * min(max(t, 1 - t), 1.0)  # smaller steps at endpoints (paper's schedule)
        hk = min(hk, (1 - t) * 0.9 + 1e-6)
        # Simple OT-map flow for diagonal Sigma: X(t) = (1-t)*X0 + t*(mu + sqrt(Sigma_diag)*X0)
        # Velocity = mu + (sqrt(Sigma_diag) - 1)*X0 = constant per particle (exact Euler)
        sig_diag = np.sqrt(np.maximum(np.diag(Sigma_target), 1e-9))
        # Reconstruct X0 from X and t: X0 = (X - t*mu) / ((1-t) + t*sig_diag)
        scale = (1 - t) + t * sig_diag
        X0_recon = (X - t * mu_target[None, :]) / scale[None, :]
        target_pos = mu_target[None, :] + X0_recon * sig_diag[None, :]
        v = (target_pos - X) / max(1 - t, 1e-4)
        X = X + hk * v
    return X


def kl_gaussian(samples, mu_target, Sigma_target):
    """KL( sample distribution || N(mu, Sigma) ) — parametric."""
    d = len(mu_target)
    mu_s = samples.mean(0)
    Sigma_s = np.cov(samples.T) + 1e-8 * np.eye(d)
    Si = np.linalg.inv(Sigma_target + 1e-8 * np.eye(d))
    kl = 0.5 * (np.trace(Si @ Sigma_s) + (mu_s - mu_target) @ Si @ (mu_s - mu_target) - d
                + np.log(np.linalg.det(Sigma_target + 1e-8*np.eye(d)) / max(np.linalg.det(Sigma_s), 1e-300)))
    return float(max(kl, 0.0))


def w2_gaussian(samples, mu_target, Sigma_target):
    """2-Wasserstein to N(mu, Sigma) — parametric."""
    d = len(mu_target)
    mu_s = samples.mean(0); Sigma_s = np.cov(samples.T) + 1e-8 * np.eye(d)
    Ss_sqrt = np.linalg.cholesky(Sigma_s)
    cross = np.linalg.cholesky(Sigma_target + 1e-8 * np.eye(d))
    term = np.trace(Sigma_s) + np.trace(Sigma_target) - 2 * np.trace(np.linalg.cholesky(Sigma_s @ Sigma_target + 1e-8*np.eye(d)))
    return float(np.sum((mu_s - mu_target)**2) + max(term, 0))
