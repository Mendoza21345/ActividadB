from google.cloud import bigquery

def ejecutar_consulta():
    # Configura tu proyecto y crea un cliente de BigQuery
    proyecto = "tu-proyecto"  # Reemplaza con tu ID de proyecto
    client = bigquery.Client(project=proyecto)

    # Especifica tu nueva consulta SQL para obtener el total agrupado por "family" y "species"
    nueva_consulta = """
        SELECT family, species, COUNT(*) AS cantidad_total
        FROM `bigquery-public-data.gbif.occurrences`
        WHERE family IS NOT NULL AND species IS NOT NULL
        GROUP BY family, species;
    """

    # Ejecuta la nueva consulta
    resultados = client.query(nueva_consulta)

    # Imprime los resultados
    for fila in resultados:
        print(fila)

if __name__ == "__main__":
    ejecutar_consulta()
