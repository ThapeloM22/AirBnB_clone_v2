-- creating a database and User
-- Grantin user select priv for performance_schema
-- Should not fail if database exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
