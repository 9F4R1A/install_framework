-- Secure mariadb
ALTER USER 'root'@'localhost' IDENTIFIED BY '12345678';
DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
-- FLUSH PRIVILEGES
FLUSH PRIVILEGES;