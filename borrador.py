from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def blastn_search(query_sequence):
    # Crear un objeto de secuencia a partir de la secuencia de consulta
    query = SeqRecord(Seq(query_sequence))

    # Realizar la búsqueda BLASTn en la base de datos "nt" de NCBI
    result_handle = NCBIWWW.qblast("blastn", "nt", query.seq)

    # Analizar los resultados en formato XML
    blast_records = NCBIXML.parse(result_handle)

    # Obtener el primer registro BLAST
    blast_record = next(blast_records)

    # Obtener la secuencia de mayor similitud (la primera en el registro BLAST)
    top_hit = blast_record.alignments[0]

    # Imprimir el título y la descripción del hit de mayor similitud
    print("Secuencia de mayor similitud:")
    print("Título:", top_hit.title)
    print("Descripción:", top_hit.description)

# Ingresar la secuencia nucleotídica de consulta
query_sequence = input("Ingresa la secuencia nucleotídica de consulta: ")

# Realizar la búsqueda BLASTn
blastn_search(query_sequence)
