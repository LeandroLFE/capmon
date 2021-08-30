from db.default_data.default_create_table_with_underline_structure import default_create_table_structure_aventureiros

script_create_table_aventureiros = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Aventureiros;
    
    CREATE TABLE Aventureiros (
        {default_create_table_structure_aventureiros()}
    );
"""