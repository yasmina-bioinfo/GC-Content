import os
import matplotlib.pyplot as plt
from src.fasta_io import read_fasta
from src.gc_metrics import gc_percent

def main():
    # 1) Lire les séquences
    seqs = read_fasta("data/toy.fasta")

    # 2) Calculer le %GC pour chaque séquence
    ids = []
    gcs = []
    for sid, s in seqs.items():
        ids.append(sid)
        gcs.append(gc_percent(s))

    # 3) Créer le dossier de sortie
    os.makedirs("results", exist_ok=True)

    # 4) Tracer un diagramme en barres
    plt.figure(figsize=(8, 4))
    plt.bar(ids, gcs)
    plt.ylabel("GC%")
    plt.title("GC content par séquence")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 5) Sauvegarder l'image
    outpath = "results/gc_bar.png"
    plt.savefig(outpath, dpi=150)
    print(f"✅ Graphique enregistré : {outpath}")

if __name__ == "__main__":
    main()
