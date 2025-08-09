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
from binomial_greeks import binomial_price, greeks_binomial

# Price an American call option
price = binomial_price(100, 100, 0.75, 0.04, 0.2, N=200, option='call', style='amer')
print(f"Option Price: {price:.2f}")

# Calculate Greeks
greeks = greeks_binomial(100, 100, 0.75, 0.04, 0.2, N=200)
print(greeks)
```

## Example Output
```rust
Option Price: 6.78
{'price': 6.7823, 'delta': 0.545, 'gamma': 0.012, 'theta': -6.23, 'vega': 25.14, 'rho': 41.52}
```
