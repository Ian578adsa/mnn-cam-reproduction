from pathlib import Path
import logging

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from mnn import simulations
from mnn.plotting import figures

Path("results").mkdir(exist_ok=True)
logging.getLogger().addHandler(
    logging.FileHandler("results/run.log", encoding="utf-8")
)

simulations.discretisation.run()
figures.discretisation_boxplots()

plt.gcf().savefig(
    "results/discretisation-boxplots.png",
    dpi=200,
    bbox_inches="tight",
)
plt.close("all")

assert Path("results/discretisation-boxplots.png").stat().st_size > 0
print("Reproduction finished. See results/ and plots/.")