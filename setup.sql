CREATE TABLE data_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(45),
    summary VARCHAR(512),
    decription TEXT
);

--insert 3 records

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Integer",
    "Integer values",
    "A data type that stores an integer value"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Float",
    "Floating point value",
    "A data type that stores allows us to store multiple values after the decimal"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Boolean",
    "True or False values",
    "Named after George Boole (Boolean algegra); These can take true or false values"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Strings",
    "Text Values",
    "A data type that stores a string value"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Lists",
    "Non-Null values",
    "a collection type that can store ordered non-NULL elements of the same SQL data type"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Dictionaries",
    "Various values",
    "Contains information about database objects such as tables, indexes, columns, datatypes, and views"
);

INSERT INTO data_type (
    name,
    summary,
    decription
) VALUES (
    "Tuples",
    "One Record, One Row",
    "Contains all the data for an individual record."
);
