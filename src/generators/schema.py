def generate_schema(blueprint_list):
    sql = []
    for bp in blueprint_list:
        sql.append(f"CREATE TABLE {bp} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT);")
    return "\n".join(sql)
