CREATE  DATABASE notifications CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'root'@'%' IDENTIFIED BY 'QWEqwe!1';
GRANT ALL PRIVILEGES ON notifications.* TO 'root'@'%';
FLUSH PRIVILEGES;
