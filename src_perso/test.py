from src_perso.gc_content_PERSO import read_fasta, gc_percent, save_gc_csv, plot_gc_bar # oCall the CSV export function and save the figure.

seqs = read_fasta("data/data.fasta")

for sid, seq in seqs.items(): #Iterate through the dictionary: sid represents the sequence name and sequence its content.
    gcp = gc_percent(seq) # Apply the function to each sequence.
    print(f"{sid}\tlen={len(seq)}\tGC%={gcp:.4f}") # Display the ID, sequence length, and GC% with four decimal places.

save_gc_csv(seqs, "results/results_gc_content_PERSO.csv")
print("OK Fichier CSV créé : results/results_gc_content_PERSO.csv")

plot_gc_bar(seqs, "results/gc_PERSO_bar.png")
print("OK Graphique créé : results/gc_PERSO_bar.png")


