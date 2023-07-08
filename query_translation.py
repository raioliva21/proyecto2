
def translate_sequence(sequence):
    # Traducir la secuencia de ADN a proteína
    protein_sequence = sequence.translate()

    # Imprimir la secuencia de proteína
    print("Secuencia de proteína:")
    print(protein_sequence)