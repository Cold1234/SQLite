import sys 


database_file_path = sys.argv[1]
command            = sys.argv[2]


if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:
        database_file.seek(16) # Skip the first 16 bytes of the header 
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")
        database_file.seek(40) # Skip the first 40 bytes of the header
        number_tables = int.from_bytes(database_file.read(4), byteorder="big")
        print(f"number of tables: {number_tables}")

else:
    print(f"Ivalid command: {command}")
