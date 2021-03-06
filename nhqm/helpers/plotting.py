from __future__ import division
import scipy as sp
import matplotlib.pyplot as plt
from nhqm.helpers.quantum import absq

def plot_contour(contour):
    """
    Plots the points of a contour.
    """
    points, _ = contour
    return plt.plot(sp.real(points), sp.imag(points), 
                    'o', color='gray', label="Contour")

def plot_pole(state):
    """
    Plots the momentum pole of a state in the complex plane.
    """
    mass = state.problem.mass
    energy = state.energy
    k = sp.sqrt(2*mass*energy)
    return plt.plot(sp.real(k), sp.imag(k), 'o', color='red')
    
def plot_momentum_wavefunction(state):
    """
    Plots the momentum wavefunction (a vector) of a state.
    """
    points, _ = state.basis.contour
    return plt.plot(sp.real(points), absq(state.eigenvector))
    
def find_resonance_state(states):
    """
    Heuristic that picks out the state with the least peaked 
    (most spread out) momentum wavefunction. By the uncertainty 
    principle, this should be (but isn't always) the most 
    localized state in position space.
    """
    def wavefunction_peak(state):
        return max(abs(state.eigenvector))
    return min(states, key=wavefunction_peak)