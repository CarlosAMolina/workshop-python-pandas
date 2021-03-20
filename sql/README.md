## Create DB and tables with data

First, we connect to the database using the commands explained in the docker folder.

In that folder you can see the server's password.

We can import the database or create all the information manually.

### Import the database

First, the database must exist

```bash
CREATE DATABASE funds;
```

Exit the connection to the mysql server and import the database with:

```bash
mysql -hlocalhost --protocol=TCP -uroot -p funds < export/funds_db.txt
```

You can export the database with:

```bash
mysqldump -hlocalhost --protocol=TCP -uroot -p funds > export/funds_db.txt
```

### Create database, tables and information manually

To create the database and tables, run the commads in the folder create_db_manually/sql_sentences/

Import the tables data, this informaion is in the folder create_db_manually/tables_data/

