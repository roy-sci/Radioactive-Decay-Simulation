# Radioactive Decay Simulation using Monte Carlo Method
# Example isotope: Carbon-14
# Author: (your name)
# This script simulates radioactive decay and compares it with theory

import numpy as np
import matplotlib.pyplot as plt


# Physical parameters


# Carbon-14 properties
half_life_years = 5730            # half-life of Carbon-14 in years
lambda_decay = np.log(2) / half_life_years  # decay constant 

# Simulation parameters
N0 = 10000        # initial number of nuclei
dt = 1.0          # time step in yrs
total_time = 20000  # total simulation time in yrs

# No of steps
num_steps = int(total_time / dt)


#  to store results


time_array = np.zeros(num_steps)
N_array = np.zeros(num_steps)

# Start with all nuclei undecayed
N_current = N0

# Probability of decay per nucleus per time step
p_decay = lambda_decay * dt


# Monte Carlo simulation


for i in range(num_steps):
    time_array[i] = i * dt
    N_array[i] = N_current

    # Count how many nuclei decay in this step
    decayed_this_step = 0

    # Loop over remaining nuclei (not vectorised)
    for _ in range(N_current):
        r = np.random.rand()
        if r < p_decay:
            decayed_this_step += 1

    # Update remaining nuclei
    N_current = N_current - decayed_this_step

    # Stop if everything has decayed
    if N_current <= 0:
        N_array[i:] = 0
        break


# Theoretical decay curve


N_theory = N0 * np.exp(-lambda_decay * time_array)


# Estimate half-life from simulation


half_N = N0 / 2
half_life_sim = None

for i in range(len(N_array)):
    if N_array[i] <= half_N:
        half_life_sim = time_array[i]
        break


# Plotting


plt.figure(figsize=(8, 5))
plt.plot(time_array, N_array, label="Monte Carlo Simulation", alpha=0.8)
plt.plot(time_array, N_theory, label="Theoretical Decay", linestyle="--")

if half_life_sim is not None:
    plt.axvline(half_life_sim, color="red", linestyle=":",
                label=f"Simulated Half-life ≈ {half_life_sim:.0f} years")

plt.xlabel("Time (years)")
plt.ylabel("Number of undecayed nuclei")
plt.title("Radioactive Decay of Carbon-14 (Monte Carlo Simulation)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()




print("Isotope: Carbon-14")
print(f"Theoretical half-life: {half_life_years} years")

if half_life_sim is not None:
    print(f"Simulated half-life: {half_life_sim:.1f} years")
else:
    print("Half-life could not be determined from simulation.")
