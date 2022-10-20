class Table:
    def __init__(self, data=None, column_names=None):
        if data is None:
            data = []
        if column_names is None:
            column_names = []
        self.__table = data
        self.column_names = column_names

    def __str__(self):
        string = ""
        for row in self.__table:
            string += str(row) + "\n"
        return string

    def __getitem__(self, x):
        if isinstance(x, int):
            return self.__table[x]
        elif isinstance(x, str):
            column_values = []
            for row in self.__table:
                column_values.append(row[x])
            return column_values
        else:
            return ValueError(f"Cannot accept arguments of type {type(x)}")

    def __setitem__(self, key, value):
        if isinstance(key, int) and isinstance(value, dict) and value.keys() == set(self.column_names):
            self.__table[key] = value
        else:
            return ValueError(f"Cannot accept arguments of type {type(key)} or {type(value)}")

    def __len__(self):
        return len(self.__table)

    def append(self, row: dict):
        if row.keys() == set(self.column_names):
            self.__table.append(row)
        else:
            return ValueError(f"Row must have keys equal to column names")

    def find_row_by_value(self, value, column_name):
        if column_name in self.column_names:
            for i, row in enumerate(self.__table):
                if row[column_name] == value:
                    return self.__table[i]
        return ValueError(f"No column named {column_name}")

    def save_as(self, filename):
        with open(filename, 'w') as file:
            for name in self.column_names:
                file.write(name + "    ")
            file.write("\n")
            for row in self.__table:
                for value in row.values():
                    file.write("\t\t" + str(value) + "\t\t\t")
                file.write("\n")
