## Steps to run the MySQL server

### Download image

```bash
docker pull mysql
```

### Create volume

```bash
docker volume create mysql-volume
```

### Start instance

We are using the simple password: pw

```bash
docker run --rm --name mysql-local -p3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=pw -d mysql:latest
```

To check the instance is working correctly, we are going to access it using the command line:

```bash
mysql -hlocalhost --protocol=TCP -uroot -p
```

