def proteins(strand):
    triplets = [strand[i:i+3] for i in range(0, len(strand), 3)]
    decoder = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }
    protein = []
    for i in triplets:
        if decoder[i] == "STOP":
            break
        else:
            protein.append(decoder[i])
    return protein