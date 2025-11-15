import csv
from src.fasta_io import read_fasta
from src.gc_metrics import gc_percent

# Lecture du fichier FASTA
seqs = read_fasta("data/toy.fasta")

# Création et ouverture d'un fichier CSV en écriture
with open("results_gc_content.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["Sequence ID", "Length", "GC%"])  # En-têtes de colonnes

    # Pour chaque séquence du dictionnaire
    for sid, s in seqs.items():
        gcp = gc_percent(s)
        writer.writerow([sid, len(s), f"{gcp:.4f}"])

print("✅ Résultats enregistrés dans 'results_gc_content.csv'")
