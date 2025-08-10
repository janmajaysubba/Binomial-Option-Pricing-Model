# Binomial-Option-Pricing-Model
This project implements a **Binomial Options Pricing Model** (also known as the **Cox–Ross–Rubinstein model**) in Python to price both **American and European options** with **continuous dividend yields **, including a **Greeks calculator** for Delta, Gamma, Theta, Vega, and Rho.  

This project is based on the Binomial Options Pricing concepts from *Sheldon Natenberg's* **"Options, Volatility, and Pricing"**.


## Features
- Supports both **American** and **European** style options 
- Handles **Call** and **Put** options
- Includes **Continuous Dividend Yield** parameter (`q`)
- Calculates **Option Price** and **Greeks**
- Adjustable **time steps (`N`)** for accuracy vs. speed
  

## Limitations 

- Assumes constant volatility and interest rates over the option’s life.
- Models dividends as a continuous yield `q` — discrete dividends are not handled.
- Binomial parameters may produce unstable probabilities for very short maturities or extreme inputs (e.g., very high volatility).
- Accuracy depends on the number of steps `N`; very small `N` can cause large errors, while very large `N` increases runtime.
- Greeks are computed numerically via finite differences and may vary with bump size and `N`.

This project is a **basic, educational implementation** of the Cox–Ross–Rubinstein (CRR) binomial option pricing model with Greek calculations via finite differences.  
It is designed to demonstrate core option pricing concepts in Python, rather than to serve as a trading tool.


## Requirements
- NumPy
```bash
pip install numpy
```


## Usage

### 1. Clone the repository
```bash
git clone https://github.com/janmajaysubba/binomial-option-pricing-model.git
cd binomial-option-pricing-model
```

### 2. Run the example
```bash
python binomial_greeks.py
```

### 3. Import into your own Python scripts
```python
from binomial_greeks import binomial_price, greeks_binomial

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
```


## Example Output
```rust
Option Price: 7.93
Delta: 0.5813 | Gamma: 3.865473 | Theta/yr: -5.89 | Vega: 33.48 | Rho:  37.65
```


