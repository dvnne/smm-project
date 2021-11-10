from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.core import Spin
import matplotlib.pyplot as plt

def plot_eigen_from_vasprun(filename = 'vasprun.xml', kpoint = 0, e_window = 2.5):
    vr = Vasprun(filename, parse_potcar_file = False)
    efermi = vr.efermi
    values_up = vr.eigenvalues[Spin.up][kpoint]
    values_down = vr.eigenvalues[Spin.down][kpoint]
    values_up, values_down = values_up.transpose()[0], values_down.transpose()[0]
    ## Plotting ##
    plt.plot([1]*len(values_up), values_up, ls = '', ms = 60, marker = '_', label = "Spin Up")
    plt.plot([2]*len(values_down), values_down, ls = '', ms = 60, marker = '_', label = "Spin Down")
    plt.ylim(efermi - e_window, efermi + e_window)
    plt.xlim(0, 3)
    plt.ylabel("Energy (eV)")
    plt.hlines(efermi, 0, 4, ls = '--')
    plt.xticks([1, 2], ["Spin Up", "Spin Down"])
    plt.show()

plot_eigen_from_vasprun('vasprun.xml')

