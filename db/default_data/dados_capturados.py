from db.default_data.default_create_table_with_underline_structure import default_create_table_structure_capturados

script_create_table_capturados = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Capturados;
    
    CREATE TABLE Capturados (
        {default_create_table_structure_capturados()}
    );
"""