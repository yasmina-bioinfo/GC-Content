from typing import Dict

def read_fasta(path: str) -> Dict[str, str]:
    """
    Lit un FASTA et renvoie un dict {id: sequence} en majuscules.
    Les caractères gardés sont A/C/G/T/N (on ignore tout le reste).
    """
    seqs: Dict[str, str] = {}
    sid = None          # identifiant de la séquence en cours
    chunks = []         # morceaux (lignes) de la séquence en cours

    with open(path, 'r', encoding='utf-8') as fh:
        for raw in fh:
            line = raw.strip()
            if not line:
                continue

            if line.startswith('>'):
                # si on était en train de remplir une séquence, on la cloture
                if sid is not None:
                    seqs[sid] = _sanitize(''.join(chunks))
                # on démarre une nouvelle séquence
                sid = line[1:].split()[0]
                chunks = []
            else:
                chunks.append(line)

    # fin de fichier : on enregistre la dernière séquence si elle existe
    if sid is not None:
        seqs[sid] = _sanitize(''.join(chunks))

    return seqs


def _sanitize(seq: str) -> str:
    """
    Met en majuscules et filtre pour ne garder que A/C/G/T/N.
    """
    s = seq.upper()
    return ''.join(ch for ch in s if ch in {'A', 'C', 'G', 'T', 'N'})
