CREATE DATABASE IF NOT EXISTS `store`;
CREATE DATABASE IF NOT EXISTS `delivery`;
CREATE DATABASE IF NOT EXISTS `order`;
CREATE DATABASE IF NOT EXISTS `account`;
CREATE DATABASE IF NOT EXISTS `courier`;
GRANT ALL ON `store`.* TO 'user'@'%';
GRANT ALL ON `delivery`.* TO 'user'@'%';
GRANT ALL ON `order`.* TO 'user'@'%';
GRANT ALL ON `account`.* TO 'user'@'%';
GRANT ALL ON `courier`.* TO 'user'@'%';