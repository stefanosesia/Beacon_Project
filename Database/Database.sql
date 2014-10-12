-- Code by WeHaveCake - Stefano Sesia, Seoras MacDonald & Andrew McCluskey 
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wehavecake
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema wehavecake
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wehavecake` DEFAULT CHARACTER SET latin1 ;
USE `wehavecake` ;

-- -----------------------------------------------------
-- Table `wehavecake`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wehavecake`.`user` (
  `Username` VARCHAR(20) NOT NULL,
  `HashPass` VARCHAR(256) NOT NULL,
  `EMail` VARCHAR(30) NOT NULL,
  `CurrentLocation` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`Username`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `wehavecake`.`friendship`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wehavecake`.`friendship` (
  `User1` VARCHAR(20) NOT NULL,
  `User2` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`User1`, `User2`),
  INDEX `Frienship2_idx` (`User2` ASC),
  CONSTRAINT `Friendship`
    FOREIGN KEY (`User1`)
    REFERENCES `wehavecake`.`user` (`Username`)
    ON UPDATE CASCADE,
  CONSTRAINT `Frienship2`
    FOREIGN KEY (`User2`)
    REFERENCES `wehavecake`.`user` (`Username`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `wehavecake`.`routes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wehavecake`.`routes` (
  `Node1` VARCHAR(50) NOT NULL,
  `Start` DATETIME NOT NULL,
  `Username` VARCHAR(20) NOT NULL,
  `ID` INT(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`),
  INDEX `Moves_idx` (`Username` ASC),
  CONSTRAINT `Moves`
    FOREIGN KEY (`Username`)
    REFERENCES `wehavecake`.`user` (`Username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
