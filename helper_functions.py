from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read the rows of a csv into a table."""

    result: list[dict[str,str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row oriented table to a column oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result

def filter_table(row_table: list[dict[str,str]], key: str, value: str) -> list[dict[str,str]]:
    """Pull the rows of a table with the wanted value."""
    result: list[dict[str,str]] = []
    for row in row_table:
        if row[key] == value:
            result.append(row)
    return result

def add_column_values(vals: list[str]) -> str:
    """Adds the values of a column together, and returns them as a string."""
    result: float = 0
    for val in vals:
        result += float(val)
    return str(result)