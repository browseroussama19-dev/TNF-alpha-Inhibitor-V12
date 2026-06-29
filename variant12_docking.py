smiles_v12 = "CC1CN(C1CC(F)(F)F)C2=NC=NC3=C(N2)C=CC(=C3)C4=CC=C(F)C=C4"

print("🧪 Processing Variant 12 (Strong Attack)...")
mol = Chem.AddHs(Chem.MolFromSmiles(smiles_v12))
AllChem.EmbedMolecule(mol, randomSeed=42)
AllChem.MMFFOptimizeMolecule(mol)
Chem.MolToMolFile(mol, "variant12.mol")

!mk_prepare_ligand.py -i variant12.mol -o variant12_final.pdbqt

v = Vina(sf_name='vina')
v.set_receptor('1TNF.pdbqt')
v.set_ligand_from_file("variant12_final.pdbqt")

v.compute_vina_maps(center=[20, 10, 5], box_size=[20, 20, 20])
v.dock(exhaustiveness=64, n_poses=1)

score = v.energies(n_poses=1)[0][0]
print("-" * 40)
print(f"🎯 Final Binding Energy for Variant 12: {score:.2f} kcal/mol")
print("-" * 40)
