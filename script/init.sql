CREATE USER IF NOT EXISTS 'copter50029'@'%' IDENTIFIED BY 'copter12345';
GRANT ALL PRIVILEGES ON *.* TO 'copter50029'@'%';
FLUSH PRIVILEGES;
-- login to mysql with the following command
-- docker exec -it license-plate-mysql mysql -u copter50029 -p'copter12345' licence-plate
USE `licence-plate`;

CREATE TABLE IF NOT EXISTS `license_plates` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `plate_id` VARCHAR(15) NOT NULL,
  `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `image_url` TEXT NOT NULL,
  `camera_id` VARCHAR(10) NOT NULL
);