def to_rna(dna_strand):
    rna = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    transcript = [rna[i] for i in dna_strand]
    return "".join(transcript)