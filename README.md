# Binomial-Option-Pricing-Model
This project implements a **Binomial Options Pricing Model** (also known as the **Cox–Ross–Rubinstein model**) in Python to price both **American and European options** with **continuous dividend yields **, including a **Greeks calculator** for Delta, Gamma, Theta, Vega, and Rho.  

Based on the Binomial Options Pricing concepts from *Sheldon Natenberg's* **"Options, Volatility, and Pricing"**.

## Features
- American and European option pricing
- Call and Put support
- Continuous dividend yield (`q`)
- Greeks calculation:
  - Delta
  - Gamma
  - Theta
  - Vega
  - Rho

## Requirements
- NumPy (`pip install numpy`)

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/janmajaysubba/binomial-option-pricing-model.git
cd binomial-option-pricing-model
```

###2. Run the example
```bash
python binomial_greeks.py
```

### 3. Import into your own Python scripts
```python
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
