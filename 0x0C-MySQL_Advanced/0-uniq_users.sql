CREATE TABLE IF NOT EXISTS `users` (
  `id` INTEGER UNSIGNED PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255)
)
