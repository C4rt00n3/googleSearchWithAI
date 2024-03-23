-- -----------------------------------------------------
-- Table `mydb`.`topic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`topic` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` LONGTEXT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name`(255) ASC) VISIBLE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`links`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`links` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `link` LONGTEXT NULL,
  `topic_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `topic_id_idx` (`topic_id` ASC) VISIBLE,
  CONSTRAINT `topic_id`
    FOREIGN KEY (`topic_id`)
    REFERENCES `mydb`.`topic` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`content` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` LONGTEXT NULL,
  `content` LONGTEXT NULL,
  `link_id` INT NULL, -- Removendo NOT NULL
  PRIMARY KEY (`id`),
  INDEX `link_id_idx` (`link_id` ASC) VISIBLE,
  CONSTRAINT `link_id`
    FOREIGN KEY (`link_id`)
    REFERENCES `mydb`.`links` (`id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
) ENGINE = InnoDB;
