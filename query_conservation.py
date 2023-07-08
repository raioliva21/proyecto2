from Bio import AlignIO
from Bio.Align import AlignInfo

def analyze_conservation(sequence):
    # Crear un objeto de alineamiento a partir de la secuencia
    alignment = AlignIO.MultipleSeqAlignment([sequence])

    # Obtener la información de conservación del alineamiento
    summary_align = AlignInfo.SummaryInfo(alignment)

    # Obtener los sitios de mayor conservación
    conservation = summary_align.pos_specific_score()

    # Imprimir los sitios de mayor conservación
    print("Sitios de mayor conservación:")
    for pos, score in conservation.items():
        print("Posición:", pos, "Conservación:", score)