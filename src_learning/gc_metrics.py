def gc_percent(seq: str) -> float:
    """
    Pourcentage de GC dans 'seq' (en ignorant 'N' dans le dénominateur).
    Renvoie un float entre 0 et 100.
    Cas particuliers gérés :
    - séquence vide -> 0.0
    - séquence ne contenant que des 'N' -> 0.0
    """
    if not seq:
        return 0.0
    s = seq.upper()
    g = s.count('G')
    c = s.count('C')
    a = s.count('A')
    t = s.count('T')
    denom = a + c + g + t
    if denom == 0:
        return 0.0
    return 100.0 * (g + c) / denom
