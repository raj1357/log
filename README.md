# LOG ANALYSIS

## Basic Data Operations by using SQL queries

### Developed by Raj Vamsi. 

## Abstract
It is a reporting page which prints out reports in a plain text format based on the data in database. This reporting tool is a python program using 'psycopg2' module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website.

## Questions
The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular articles of all time?
3. On which days did more than 1% of requests lead to errors?

## To Run program

1. To execute this program, the client/user will need to use a Virtual Machine(VM) to make sure that they are able to use the similar workspace that this project was built for running on your computer. Download the distributions "Vagrant" and "VirtualBox" to install and manage your virtual machine. Use 'vagrant up' to bring the virtal machine online and 'vagrant ssh' to login.
2. Download the data provided here. Unzip the file in order to extract newsdata.sql. This file
 should be inside the Vagrant folder.
3. Load the database using psql -d news -f newsdata.sql.
4. connect to the database using psql -d news.
5. Create the Queries given below. Then exit psql.
6. Now execute the Python file -python log_analysis.py


