import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

# Define optical elements as matrices
def beam_splitter():
    return (1 / np.sqrt(2)) * np.array([[1, 1j], [1j, 1]])

def phase_shifter(phase):
    return np.array([[np.exp(1j * phase), 0], [0, 1]])

def mirror():
    return np.array([[0, 1], [1, 0]])

# Simulate Mach-Zehnder Interferometer with multiple photons
def mach_zehnder_interferometer(phase, num_photons=1):
    BS = beam_splitter()
    P = phase_shifter(phase)
    M = mirror()
    
    # Initial photon state: enters through first port
    psi_in = np.array([1, 0])
    
    # Photon transformation through interferometer
    psi_out = BS @ M @ P @ BS @ psi_in
    
    # Probability of detection at each output
    prob_0 = np.abs(psi_out[0])**2
    prob_1 = np.abs(psi_out[1])**2
    
    return prob_0 * num_photons, prob_1 * num_photons

# Phase range for simulation
phases = np.linspace(0, 2 * np.pi, 100)
probabilities = [mach_zehnder_interferometer(ϕ, num_photons=10) for ϕ in phases]
prob_0, prob_1 = zip(*probabilities)

# Interactive plot for multi-photon simulation
def interactive_plot(phase, num_photons):
    prob_0, prob_1 = mach_zehnder_interferometer(phase, num_photons)
    plt.figure(figsize=(6, 4))
    plt.bar(["Output Port 0", "Output Port 1"], [prob_0, prob_1], color=["blue", "red"])
    plt.ylim(0, num_photons)
    plt.ylabel("Photon Detection Count")
    plt.title(f"Mach-Zehnder Interferometer at Phase = {phase:.2f} radians with {num_photons} Photons")
    plt.show()

interact(interactive_plot, phase=(0, 2 * np.pi, 0.1), num_photons=(1, 100, 1))

# Static interference plot
plt.figure(figsize=(8, 5))
plt.plot(phases, prob_0, label="Output Port 0", color="blue")
plt.plot(phases, prob_1, label="Output Port 1", color="red")
plt.xlabel("Phase Shift (radians)")
plt.ylabel("Photon Detection Count")
plt.title("Mach-Zehnder Interferometer: Multi-Photon Quantum Interference")
plt.legend()
plt.grid()
plt.show()
