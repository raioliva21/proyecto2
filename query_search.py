#Busqueda de secuencia consulta en Base de Datos nucleotidicas de NCBI mediante algoritmo BLASTn

from Bio.Blast import NCBIWWW, NCBIXML

def blastn_search(query_sequence):

    # Realizar la búsqueda BLASTn en la base de datos "nt" de NCBI
    result_handle = NCBIWWW.qblast("blastn", "nt", query_sequence)

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

