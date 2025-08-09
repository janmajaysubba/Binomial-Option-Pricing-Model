import numpy as np

def binomial_price(S, K, T, r, sigma, N=200, option='call', style='amer', q=0.0):
    """
    Binomial option pricing model with continuous dividend yield q and American/European toggle.

    Parameters
    ----------
    S : spot price of the underlying asset
    K : strike price
    T : time to expiry in years (calendar years, e.g., 30 days = 30/365)
    r : risk-free interest rate (continuous compounding)
    sigma : annualized volatility of the underlying asset
    N : number of time steps (higher = more accuracy)
    option : 'call' or 'put'
    style : 'amer' (American) or 'euro' (European)
    q : continuous dividend yield (e.g., 0.02 = 2% per year)

    Returns
    -------
    Option value at time 0
    """
    dt = T / N  # length of each time step
    if dt <= 0:
        raise ValueError("T must be > 0 and N must be >= 1")

    # Cox–Ross–Rubinstein up and down factors
    u = np.exp(sigma * np.sqrt(dt))  # up move factor
    d = 1.0 / u                      # down move factor

    # Risk-neutral probability (adjusted for continuous dividend yield q)
    p = (np.exp((r - q) * dt) - d) / (u - d)

    # Check for arbitrage violations
    if not (0 < p < 1):
        raise ValueError(f"Invalid probability p={p:.4f}. Try larger N or check r, q, sigma.")

    # Stock prices at maturity (final layer of the tree)
    ST = np.array([S * (u**j) * (d**(N - j)) for j in range(N + 1)])

    # Option payoff at maturity
    if option == 'call':
        V = np.maximum(ST - K, 0.0)
    else:
        V = np.maximum(K - ST, 0.0)

    # Discount factor for each step
    disc = np.exp(-r * dt)

    # Backward induction to present value
    for i in range(N - 1, -1, -1):
        # Expected option value from continuation
        V = disc * (p * V[1:i+2] + (1 - p) * V[0:i+1])

        if style == 'amer':
            # Stock prices at current step
            S_nodes = np.array([S * (u**j) * (d**(i - j)) for j in range(i + 1)])
            # Check early exercise value
            if option == 'call':
                exercise = np.maximum(S_nodes - K, 0.0)
            else:
                exercise = np.maximum(K - S_nodes, 0.0)
            # Choose max of continuation and early exercise
            V = np.maximum(V, exercise)

    return float(V[0])


def greeks_binomial(S, K, T, r, sigma, N, option='call', style='amer', q=0.0,
                    h_S=0.01, h_sigma=0.01, h_T=1/365, h_r=1e-4):
    """
    Compute option price and Greeks using finite-difference approximations.

    Parameters
    ----------
    h_S, h_sigma, h_T, h_r : small bumps for numerical differentiation.
        h_T=1/365 means a 1-calendar-day bump.

    Returns
    -------
    Dictionary containing price, delta, gamma, theta, vega, rho.
    """
    price0 = binomial_price(S, K, T, r, sigma, N, option, style, q)

    # Delta & Gamma
    up = binomial_price(S + h_S, K, T, r, sigma, N, option, style, q)
    dn = binomial_price(S - h_S, K, T, r, sigma, N, option, style, q)
    delta = (up - dn) / (2 * h_S)
    gamma = (up - 2 * price0 + dn) / (h_S ** 2)

    # Theta (per year; negative means time decay)
    Tp = T + h_T
    Tm = max(T - h_T, 1e-6)
    vp = binomial_price(S, K, Tp, r, sigma, N, option, style, q)
    vm = binomial_price(S, K, Tm, r, sigma, N, option, style, q)
    theta = (vp - vm) / (2 * h_T) * (-1)

    # Vega
    sp = binomial_price(S, K, T, r, sigma + h_sigma, N, option, style, q)
    sm = binomial_price(S, K, T, r, sigma - h_sigma, N, option, style, q)
    vega = (sp - sm) / (2 * h_sigma)

    # Rho
    rp = binomial_price(S, K, T, r + h_r, sigma, N, option, style, q)
    rm = binomial_price(S, K, T, r - h_r, sigma, N, option, style, q)
    rho = (rp - rm) / (2 * h_r)

    return {
        "price": price0,
        "delta": delta,
        "gamma": gamma,
        "theta": theta,
        "vega": vega,
        "rho": rho
    }


# ------------------------
# Example usage (demo)
# ------------------------
if __name__ == "__main__":
    # Parameters
    S, K, T, r, sigma, q, N = 100, 100, 0.75, 0.04, 0.2, 0.01, 400

    # Price an American call option
    price = binomial_price(S, K, T, r, sigma, N, option='call', style='amer', q=q)
    print("Option Price:", round(price, 2))

    # Compute Greeks
    greeks = greeks_binomial(S, K, T, r, sigma, N, option='call', style='amer', q=q)
    print(
    "Delta: {d:.4f} | Gamma: {g:.6f} | Theta/yr: {t:.2f} | Vega: {v:.2f} | Rho: {r_: .2f}"
    .format(d=greeks['delta'], g=greeks['gamma'], t=greeks['theta'],
            v=greeks['vega'], r_=greeks['rho'])
)
