
# 🧬 Variant 12: Novel TNF-alpha Inhibitor Discovery

## 📌 Project Overview
This repository contains the Python-based molecular docking script for **Variant 12**, a novel lead compound designed to inhibit the **1TNF** (Tumor Necrosis Factor-alpha) protein. 

Through an iterative computational drug design approach, this specific structural variant was identified to possess optimal steric and electronic properties for the target binding pocket.

## 🎯 Key Results
* **Target Protein:** 1TNF
* **Tool Used:** AutoDock Vina
* **Best Binding Affinity:** `-6.64 kcal/mol`
* **Grid Box Coordinates:** Center `[20, 10, 5]` | Size `[20, 20, 20]`

## 🔬 Methodology
The ligand design process involved:
1. **Hybrid Strategy:** Combining structural stability with targeted electronegativity.
2. **Fluorine Substitution:** Placing a fluorine atom to enhance molecular interactions within the active site.
3. **Docking Simulation:** Utilizing `AutoDock Vina` with an exhaustiveness of `64` to ensure highly accurate pose generation and binding energy calculation.

## 💻 How to Use
The provided Python script (`variant12_docking.py`) automates the preparation and docking process. 

### Prerequisites:
Ensure you have the following installed in your environment:
* RDKit
* AutoDock Vina
* AutoDockTools (`mk_prepare_ligand.py`)

### Execution:
Simply run the script in your terminal to generate the `SMILES` 3D structure, optimize it using the MMFF force field, and execute the Vina docking protocol.
