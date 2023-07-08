import sys
from Bio import SeqIO
from query_search import blastn_search
from query_conservation import analyze_conservation
from query_translation import translate_sequence
import concurrent.futures


#def generate_report(genomic_location, query_sequence, protein_sequence)
    

def process_sequence(sequence):
    print("A")
    # Realizar la búsqueda BLASTn
    blastn_search(sequence.seq)

    # Analizar los sitios de mayor conservación de la secuencia
    analyze_conservation(sequence.seq)

    # Traducir la secuencia a proteína
    translate_sequence(sequence.seq)


def main(file_path):
    # Leer el archivo FASTA
    sequences = SeqIO.parse(file_path, "fasta")

    # Crear un conjunto de hebras
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Procesar cada secuencia en paralelo
        futures = [executor.submit(process_sequence, sequence) for sequence in sequences]

        # Esperar a que todas las hebras terminen
        concurrent.futures.wait(futures)


# Verificar si se proporciona una ruta de archivo como argumento de línea de comandos
if len(sys.argv) > 1:
    # Obtener la ruta de archivo del argumento de línea de comandos
    file_path = sys.argv[1]
    # Llamar a la función principal con la ruta de archivo
    main(file_path)
else:
    print("No se proporcionó una ruta de archivo.")


