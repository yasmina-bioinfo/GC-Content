![Python](https://img.shields.io/badge/Python-3.x-blue svg)
# Mini-Projet 3 — GC Content Analysis

**Period :** 2025-11-08 → 2025-11-15
**Approx. duration :** 8 jours  
**Status :**Completed ✅

---

## Overview
This mini-project implements a complete and personal pipeline for analyzing DNA sequences stored in FASTA format.
The goal is to read multiple sequences, compute their GC percentage, and produce:
  - a CSV file summarizing the results
  - a bar chart visualizing GC% for each sequence
Through this project, I practiced essential bioinformatics skills:
  - writing a custom FASTA parser
  - manipulating strings and dictionaries
  - implementing a biological calculation (GC%)
  - exporting structured data (CSV)
  - creating scientific graphics with Matplotlib
  - organizing reusable and clean code in functions
---

## Features

1. Custom FASTA Reader
  - Supports multi-line sequences
  - Handles UTF-8 BOM automatically
  - Skips empty lines
  - Returns a dictionary like:
  {"seq1": "ATGC...", "seq2": "GGGCCC...", ...}

2. GC Content Calculation
The GC% is computed using the formula:
𝐺𝐶%=(𝐺+𝐶/𝐴+𝑇+𝐺+𝐶) ×100

3. CSV Export
Creates a file containing:
  - Sequence ID
  - Length
  - GC percentage
File: **results_gc_content.csv

4. Bar Chart 
Generates a PNG figure showing GC% per sequence 
File: **gc_content_bar.png

## How to Run
From the project folder : python -m src_perso.test
Outputs:
  - GC% printed in the terminal
  - results_gc_content.csv generated
  - gc_content_bar.png saved 
---

## Tools Used
- **Python 3**  
- **Matplotlib** → création de graphiques / graph generation  
- **CSV module** → sauvegarde des résultats / save results  
- **Visual Studio Code** → environnement de développement / development environment

---

## Résultats obtenus / Results

- **Fichier / File :** `results_gc_content.csv` → contient le %GC de chaque séquence / contains the GC% for each sequence  
- **Graphique / Chart :** `results/gc_bar.png` → diagramme en barres du %GC / bar plot of GC content  

---

## Notes personnelles / Personal Notes


Ce projet m’a aidée à mieux comprendre :
- la lecture et la structure d’un fichier FASTA / how to read and structure a FASTA file  
- la logique d’une fonction bioinformatique (`gc_percent`) / the logic of a bioinformatics function  
- le flux complet lecture → calcul → sauvegarde → visualisation / the complete data flow  
- l’organisation d’un projet Python en modules (`src/`) / how to organize a Python project into modules  

> *Projet réalisé dans le cadre de mon apprentissage guidé de la bioinformatique, en cherchant à comprendre chaque étape pas à pas.*  
> *Project completed as part of my guided learning journey in bioinformatics, aiming to understand each step step-by-step.*

### Notes
Code inspired and adapted from learning sessions with AI and Coursera.
All scripts are fully understood, rewritten by me, tested, and commented by me.

---

## Structure du dossier / Folder Structure
GCContent/
│
├── data/
│   ├── data.fasta              # Main FASTA file used for GC analysis
│   └── toy.fasta               # Small FASTA file used for testing
│
├── results/
│   ├── gc_bar.png              # Plot generated from earlier versions
│   ├── gc_PERSO_bar.png        # Plot generated with my own final code
│   ├── results_gc_content.csv  # CSV from earlier versions
│   └── results_gc_content_PERSO.csv   # CSV generated with my own code
│
├── src_learning/               # (Optional) Exploratory /learning scripts
│
├── src_perso/
│   ├── __init__.py             # Marks this directory as a Python module
│   ├── gc_content_PERSO.py     # Final personal implementation, Functions for FASTA parsing, GC%, CSV export, and plotting
│   └── test.py                 # Main script that runs the full analysis pipeline
│
└── README.md                   # Project documentation (English)


