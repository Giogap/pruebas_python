-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS contact_db;
CREATE USER IF NOT EXISTS 'root' IDENTIFIED BY 'contrasena_nueva';
GRANT ALL ON `contacts_db`.* TO 'root';
GRANT SELECT ON `performance_schema`.* TO 'root';
FLUSH PRIVILEGES;