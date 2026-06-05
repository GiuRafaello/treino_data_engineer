for tabela in tabelas:

    print(f"\nLendo {tabela}...")

    df = pd.read_sql(
        f"SELECT * FROM {tabela}",
        engine
    )

    # Debug
    print(df.dtypes)

    # Tratamentos específicos
    if tabela == "gold_analitico_vendas":

        df["data_venda"] = pd.to_datetime(
            df["data_venda"],
            errors="coerce"
        )

        df["quantidade"] = pd.to_numeric(
            df["quantidade"],
            errors="coerce"
        )

        df["valor_unitario"] = pd.to_numeric(
            df["valor_unitario"],
            errors="coerce"
        )

        df["valor_total"] = pd.to_numeric(
            df["valor_total"],
            errors="coerce"
        )

        df["taxa_selic"] = pd.to_numeric(
            df["taxa_selic"],
            errors="coerce"
        )

    destino = f"{PROJECT_ID}.{DATASET_ID}.{tabela}"

    print(f"Enviando {len(df)} registros para {destino}")

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE"
    )

    job = client.load_table_from_dataframe(
        df,
        destino,
        job_config=job_config
    )

    job.result()

    print(f"{tabela} carregada com sucesso!")