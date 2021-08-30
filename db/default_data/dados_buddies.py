from db.default_data.default_create_table_with_underline_structure import default_create_table_structure_buddies

script_create_table_buddies = lambda dados = {} : f"""
    DROP TABLE IF EXISTS Buddies;
    
    CREATE TABLE Buddies (
        {default_create_table_structure_buddies()}
    );
"""