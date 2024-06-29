CREATE DATABASE  IF NOT EXISTS `nova_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `nova_db`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: nova_db
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bond`
--

DROP TABLE IF EXISTS `bond`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bond` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `density` varchar(45) DEFAULT NULL,
  `hardness_HRB` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `sint_temp` varchar(45) DEFAULT NULL,
  `sint_time` varchar(45) DEFAULT NULL,
  `ballmill_time` varchar(45) DEFAULT NULL,
  `mixing_time` varchar(45) DEFAULT NULL,
  `method` varchar(45) DEFAULT NULL,
  `Co` varchar(45) DEFAULT NULL,
  `Fe` varchar(45) DEFAULT NULL,
  `Cu#300` varchar(45) DEFAULT NULL,
  `Cu#600` varchar(45) DEFAULT NULL,
  `Ni` varchar(45) DEFAULT NULL,
  `CuSn#67` varchar(45) DEFAULT NULL,
  `CuSn#80` varchar(45) DEFAULT NULL,
  `Sn#300` varchar(45) DEFAULT NULL,
  `Sn#600` varchar(45) DEFAULT NULL,
  `W` varchar(45) DEFAULT NULL,
  `WC` varchar(45) DEFAULT NULL,
  `W₂C` varchar(45) DEFAULT NULL,
  `S` varchar(45) DEFAULT NULL,
  `Ag` varchar(45) DEFAULT NULL,
  `P₂O₅` varchar(45) DEFAULT NULL,
  `Zn` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bond`
--

LOCK TABLES `bond` WRITE;
/*!40000 ALTER TABLE `bond` DISABLE KEYS */;
INSERT INTO `bond` VALUES ('BO000000001','2024-05-07 10:57:55','2024-05-17 11:21:00','1','Q301','YELLOW','8.82','64',NULL,'878',NULL,NULL,NULL,NULL,'45',NULL,'26',NULL,'24',NULL,NULL,NULL,'5',NULL,NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000002','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q302','P.Blue','8.76','40~60',NULL,'760',NULL,NULL,NULL,NULL,'60',NULL,'32',NULL,NULL,NULL,NULL,NULL,'8',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('BO000000003','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q303','White','8.82','80',NULL,'760',NULL,NULL,NULL,NULL,'20',NULL,'9',NULL,NULL,NULL,'70','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('BO000000004','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q304',NULL,'8.75','80',NULL,'680',NULL,NULL,NULL,NULL,'20',NULL,'9',NULL,NULL,'70',NULL,'1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('BO000000005','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q305','Orange','8.82','80',NULL,'760',NULL,NULL,NULL,NULL,'25',NULL,NULL,NULL,NULL,NULL,'75',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('BO000000006','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q501','RED','10.17','105',NULL,'878',NULL,NULL,NULL,NULL,'12',NULL,'24',NULL,'34',NULL,NULL,NULL,'5','25',NULL,NULL,NULL,NULL,'0.4',NULL),('BO000000007','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q502','BLUE','10.92','110',NULL,'878',NULL,NULL,NULL,NULL,'10',NULL,'13.5',NULL,'36',NULL,NULL,'4.5',NULL,'36',NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000008','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q701','SILVER','10.62','105',NULL,'1015',NULL,NULL,NULL,NULL,'70',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'30',NULL,NULL,NULL,NULL,'0.55',NULL),('BO000000009','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q702','BROWN','12.06','104',NULL,'878','30',NULL,NULL,NULL,'5',NULL,'21',NULL,'20',NULL,NULL,'4',NULL,'50',NULL,NULL,NULL,NULL,'0.2',NULL),('BO000000010','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q703','GOLD','10.74','92',NULL,'1030',NULL,NULL,NULL,NULL,'30',NULL,'6',NULL,'20',NULL,NULL,NULL,'2',NULL,'42',NULL,NULL,NULL,'0.5',NULL),('BO000000011','2024-05-07 10:57:55','2024-05-17 11:21:00','1','Q705*','BLACK-TEST','11.83','95',NULL,'1015',NULL,NULL,NULL,NULL,'36',NULL,'10',NULL,NULL,NULL,'8',NULL,NULL,'46',NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000012','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q705+','BLACK-TEST','11.84','112',NULL,'1015',NULL,NULL,NULL,NULL,'46',NULL,'6',NULL,NULL,NULL,'2',NULL,NULL,'46',NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000013','2024-05-07 10:57:55','2024-05-17 11:21:00','3','Q705^','BLACK-TEST','11.84',NULL,NULL,'1015',NULL,NULL,NULL,NULL,'40',NULL,'10',NULL,NULL,NULL,'4',NULL,NULL,'46',NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000014','2024-05-07 10:57:55','2024-05-17 11:21:00',NULL,'Q706','XB-Silver','11.34','105',NULL,'900',NULL,NULL,NULL,NULL,'40',NULL,'6',NULL,'8',NULL,'6',NULL,NULL,'40',NULL,NULL,NULL,NULL,'0.5',NULL),('BO000000017','2024-05-20 18:08:26','2024-05-20 18:08:26',NULL,NULL,NULL,NULL,NULL,'0.00',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('BO000000018','2024-05-20 18:08:30','2024-05-20 18:08:30',NULL,'asd',NULL,NULL,NULL,'0.00',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `bond` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_bond_insert` BEFORE INSERT ON `bond` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    DECLARE powder_ratio DECIMAL(10, 2);
    DECLARE powder_price DECIMAL(10, 2);
    DECLARE temp_ratio DECIMAL(10, 2);
    DECLARE temp_price DECIMAL(10, 2);
    -- ----------------------------------------------------------------------
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM bond;
    SET NEW.sys_id = CONCAT('BO', LPAD(next_id, 9, '0'));
    -- ----------------------------------------------------------------------
    SET powder_ratio = 0;
	SET powder_price = 0;

    IF NEW.Co IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Co') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.Co AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;
  
	IF NEW.Fe IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Fe') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.Fe AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;
    
	IF NEW.`Cu#300` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Cu #300') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Cu#300` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Cu#600` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Cu #600') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Cu#600` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Ni` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Ni') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.Ni AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`CuSn#67` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'CuSn #67') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`CuSn#67` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`CuSn#80` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'CuSn #80') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`CuSn#80` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;        
    
	IF NEW.`Sn#300` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Sn #300') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Sn#300` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Sn#600` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Sn #600') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Sn#600` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`W` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'W') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`W` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`WC` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'WC') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`WC` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;         
    
	IF NEW.`W₂C` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'W₂C') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`W₂C` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;        
    
	IF NEW.`S` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'S') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.S AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Ag` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Ag') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Ag` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`P₂O₅` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'P₂O₅') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`P₂O₅` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;    
    
	IF NEW.`Zn` IS NOT NULL THEN
        SET temp_price = CAST((SELECT price FROM powder WHERE powder.chemical_symbol = 'Zn') AS DECIMAL(10, 2)) * 0.01;
        SET temp_ratio = CAST(NEW.`Zn` AS DECIMAL(10, 2));
        SET powder_price = powder_price + temp_price;
    END IF;         
    
	SET NEW.price = CAST(powder_price AS DECIMAL(10, 2));    
    -- ----------------------------------------------------------------------
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `bond_BEFORE_UPDATE` BEFORE UPDATE ON `bond` FOR EACH ROW BEGIN
	SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `customer_name` varchar(45) DEFAULT NULL,
  `customer_id` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('CU000000001','2024-05-07 10:50:07','2024-05-12 01:21:52','6','customer1','c1'),('CU000000002','2024-05-07 10:50:12','2024-05-12 01:21:52','6','customer2','c2'),('CU000000003','2024-05-20 17:11:23','2024-05-20 17:11:23',NULL,'해돋이','SR');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_customer_insert` BEFORE INSERT ON `customer` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM customer;
    SET NEW.sys_id = CONCAT('CU', LPAD(next_id, 9, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `customer_BEFORE_UPDATE` BEFORE UPDATE ON `customer` FOR EACH ROW BEGIN
	SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `diamond`
--

DROP TABLE IF EXISTS `diamond`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diamond` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diamond`
--

LOCK TABLES `diamond` WRITE;
/*!40000 ALTER TABLE `diamond` DISABLE KEYS */;
INSERT INTO `diamond` VALUES ('DI000000001','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #100/120','110'),('DI000000002','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #12/14',''),('DI000000003','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #120/140','110'),('DI000000004','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #14/16',''),('DI000000005','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #140/170','120'),('DI000000006','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #20/30','240'),('DI000000007','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #30/40','115'),('DI000000008','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #30/40 T','130'),('DI000000009','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #40/50','100'),('DI000000010','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #50/60','100'),('DI000000011','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #6/8',''),('DI000000012','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #60/80','110'),('DI000000013','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #8/10',''),('DI000000014','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2040 #80/100','110'),('DI000000015','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2050 #16/18','440'),('DI000000016','2024-05-07 10:48:41','2024-05-07 10:48:41',NULL,'2060 #100/120 T','140'),('DI000000017','2024-05-20 17:15:11','2024-05-20 17:15:11',NULL,'2048#123','170');
/*!40000 ALTER TABLE `diamond` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_diamond_insert` BEFORE INSERT ON `diamond` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM diamond;
    SET NEW.sys_id = CONCAT('DI', LPAD(next_id, 9, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `diamond_BEFORE_UPDATE` BEFORE UPDATE ON `diamond` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `ip`
--

DROP TABLE IF EXISTS `ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `sys_item1_id` varchar(45) DEFAULT NULL,
  `sys_item2_id` varchar(45) DEFAULT NULL,
  `sys_item3_id` varchar(45) DEFAULT NULL,
  `sys_item4_id` varchar(45) DEFAULT NULL,
  `sys_seg1_id` varchar(45) DEFAULT NULL,
  `sys_seg2_id` varchar(45) DEFAULT NULL,
  `sys_sp1_id` varchar(45) DEFAULT NULL,
  `sys_sp2_id` varchar(45) DEFAULT NULL,
  `sys_shank1_id` varchar(45) DEFAULT NULL,
  `sys_shank2_id` varchar(45) CHARACTER SET armscii8 COLLATE armscii8_general_ci DEFAULT NULL,
  `sys_shank3_id` varchar(45) DEFAULT NULL,
  `sys_shank4_id` varchar(45) DEFAULT NULL,
  `sys_sub1_id` varchar(45) DEFAULT NULL,
  `sys_sub2_id` varchar(45) DEFAULT NULL,
  `sys_sub3_id` varchar(45) DEFAULT NULL,
  `sys_sub4_id` varchar(45) DEFAULT NULL,
  `ip_no` varchar(45) DEFAULT NULL,
  `ip_no1` varchar(45) DEFAULT NULL,
  `ip_no2` varchar(45) DEFAULT NULL,
  `ip_no3` varchar(45) DEFAULT NULL,
  `creation_date` varchar(45) DEFAULT NULL,
  `due_date` varchar(45) DEFAULT NULL,
  `item_group_name` varchar(45) DEFAULT NULL,
  `item1_name` varchar(45) DEFAULT NULL,
  `item1_amount` varchar(45) DEFAULT NULL,
  `item2_name` varchar(45) DEFAULT NULL,
  `item2_amount` varchar(45) DEFAULT NULL,
  `item3_name` varchar(45) DEFAULT NULL,
  `item3_amount` varchar(45) DEFAULT NULL,
  `item4_name` varchar(45) DEFAULT NULL,
  `item4_amount` varchar(45) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  `seg1_no` varchar(45) DEFAULT NULL,
  `seg1_sp_no` varchar(45) DEFAULT NULL,
  `seg1_amount` varchar(45) DEFAULT NULL,
  `seg1_memo1` varchar(45) DEFAULT NULL,
  `seg1_memo2` varchar(45) DEFAULT NULL,
  `seg2_no` varchar(45) DEFAULT NULL,
  `seg2_sp_no` varchar(45) DEFAULT NULL,
  `seg2_amount` varchar(45) DEFAULT NULL,
  `seg2_memo1` varchar(45) DEFAULT NULL,
  `seg2_memo2` varchar(45) DEFAULT NULL,
  `shank1_name` varchar(45) DEFAULT NULL,
  `shank1_amount` varchar(45) DEFAULT NULL,
  `shank2_name` varchar(45) DEFAULT NULL,
  `shank2_amount` varchar(45) DEFAULT NULL,
  `shank3_name` varchar(45) DEFAULT NULL,
  `shank3_amount` varchar(45) DEFAULT NULL,
  `shank4_name` varchar(45) DEFAULT NULL,
  `shank4_amount` varchar(45) DEFAULT NULL,
  `shank_memo1` varchar(45) DEFAULT NULL,
  `shank_memo2` varchar(45) DEFAULT NULL,
  `sub1_name` varchar(45) DEFAULT NULL,
  `sub1_amount` varchar(45) DEFAULT NULL,
  `sub1_memo1` varchar(45) DEFAULT NULL,
  `sub1_memo2` varchar(45) DEFAULT NULL,
  `sub2_name` varchar(45) DEFAULT NULL,
  `sub2_amount` varchar(45) DEFAULT NULL,
  `sub2_memo1` varchar(45) DEFAULT NULL,
  `sub2_memo2` varchar(45) DEFAULT NULL,
  `sub3_name` varchar(45) DEFAULT NULL,
  `sub3_amount` varchar(45) DEFAULT NULL,
  `sub3_memo1` varchar(45) DEFAULT NULL,
  `sub3_memo2` varchar(45) DEFAULT NULL,
  `sub4_name` varchar(45) DEFAULT NULL,
  `sub4_amount` varchar(45) DEFAULT NULL,
  `sub4_memo1` varchar(45) DEFAULT NULL,
  `sub4_memo2` varchar(45) DEFAULT NULL,
  `welding1` varchar(300) DEFAULT NULL,
  `welding2` varchar(300) DEFAULT NULL,
  `dressing1` varchar(300) DEFAULT NULL,
  `dressing2` varchar(300) DEFAULT NULL,
  `paint1` varchar(300) DEFAULT NULL,
  `paint2` varchar(300) DEFAULT NULL,
  `memo1` varchar(300) DEFAULT NULL,
  `memo2` varchar(300) DEFAULT NULL,
  `memo3` varchar(300) DEFAULT NULL,
  `memo4` varchar(300) DEFAULT NULL,
  `checked` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip`
--

LOCK TABLES `ip` WRITE;
/*!40000 ALTER TABLE `ip` DISABLE KEYS */;
INSERT INTO `ip` VALUES ('IP000000001','2024-05-12 02:40:06','2024-05-12 02:40:16',NULL,'IT000000022',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,NULL,'SH000000001',NULL,NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0001','2024','IP0001','2024-IP0013','2024-05-12','12345','TEST','TEST_ITEM','1','','','','','','','','SQ0000','','2','','','SQ9999','','1','','','3\"DISC-CCW','1','','','','','','','TEST','TEST','PCD10','2','','','PCD12','1','','','','','','','','','','','','','','','TEST','','dkwkdkwkdkQyd','','','','1'),('IP000000002','2024-05-12 02:40:24','2024-05-14 19:18:57',NULL,'IT000000023',NULL,NULL,NULL,'SE000000001','SE000000086','SP000000003','SP000000007','SH000000002',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0002','2024','IP0002','2024-IP0012','2024-05-12','235235','TEST','TEST_ITEM2','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000','2024-SP0001','2',NULL,NULL,'SQ9999','2024-SP0005','2',NULL,NULL,'3\"DISC-CW','2',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'2'),('IP000000003','2024-05-13 09:04:09','2024-05-13 09:04:09',NULL,'IT000000022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0003','2024','IP0003',NULL,'2024-05-13',NULL,NULL,'TEST_ITEM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IP000000004','2024-05-13 09:07:26','2024-05-13 09:07:26',NULL,'IT000000022',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0004','2024','IP0004',NULL,'2024-05-13',NULL,NULL,'TEST_ITEM',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IP000000005','2024-05-13 09:07:34','2024-05-13 09:07:34',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0005','2024','IP0005',NULL,'2024-05-13',NULL,'TEST',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IP000000006','2024-05-13 09:08:36','2024-05-14 19:18:57',NULL,'IT000000023',NULL,NULL,NULL,'SE000000001','SE000000086','SP000000006','SP000000007','SH000000002',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0006','2024','IP0006','2024-IP0002','2024-05-13','235235','TEST','TEST_ITEM2','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000','2024-SP0004','2',NULL,NULL,'SQ9999','2024-SP0005','2',NULL,NULL,'3\"DISC-CW','2',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'2'),('IP000000007','2024-05-13 09:09:33','2024-05-14 19:18:57',NULL,'IT000000022',NULL,NULL,NULL,'SE000000001','SE000000086','SP000000006','SP000000007','SH000000001',NULL,NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0007','2024','IP0007','2024-IP0004','2024-05-13','12345','TEST','TEST_ITEM','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000','2024-SP0004','2',NULL,NULL,'SQ9999','2024-SP0005','1',NULL,NULL,'3\"DISC-CCW','1',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST','PCD10','2',NULL,NULL,'PCD12','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'2'),('IP000000008','2024-05-14 18:51:30','2024-05-14 19:18:57',NULL,'IT000000022','IT000000023',NULL,NULL,'SE000000001','SE000000086',NULL,'SP000000007','SH000000001','SH000000002',NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0008','2024','IP0008','2024-IP0007','2024-05-14','235235','TEST','TEST_ITEM','1','TEST_ITEM2','2',NULL,NULL,NULL,NULL,NULL,'SQ0000',NULL,'4',NULL,NULL,'SQ9999','2024-SP0005','3',NULL,NULL,'3\"DISC-CCW','1','3\"DISC-CW','2',NULL,NULL,NULL,NULL,'TEST','TEST','PCD10','2',NULL,NULL,'PCD12','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'1'),('IP000000009','2024-05-17 09:45:06','2024-05-17 10:37:43',NULL,'IT000000022','IT000000023',NULL,NULL,'SE000000001','SE000000086',NULL,'SP000000008','SH000000001','SH000000002',NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0009','2024','IP0009','2024-IP0008','2024-05-17','235235','TEST','TEST_ITEM','1','TEST_ITEM2','2',NULL,NULL,NULL,NULL,NULL,'SQ0000',NULL,'4',NULL,NULL,'SQ9999','2024-SP0006','3',NULL,NULL,'3\"DISC-CCW','1','3\"DISC-CW','2',NULL,NULL,NULL,NULL,'TEST','TEST','PCD10','2',NULL,NULL,'PCD12','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'1'),('IP000000010','2024-05-17 09:45:28','2024-05-17 10:37:43',NULL,'IT000000022',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,'SP000000008','SH000000001',NULL,NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0010','2024','IP0010','2024-IP0009','2024-05-17','12345','TEST','TEST_ITEM','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000',NULL,'2',NULL,NULL,'SQ9999','2024-SP0006','1',NULL,NULL,'3\"DISC-CCW','1',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST','PCD10','2',NULL,NULL,'PCD12','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'1'),('IP000000011','2024-05-17 10:29:43','2024-05-17 10:37:43',NULL,'IT000000023',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,'SP000000008','SH000000002',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0011','2024','IP0011','2024-IP0009','2024-05-17','235235','TEST','TEST_ITEM2','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000',NULL,'2',NULL,NULL,'SQ9999','2024-SP0006','2',NULL,NULL,'3\"DISC-CW','2',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'1'),('IP000000012','2024-05-17 20:25:28','2024-05-17 20:31:07',NULL,'IT000000022',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,NULL,'SH000000001',NULL,NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0012','2024','IP0012','2024-IP0010','2024-05-17','12345','TEST','TEST_ITEM','1','','','','','','','','SQ0000','','2','','','SQ9999','','1','','','3\"DISC-CCW','1','','','','','','','TEST','TEST','PCD10','2','','','PCD12','1','','','','','','','','','','','','','','','TEST','','','','','','1'),('IP000000013','2024-05-17 20:36:40','2024-05-17 20:36:51',NULL,'IT000000022',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,'SP000000017','SH000000001',NULL,NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0013','2024','IP0013','2024-IP0012','2024-05-17','12345','TEST','TEST_ITEM','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0000',NULL,'2',NULL,NULL,'SQ9999','2024-SP0015','1',NULL,NULL,'3\"DISC-CCW','1',NULL,NULL,NULL,NULL,NULL,NULL,'TEST','TEST','PCD10','2',NULL,NULL,'PCD12','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'TEST',NULL,NULL,NULL,NULL,NULL,'1'),('IP000000014','2024-05-18 09:06:22','2024-05-18 09:06:42',NULL,'IT000000023',NULL,NULL,NULL,'SE000000001','SE000000086',NULL,NULL,'SH000000002',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0014','2024','IP0014','2024-IP0011','2024-05-18','235235','TEST','TEST_ITEM2','2','','','','','','','','SQ0000','','2','','','SQ9999','','2','','','3\"DISC-CW','2','','','','','','','TEST','TEST','','','','','','','','','','','','','','','','','','','','','TEST','','MEMO','','','','3'),('IP000000015','2024-05-19 20:25:45','2024-05-19 20:25:45',NULL,'IT000000005',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0015','2024','IP0015',NULL,'2024-05-19','3/5','3\"6Y20','3\"6Y20CW','24',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0090',NULL,'144',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"DISC-SSCW','24',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Y20',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IP000000016','2024-05-19 20:28:09','2024-05-19 20:29:15',NULL,'IT000000005','IT000000004',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0016','2024','IP0016','2024-IP0015','2024-05-19','3/5','3\"6Y20','3\"6Y20CW','24','3\"6Y20CCW','24','','','','','','SQ0090','','288','','','','','','','','3\"DISC-SSCW','24','3\"DISC-SSCCW','24','','','','','','Y20','','','','','','','','','','','','','','','','','','','','','','','','','','','1'),('IP000000017','2024-05-20 17:47:45','2024-05-20 17:47:45',NULL,'IT000000005',NULL,NULL,NULL,'SE000000087',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0017','2024','IP0017','2024-IP0016','2024-05-20','3/5','3\"6Y20','3\"6Y20CW','24',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'SQ0090',NULL,'144',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"DISC-SSCW','24',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Y20',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IP000000018','2024-05-20 17:48:25','2024-06-27 15:49:26',NULL,'IT000000022','IT000000023',NULL,NULL,'SE000000001','SE000000086',NULL,NULL,'SH000000001','SH000000002',NULL,NULL,'SU000000001','SU000000002',NULL,NULL,'2024-IP0018','2024','IP0018','2024-IP0013','2024-05-20','235235','TEST','TEST_ITEM','1','TEST_ITEM2','2','','','','','','SQ0000','','4','','','SQ9999','','3','','','3\"DISC-CCW','1','3\"DISC-CW','2','','','','','TEST','TEST','PCD10','2','','','PCD12','1','','','','','','','','','','','','','','','TEST','','','','','','2');
/*!40000 ALTER TABLE `ip` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_ip_insert` BEFORE INSERT ON `ip` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM ip;
    SET NEW.sys_id = CONCAT('IP', LPAD(next_id, 9, '0'));
    
    SELECT IFNULL(MAX(SUBSTRING(`ip_no2`, 3)) + 1, 1) INTO next_id FROM ip;
    SET NEW.`ip_no2` = CONCAT('IP', LPAD(next_id, 4, '0'));
    SET NEW.`ip_no1` = DATE_FORMAT(NOW(), '%Y');
    SET NEW.`ip_no` = CONCAT(NEW.`ip_no1`,'-', NEW.`ip_no2`);

    SET NEW.`creation_date` = DATE_FORMAT(NOW(), '%Y-%m-%d');
    -- ----------------------------------------------------------------------
	IF NEW.`item1_name` IS NOT NULL THEN
        SET NEW.sys_item1_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item1_name`);
		SET NEW.`ip_no3` = (SELECT recent_ip FROM item WHERE item.product_name = NEW.`item1_name`);        
    END IF;
	IF NEW.`item2_name` IS NOT NULL THEN
        SET NEW.sys_item2_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item2_name`);
    END IF;
	IF NEW.`item3_name` IS NOT NULL THEN
        SET NEW.sys_item3_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item3_name`);
    END IF;
	IF NEW.`item4_name` IS NOT NULL THEN
        SET NEW.sys_item4_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item4_name`);
    END IF;
	IF NEW.`seg1_no` IS NOT NULL THEN
        SET NEW.sys_seg1_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg1_no`);
    END IF;
	IF NEW.`seg2_no` IS NOT NULL THEN
        SET NEW.sys_seg2_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg2_no`);
    END IF; 
	IF NEW.`shank1_name` IS NOT NULL THEN
        SET NEW.sys_shank1_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank1_name`);
    END IF;     
	IF NEW.`shank1_name` IS NOT NULL THEN
        SET NEW.sys_shank1_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank1_name`);
    END IF;     
	IF NEW.`shank2_name` IS NOT NULL THEN
        SET NEW.sys_shank2_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank2_name`);
    END IF;     
	IF NEW.`shank3_name` IS NOT NULL THEN
        SET NEW.sys_shank3_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank3_name`);
    END IF;     
	IF NEW.`shank4_name` IS NOT NULL THEN
        SET NEW.sys_shank4_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank4_name`);
    END IF;         
	IF NEW.`sub1_name` IS NOT NULL THEN
        SET NEW.sys_sub1_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub1_name`);
    END IF;         
	IF NEW.`sub2_name` IS NOT NULL THEN
        SET NEW.sys_sub2_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub2_name`);
    END IF;     
	IF NEW.`sub3_name` IS NOT NULL THEN
        SET NEW.sys_sub3_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub3_name`);
    END IF;     
	IF NEW.`sub4_name` IS NOT NULL THEN
        SET NEW.sys_sub4_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub4_name`);
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `ip_AFTER_INSERT` AFTER INSERT ON `ip` FOR EACH ROW BEGIN
    UPDATE `item`
    SET recent_ip = NEW.ip_no
    WHERE item.product_name = NEW.item1_name 
		OR item.product_name = NEW.item2_name 
        OR item.product_name = NEW.item3_name 
        OR item.product_name = NEW.item4_name;

    UPDATE item_order
    SET ip_no = NEW.ip_no, sys_ip_id = NEW.sys_id
	WHERE item_order.ip_no IS NULL
		AND (
			item_order.item_name = NEW.item1_name 
			OR item_order.item_name = NEW.item2_name 
			OR item_order.item_name = NEW.item3_name 
			OR item_order.item_name = NEW.item4_name
		);
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `ip_BEFORE_UPDATE` BEFORE UPDATE ON `ip` FOR EACH ROW BEGIN
    SET NEW.sys_update_date = CURRENT_TIMESTAMP;
	IF NEW.checked IS NULL OR NEW.checked = '' THEN
		SET NEW.checked = 1;
	ELSE
		SET NEW.checked = NEW.checked + 1;
	END IF;        
	-- ----------------------------------------------------------------------
	IF NEW.`item1_name` IS NOT NULL THEN
        SET NEW.sys_item1_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item1_name`);     
    END IF;
	IF NEW.`item2_name` IS NOT NULL THEN
        SET NEW.sys_item2_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item2_name`);
    END IF;
	IF NEW.`item3_name` IS NOT NULL THEN
        SET NEW.sys_item3_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item3_name`);
    END IF;
	IF NEW.`item4_name` IS NOT NULL THEN
        SET NEW.sys_item4_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item4_name`);
    END IF;
	IF NEW.`seg1_no` IS NOT NULL THEN
        SET NEW.sys_seg1_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg1_no`);
    END IF;
	IF NEW.`seg2_no` IS NOT NULL THEN
        SET NEW.sys_seg2_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg2_no`);
    END IF; 
	IF NEW.`shank1_name` IS NOT NULL THEN
        SET NEW.sys_shank1_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank1_name`);
    END IF;     
	IF NEW.`shank1_name` IS NOT NULL THEN
        SET NEW.sys_shank1_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank1_name`);
    END IF;     
	IF NEW.`shank2_name` IS NOT NULL THEN
        SET NEW.sys_shank2_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank2_name`);
    END IF;     
	IF NEW.`shank3_name` IS NOT NULL THEN
        SET NEW.sys_shank3_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank3_name`);
    END IF;     
	IF NEW.`shank4_name` IS NOT NULL THEN
        SET NEW.sys_shank4_id = (SELECT sys_id FROM shank WHERE shank.product_name = NEW.`shank4_name`);
    END IF;         
	IF NEW.`sub1_name` IS NOT NULL THEN
        SET NEW.sys_sub1_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub1_name`);
    END IF;         
	IF NEW.`sub2_name` IS NOT NULL THEN
        SET NEW.sys_sub2_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub2_name`);
    END IF;     
	IF NEW.`sub3_name` IS NOT NULL THEN
        SET NEW.sys_sub3_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub3_name`);
    END IF;     
	IF NEW.`sub4_name` IS NOT NULL THEN
        SET NEW.sys_sub4_id = (SELECT sys_id FROM submaterial WHERE submaterial.product_name = NEW.`sub4_name`);
    END IF;        

END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `sys_seg1_id` varchar(45) DEFAULT NULL,
  `sys_seg2_id` varchar(45) DEFAULT NULL,
  `sys_shank_id` varchar(45) DEFAULT NULL,
  `sys_sub1_id` varchar(45) DEFAULT NULL,
  `sys_sub2_id` varchar(45) DEFAULT NULL,
  `sys_ip_id` varchar(45) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `group_name` varchar(45) DEFAULT NULL,
  `seg1_no` varchar(45) DEFAULT NULL,
  `seg1_amount` varchar(45) DEFAULT NULL,
  `seg2_no` varchar(45) DEFAULT NULL,
  `seg2_amount` varchar(45) DEFAULT NULL,
  `shank_name` varchar(45) DEFAULT NULL,
  `shank_amount` varchar(45) DEFAULT NULL,
  `sub1_name` varchar(45) DEFAULT NULL,
  `sub1_amount` varchar(45) DEFAULT NULL,
  `sub2_name` varchar(45) DEFAULT NULL,
  `sub2_amount` varchar(45) DEFAULT NULL,
  `mark` varchar(45) DEFAULT NULL,
  `welding` varchar(45) DEFAULT NULL,
  `dressing` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `recent_ip` varchar(45) DEFAULT NULL,
  `image` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES ('IT000000001','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"6OR60CCW','3\"6OR60','SQ0081','6','','','3\"DISC-SSCCW','1','','','','ORANGE','O60',NULL,NULL,NULL,NULL,NULL),('IT000000002','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"6OR60CW','3\"6OR60','SQ0081','6','','','3\"DISC-SSCW','1','','','','ORANGE','O60',NULL,NULL,NULL,NULL,NULL),('IT000000003','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"6OR60T','3\"6OR60','SQ0081','6','','','3\"DISC-T','1','','','','ORANGE','O60',NULL,NULL,NULL,NULL,NULL),('IT000000004','2024-05-07 11:10:37','2024-05-19 20:28:09',NULL,NULL,NULL,NULL,NULL,NULL,'IP000000016','3\"6Y20CCW','3\"6Y20','SQ0090','6','','','3\"DISC-SSCCW','1','','','','YELLOW','Y20',NULL,NULL,NULL,'2024-IP0016',NULL),('IT000000005','2024-05-07 11:10:37','2024-05-20 17:47:45',NULL,'SE000000087',NULL,NULL,NULL,NULL,'IP000000017','3\"6Y20CW','3\"6Y20','SQ0090','6','','','3\"DISC-SSCW','1','','','','YELLOW','Y20',NULL,NULL,NULL,'2024-IP0017',NULL),('IT000000006','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'3\"6Y20T','3\"6Y20','SQ0090','6','','','3\"DISC-T','1','','','','YELLOW','Y20',NULL,NULL,NULL,NULL,NULL),('IT000000007','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000005',NULL,NULL,'3\"PCD CCW','3\"PCD','SQ0020','2','','','3\"PCD SSCCW','1','PCD8','','','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000008','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000005',NULL,NULL,'3\"PCD CW','3\"PCD','SQ0020','2','','','3\"PCD SSCW','1','PCD8','','','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000009','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000005',NULL,NULL,'3\"PCD TCCW','3\"PCD','SQ0020','2','','','3\"PCD TCCW ','1','PCD8','','','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000010','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000005',NULL,NULL,'3\"PCD TCW','3\"PCD','SQ0020','2','','','3\"PCD TCW','1','PCD8','','','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000011','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'5\"CUPB OVAL60','5\"CUPB OVAL60','SQ0082','5','','','5\"CUP-B22.23H','1','RING7/8-5/8','','','ORANGE',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000012','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'5\"CUPT-OVAL60','5\"CUPT-OVAL60','SQ0082','5','','','5\"CUP-5/8-11T','1','','','','ORANGE',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000013','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'7\"CUPB OVAL60','7\"CUPB OVAL60','SQ0082','8','','','7\"CUP-B22.23H','1','RING7/8-5/8','','','ORANGE',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000014','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'7\"CUPT-OVAL60','7\"CUPT-OVAL60','SQ0082','8','','','7\"CUP-5/8-11T','1','','','','ORANGE',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000015','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NOSECONE 120','NOSECONE 120','SQ0117','4','','','CONE5/8-11T','1','','','','YELLOW',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000016','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NOSECONE 20','NOSECONE 20','SQ0116','4','','','CONE5/8-11T','1','','','','YELLOW',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000017','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NOSECONE 40','NOSECONE 40','SQ0104','4','','','CONE5/8-11T','1','','','','YELLOW',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000018','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NOSECONE 80','NOSECONE 80','SQ0083','4','','','CONE5/8-11T','1','','','','YELLOW',NULL,NULL,NULL,NULL,NULL,NULL),('IT000000019','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000002',NULL,NULL,'RZ948 S30 CCW','RZ948 S30','SQ0141','3','SQ0045','3','RX948-CCW','1','PCD12','POST12','3','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000020','2024-05-07 11:10:37','2024-05-07 11:10:37',NULL,NULL,NULL,NULL,'SU000000002',NULL,NULL,'RZ948 S30 CW','RZ948 S30','SQ0141','3','SQ0045','3','RX948-CW','1','PCD12','POST12','3','SILVER','',NULL,NULL,NULL,NULL,NULL),('IT000000021','2024-05-07 11:33:44','2024-05-07 11:33:44',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IT000000022','2024-05-07 11:35:52','2024-05-20 17:48:25',NULL,'SE000000001','SE000000086','SH000000001','SU000000001','SU000000002','IP000000018','TEST_ITEM','TEST','SQ0000','2','SQ9999','1','3\"DISC-CCW','1','PCD10','2','PCD12','1','TEST',NULL,NULL,'TEST','2024-IP0018','TEST'),('IT000000023','2024-05-07 11:42:59','2024-05-20 17:48:25',NULL,'SE000000001','SE000000086','SH000000002',NULL,NULL,'IP000000018','TEST_ITEM2','TEST','SQ0000','1','SQ9999','1','3\"DISC-CW','1',NULL,NULL,NULL,NULL,'TEST',NULL,NULL,'TEST','2024-IP0018','TEST'),('IT000000024','2024-05-08 11:32:18','2024-05-08 11:32:18',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('IT000000025','2024-05-08 11:34:43','2024-05-08 11:34:43',NULL,NULL,NULL,NULL,NULL,NULL,'IP000000008',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0005',NULL),('IT000000026','2024-05-08 11:34:45','2024-05-08 11:34:45',NULL,NULL,NULL,NULL,NULL,NULL,'IP000000009',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0006',NULL),('IT000000027','2024-05-20 17:24:58','2024-05-20 17:24:58',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_item_insert` BEFORE INSERT ON `item` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM item;
    SET NEW.sys_id = CONCAT('IT', LPAD(next_id, 9, '0'));
    -- ----------------------------------------------------------------------
	IF NEW.`seg1_no` IS NOT NULL THEN
        SET NEW.sys_seg1_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg1_no`);
    END IF;
    
	IF NEW.`seg2_no` IS NOT NULL THEN
        SET NEW.sys_seg2_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg2_no`);
    END IF;
    
	IF NEW.`shank_name` IS NOT NULL THEN
        SET NEW.sys_shank_id = (SELECT sys_id FROM shank WHERE shank.`product_name` = NEW.`shank_name`);
    END IF;    

	IF NEW.`sub1_name` IS NOT NULL THEN
        SET NEW.sys_sub1_id = (SELECT sys_id FROM submaterial WHERE submaterial.`product_name` = NEW.`sub1_name`);
    END IF;    
    
	IF NEW.`sub2_name` IS NOT NULL THEN
        SET NEW.sys_sub2_id = (SELECT sys_id FROM submaterial WHERE submaterial.`product_name` = NEW.`sub2_name`);
    END IF;    
    
	IF NEW.`recent_ip` IS NOT NULL THEN
        SET NEW.sys_ip_id = (SELECT sys_id FROM ip WHERE ip.`ip_no` = NEW.`recent_ip`);
    END IF;        
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `item_BEFORE_UPDATE` BEFORE UPDATE ON `item` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
	IF NEW.`seg1_no` IS NOT NULL THEN
        SET NEW.sys_seg1_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg1_no`);
    END IF;
    
	IF NEW.`seg2_no` IS NOT NULL THEN
        SET NEW.sys_seg2_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg2_no`);
    END IF;
    
	IF NEW.`shank_name` IS NOT NULL THEN
        SET NEW.sys_shank_id = (SELECT sys_id FROM shank WHERE shank.`product_name` = NEW.`shank_name`);
    END IF;    

	IF NEW.`sub1_name` IS NOT NULL THEN
        SET NEW.sys_sub1_id = (SELECT sys_id FROM submaterial WHERE submaterial.`product_name` = NEW.`sub1_name`);
    END IF;    
    
	IF NEW.`sub2_name` IS NOT NULL THEN
        SET NEW.sys_sub2_id = (SELECT sys_id FROM submaterial WHERE submaterial.`product_name` = NEW.`sub2_name`);
    END IF;    
    
	IF NEW.`recent_ip` IS NOT NULL THEN
        SET NEW.sys_ip_id = (SELECT sys_id FROM ip WHERE ip.`ip_no` = NEW.`recent_ip`);
    END IF;        
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `item_order`
--

DROP TABLE IF EXISTS `item_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item_order` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `sys_customer_id` varchar(45) DEFAULT NULL,
  `sys_item_id` varchar(45) DEFAULT NULL,
  `sys_ip_id` varchar(45) DEFAULT NULL,
  `sys_sp_id` varchar(45) DEFAULT NULL,
  `sys_seg_id` varchar(45) DEFAULT NULL,
  `sys_bond_id` varchar(45) DEFAULT NULL,
  `customer_name` varchar(45) DEFAULT NULL,
  `order_date` varchar(45) DEFAULT NULL,
  `order_no` varchar(45) DEFAULT NULL,
  `order_customer_no` varchar(45) DEFAULT NULL,
  `order_item_no` varchar(45) DEFAULT NULL,
  `item_group_name` varchar(45) DEFAULT NULL,
  `item_name` varchar(45) DEFAULT NULL,
  `item_amount` varchar(45) DEFAULT NULL,
  `engrave` varchar(45) DEFAULT NULL,
  `ip_no` varchar(45) DEFAULT NULL,
  `sp_no` varchar(45) DEFAULT NULL,
  `seg_no` varchar(45) DEFAULT NULL,
  `seg_name` varchar(45) DEFAULT NULL,
  `bond_name` varchar(45) DEFAULT NULL,
  `seg_amount_net` varchar(45) DEFAULT NULL,
  `seg_amount_work` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `due_date` varchar(45) DEFAULT NULL,
  `shipping_date` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item_order`
--

LOCK TABLES `item_order` WRITE;
/*!40000 ALTER TABLE `item_order` DISABLE KEYS */;
INSERT INTO `item_order` VALUES ('IO000000001','2024-05-07 11:46:05','2024-05-20 21:13:29',NULL,NULL,'IT000000022','IP000000018','SP000000031',NULL,NULL,'coustomer1','TEST','1','c1-1','1','TEST','TEST_ITEM','1','TEST','2024-IP0018','2024-SP0029','TEST','TEST','TEST','TEST','TEST','TEST','12345',NULL),('IO000000002','2024-05-07 11:46:48','2024-05-20 21:13:29',NULL,NULL,'IT000000023','IP000000018','SP000000031',NULL,NULL,'coustomer1','TEST','1','c1-1','2','TEST','TEST_ITEM2','2','TEST','2024-IP0018','2024-SP0029','TEST','TEST','TEST','TEST','TEST','TEST','235235',NULL),('IO000000003','2024-06-27 11:14:27','2024-06-27 11:14:27',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'r','1',NULL,NULL,NULL,NULL,'r','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `item_order` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_item_order_insert` BEFORE INSERT ON `item_order` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    DECLARE v_sys_id VARCHAR(11);
    DECLARE v_customer_id VARCHAR(45);
    DECLARE max_no INT DEFAULT 0;
    DECLARE new_no VARCHAR(10);
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM item_order;
    SET NEW.sys_id = CONCAT('IO', LPAD(next_id, 9, '0'));
    -- ----------------------------------------------------------------------
	IF NEW.`customer_name` IS NOT NULL THEN
    
		SELECT sys_id, customer_id INTO v_sys_id, v_customer_id
        FROM customer
        WHERE customer_name = NEW.customer_name
        LIMIT 1;
    
		SELECT IFNULL(MAX(CAST(SUBSTRING(order_customer_no, LENGTH(v_customer_id) + 1) AS UNSIGNED)), 0)
        INTO max_no
        FROM item_order
        WHERE order_customer_no LIKE CONCAT(v_customer_id, '%');
    
        SET NEW.sys_customer_id = v_sys_id;
        SET new_no = LPAD(max_no + 1, 3, '0');
        SET NEW.order_customer_no = CONCAT(v_customer_id, new_no);
    END IF;
	IF NEW.`item_name` IS NOT NULL THEN
        SET NEW.sys_item_id = (SELECT sys_id FROM item WHERE item.product_name = NEW.`item_name`);
    END IF;
	IF NEW.`seg_no` IS NOT NULL THEN
        SET NEW.sys_seg_id = (SELECT sys_id FROM segment WHERE segment.`seg_no` = NEW.`seg_no`);
        SET NEW.seg_name = (SELECT product_name FROM segment WHERE segment.`seg_no` = NEW.`seg_no`);
    END IF;
	IF NEW.`bond_name` IS NOT NULL THEN
        SET NEW.sys_bond_id = (SELECT sys_id FROM bond WHERE bond.product_name = NEW.`bond_name`);
    END IF;    
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `item_order_BEFORE_UPDATE` BEFORE UPDATE ON `item_order` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `powder`
--

DROP TABLE IF EXISTS `powder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `powder` (
  `sys_id` varchar(11) NOT NULL COMMENT '자동생성(PO + 9자리 숫자)',
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `chemical_symbol` varchar(45) DEFAULT NULL,
  `product_name_en` varchar(45) DEFAULT NULL,
  `product_name_ko` varchar(45) DEFAULT NULL,
  `specification` varchar(45) DEFAULT NULL,
  `density` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `inventory` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `powder`
--

LOCK TABLES `powder` WRITE;
/*!40000 ALTER TABLE `powder` DISABLE KEYS */;
INSERT INTO `powder` VALUES ('PO000000002','2024-05-04 13:37:54','2024-05-17 10:11:46','1','Co','Carbond','탄소',NULL,'2.267','50',NULL),('PO000000004','2024-05-04 13:37:54','2024-05-17 10:11:46','2','Cu#300','Copper','구리','#300','8.96','20',NULL),('PO000000005','2024-05-04 13:37:54','2024-05-17 10:11:46','3','Cu#600','Copper','구리','#600','8.96','20',NULL),('PO000000006','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'CuSn#67','Bronze','청동','#67','8.7','38',NULL),('PO000000007','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'CuSn#80','Bronze','청동','#80','8.8','38',NULL),('PO000000008','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'Fe','Iron','철','5~7 µm','7.87','4.5',NULL),('PO000000009','2024-05-04 13:37:54','2024-05-17 10:11:46','6','Ni','Nickel','니켈','#400 2~8µm','8.9','34',NULL),('PO000000010','2024-05-04 13:37:54','2024-05-17 10:11:46','7','P₂O₅','Phosphorus','적인',NULL,NULL,NULL,NULL),('PO000000011','2024-05-04 13:37:54','2024-05-17 10:11:46','8','S','Sulfur','황',NULL,NULL,NULL,NULL),('PO000000012','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'Sn#300','Tin','주석','#300','7.28','60.5',NULL),('PO000000013','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'Sn#600','Tin','주석','#600','7.28','60.5',NULL),('PO000000014','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'W','Tugsten','텅스텐','0.8µm','19.3','85',NULL),('PO000000015','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'WC','Tugsten Carbide','초경','6~8µm','15.3','85',NULL),('PO000000016','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'W₂C','Ditungten Carbide','초경','100/200','16.06','85',NULL),('PO000000017','2024-05-04 13:37:54','2024-05-17 10:11:46',NULL,'Zn','Zinc Stearate','아연',NULL,NULL,NULL,NULL),('PO000000018','2024-05-20 17:13:12','2024-05-20 17:13:12',NULL,'P2AP','PPAP','펜펜','1321','7.2','13','2');
/*!40000 ALTER TABLE `powder` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_powder_insert` BEFORE INSERT ON `powder` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM powder;
    SET NEW.sys_id = CONCAT('PO', LPAD(next_id, 9, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `powder_BEFORE_UPDATE` BEFORE UPDATE ON `powder` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `segment`
--

DROP TABLE IF EXISTS `segment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `segment` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `sys_bond_id` varchar(45) DEFAULT NULL,
  `sys_dia1_id` varchar(45) DEFAULT NULL,
  `sys_dia2_id` varchar(45) DEFAULT NULL,
  `sys_dia3_id` varchar(45) DEFAULT NULL,
  `seg_no` varchar(45) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  `specification_l` varchar(45) DEFAULT NULL,
  `specification_t` varchar(45) DEFAULT NULL,
  `specification_w` varchar(45) DEFAULT NULL,
  `specification_v` varchar(45) DEFAULT NULL,
  `bond_name` varchar(45) DEFAULT NULL,
  `concent` varchar(45) DEFAULT NULL,
  `specification` varchar(45) DEFAULT NULL,
  `model_text` varchar(45) DEFAULT NULL,
  `model_img` varchar(45) DEFAULT NULL,
  `forming_pressure` varchar(45) DEFAULT NULL,
  `forming_height` varchar(45) DEFAULT NULL,
  `dia1` varchar(45) DEFAULT NULL,
  `dia1_ratio` varchar(45) DEFAULT NULL,
  `dia2` varchar(45) DEFAULT NULL,
  `dia2_ratio` varchar(45) DEFAULT NULL,
  `dia3` varchar(45) DEFAULT NULL,
  `dia3_ratio` varchar(45) DEFAULT NULL,
  `recent_sp` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `segment`
--

LOCK TABLES `segment` WRITE;
/*!40000 ALTER TABLE `segment` DISABLE KEYS */;
INSERT INTO `segment` VALUES ('SE000000001','2024-05-07 11:04:10','2024-05-20 20:13:35','TEST COLOR','BO000000008','DI000000009','DI000000014','DI000000005','SQ0000','TEST SEG T0','ALIAS','11','22','33','4','Q701','1',NULL,'TEST MODEL',NULL,NULL,NULL,'2040 #40/50','5','2040 #80/100','3','2040 #140/170','2','2024-SP0004'),('SE000000002','2024-05-07 11:04:10','2024-05-20 20:13:35','SILVER','BO000000008',NULL,NULL,NULL,'SQ0001','WEAR SEGMENT',NULL,'20','20','8',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000003','2024-05-07 11:04:10','2024-05-20 20:13:36','BROWN','BO000000009',NULL,NULL,NULL,'SQ0002','SMALL FAN - NP23','부채꼴 小 NP23','36','30','10',NULL,'Q702','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000004','2024-05-07 11:04:10','2024-05-20 20:13:36','BLACK','BO000000009',NULL,NULL,NULL,'SQ0003','SMALL FAN - NP25','부채꼴 小 NP25','36','30','10',NULL,'Q702','1.440000057',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000005','2024-05-07 11:04:10','2024-05-20 20:13:36','GOLD','BO000000010',NULL,NULL,NULL,'SQ0004','SPLIT CHAMFER - FRONT - G30','챔퍼 앞 G30','24.89999962','8','10',NULL,'Q703','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000006','2024-05-07 11:04:10','2024-05-20 20:13:36','GOLD','BO000000010',NULL,NULL,NULL,'SQ0005','SPLIT CHAMFER - REAR - G30','챔퍼 뒤 G30','10','8','10',NULL,'Q703','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000007','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0006','CHAMFER-R','챔퍼 R30','32','8','10',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000008','2024-05-07 11:04:10','2024-05-20 20:13:36','GOLD','BO000000010',NULL,NULL,NULL,'SQ0007','CHAMFER-G','챔퍼 G30','32','8','10',NULL,'Q703','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000009','2024-05-07 11:04:10','2024-05-20 20:13:36','SILVER','BO000000008',NULL,NULL,NULL,'SQ0008','SPLIT CHAMFER - FRONT - S','챔퍼 앞 S30','24.89999962','8','10',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000010','2024-05-07 11:04:10','2024-05-20 20:13:36','SILVER','BO000000008',NULL,NULL,NULL,'SQ0009','SPLIT CHAMFER - REAR - S','챔퍼 뒤 S30','10','8','10',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000011','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0010','BIG FAN R40','부채꼴 大 R40','42.5','43.5','12',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000012','2024-05-07 11:04:10','2024-05-20 20:13:36','BLUE','BO000000007',NULL,NULL,NULL,'SQ0011','BIG FAN BLU30','부채꼴 大 BLU30','42.5','43.5','12',NULL,'Q502','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000013','2024-05-07 11:04:10','2024-05-20 20:13:36','BLUE','BO000000007',NULL,NULL,NULL,'SQ0012','BIG FAN B150','부채꼴 大 B150','42.5','43.5','12',NULL,'Q502','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #140/170','10',NULL,NULL,NULL,NULL,NULL),('SE000000014','2024-05-07 11:04:10','2024-05-20 20:13:36','BLUE','BO000000007',NULL,NULL,NULL,'SQ0013','MID FAN BLU30','부채꼴 中 BLU30','42','31.60000038','10',NULL,'Q502','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000015','2024-05-07 11:04:10','2024-05-20 20:13:36','SILVER','BO000000008',NULL,NULL,NULL,'SQ0014','CHAMFER-S','챔퍼 S30','32','8','10',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000016','2024-05-07 11:04:10','2024-05-20 20:13:36','YELLOW','BO000000001',NULL,NULL,NULL,'SQ0015','MID FAN Y40','부채꼴 中 Y40','42','31.60000038','10',NULL,'Q301','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000017','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0016','BIG FAN R30',NULL,'42.5','43.5','12',NULL,'Q501','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000018','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0017','CHANNEL R40',NULL,'42','45','12',NULL,'Q501','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000019','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0018','SPLIT CHAMFER - FRONT - R',NULL,'24.89999962','8','10',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000020','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0019','SPLIT CHAMFER - REAR - R',NULL,'10','8','10',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000021','2024-05-07 11:04:10','2024-05-20 20:13:36','HRAD',NULL,NULL,NULL,NULL,'SQ0020','OVAL-WEAR',NULL,'30','17','5.5',NULL,'TOP','1.539999962',NULL,NULL,NULL,NULL,NULL,'#150','10',NULL,NULL,NULL,NULL,NULL),('SE000000022','2024-05-07 11:04:10','2024-05-20 20:13:36','YELLOW','BO000000001',NULL,NULL,NULL,'SQ0021','MID FAN Y60',NULL,'42','31.60000038','10','6.8','Q301','1',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000023','2024-05-07 11:04:10','2024-05-20 20:13:36','YELLOW','BO000000001',NULL,NULL,NULL,'SQ0022','MID FAN Y150',NULL,'42','31.60000038','10',NULL,'Q301','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #140/170','10',NULL,NULL,NULL,NULL,NULL),('SE000000024','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0023','RADIUS32 R32-R40',NULL,'32','37','5',NULL,'Q501','1',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000025','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0024','SLANT35L SL35-R40',NULL,'35','8','8',NULL,'Q501','1',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000026','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0025','TURBO T-R40',NULL,'32.5','20','8',NULL,'Q501','1',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000027','2024-05-07 11:04:10','2024-05-20 20:13:36','BLUE','BO000000007',NULL,NULL,NULL,'SQ0026','BIG FAN BLU60',NULL,'42.5','43.5','12',NULL,'Q502','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000028','2024-05-07 11:04:10','2024-05-20 20:13:36','BLUE','BO000000007',NULL,NULL,NULL,'SQ0027','BIG FAN BLU120',NULL,'42.5','43.5','12',NULL,'Q502','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #120/140','10',NULL,NULL,NULL,NULL,NULL),('SE000000029','2024-05-07 11:04:10','2024-05-20 20:13:36','RED','BO000000006',NULL,NULL,NULL,'SQ0028','BIG FAN R60',NULL,'42.5','43.5','12',NULL,'Q501','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000030','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0029','BIG FAN R120',NULL,'42.5','43.5','12',NULL,'Q501','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #120/140','10',NULL,NULL,NULL,NULL,NULL),('SE000000031','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0030','BIG FAN R16',NULL,'42.5','43.5','12',NULL,'Q501','1.700000048',NULL,NULL,NULL,NULL,NULL,'2060 #16/18','8.5','2050 40/50','1.5',NULL,NULL,NULL),('SE000000032','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0031','CUPSEG40 R40',NULL,'40.5','6','8',NULL,'Q501','0.699999988',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000033','2024-05-07 11:04:10','2024-05-20 20:13:37','JOEN','BO000000002',NULL,NULL,NULL,'SQ0032','CUPSEG40 A40',NULL,'40.5','6','4.5',NULL,'Q302','0.699999988',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000034','2024-05-07 11:04:10','2024-05-20 20:13:37','HUSQ-G620','BO000000002',NULL,NULL,NULL,'SQ0033','ROUND23 A60',NULL,'23','23','10.5',NULL,'Q302','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000035','2024-05-07 11:04:10','2024-05-20 20:13:37','HUSQ-G620','BO000000002',NULL,NULL,NULL,'SQ0034','ROUND23 A100',NULL,'23','23','10.5',NULL,'Q302','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #100/120','10',NULL,NULL,NULL,NULL,NULL),('SE000000036','2024-05-07 11:04:10','2024-05-20 20:13:37','NP23','BO000000009',NULL,NULL,NULL,'SQ0035','OVAL BRW60',NULL,'30','17','10',NULL,'Q702','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000037','2024-05-07 11:04:10','2024-05-20 20:13:37','NP23','BO000000009',NULL,NULL,NULL,'SQ0036','TURBO BRW40',NULL,'32.5','20','8',NULL,'Q702','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 #30/40TI','10',NULL,NULL,NULL,NULL,NULL),('SE000000038','2024-05-07 11:04:10','2024-05-20 20:13:37','HUSG1120','BO000000002',NULL,NULL,NULL,'SQ0037','RECT-J20',NULL,'40','10','10',NULL,'Q302','1.320000052',NULL,NULL,NULL,NULL,NULL,'360 #20/30','10',NULL,NULL,NULL,NULL,NULL),('SE000000039','2024-05-07 11:04:10','2024-05-20 20:13:37','HUSQ-G620','BO000000002',NULL,NULL,NULL,'SQ0038','ROUND23 A50',NULL,'23','23','10.5',NULL,'Q302','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #50/60','10',NULL,NULL,NULL,NULL,NULL),('SE000000040','2024-05-07 11:04:10','2024-05-20 20:13:37','BLUE','BO000000002',NULL,NULL,NULL,'SQ0039','TURBO A30',NULL,'32.5','20','8',NULL,'Q302','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000041','2024-05-07 11:04:10','2024-05-20 20:13:37','BLUE','BO000000002',NULL,NULL,NULL,'SQ0040','OVAL A40',NULL,'30','17','10',NULL,'Q302','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000042','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000002',NULL,NULL,NULL,'SQ0041','TURBO R30',NULL,'32.5','20','8',NULL,'Q302','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000043','2024-05-07 11:04:10','2024-05-20 20:13:37','BLACK',NULL,NULL,NULL,NULL,'SQ0042','CHAMFER-BK',NULL,'32','8','10',NULL,'Q705','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000044','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0043','BIG FAN R150',NULL,'42.5','43.5','12',NULL,'Q501','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #150','10',NULL,NULL,NULL,NULL,NULL),('SE000000045','2024-05-07 11:04:10','2024-05-20 20:13:37','SILVER','BO000000008',NULL,NULL,NULL,'SQ0044','RX-CHAMFER-S30',NULL,'32','8','12',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000046','2024-05-07 11:04:10','2024-05-20 20:13:37','SILVER','BO000000008',NULL,NULL,NULL,'SQ0045','RX-REAR-S30',NULL,'15','14','11',NULL,'Q701','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000047','2024-05-07 11:04:10','2024-05-20 20:13:37',NULL,NULL,NULL,NULL,NULL,'SQ0046','LX-SDS L',NULL,'72.80000305','17','10',NULL,'J501','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000048','2024-05-07 11:04:10','2024-05-20 20:13:37',NULL,NULL,NULL,NULL,NULL,'SQ0047','LX-SDS LAS',NULL,'72.80000305','17','10',NULL,'J502','1.600000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000049','2024-05-07 11:04:10','2024-05-20 20:13:37','YELLOW','BO000000001',NULL,NULL,NULL,'SQ0048','MID FAN Y80',NULL,'42','31.60000038','10',NULL,'Q301','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000050','2024-05-07 11:04:10','2024-05-20 20:13:37','BLACK',NULL,NULL,NULL,NULL,'SQ0049','RX-CHAMFER-BK30',NULL,'32','8','12',NULL,'Q705','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000051','2024-05-07 11:04:10','2024-05-20 20:13:37','BLACK',NULL,NULL,NULL,NULL,'SQ0050','RX-REAR-BK30',NULL,'15','14','11',NULL,'Q705','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000052','2024-05-07 11:04:10','2024-05-20 20:13:37',NULL,'BO000000006',NULL,NULL,NULL,'SQ0051','LX-SDS R40',NULL,'72.80000305','17','10',NULL,'Q501','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000053','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0052','RX-CHAMFER-R30',NULL,'32','8','12',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000054','2024-05-07 11:04:10','2024-05-20 20:13:37','RED','BO000000006',NULL,NULL,NULL,'SQ0053','RX-REAR-R30',NULL,'15','14','11',NULL,'Q501','1.320000052',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000055','2024-05-07 11:04:10','2024-05-20 20:13:37',NULL,'BO000000006',NULL,NULL,NULL,'SQ0054','RECT-MH40',NULL,'40','10','10',NULL,'Q501','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000056','2024-05-07 11:04:10','2024-05-20 20:13:37',NULL,'BO000000001',NULL,NULL,NULL,'SQ0055','RECT-SM40',NULL,'40','10','10',NULL,'Q301','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000057','2024-05-07 11:04:10','2024-05-20 20:13:37','WHITE','BO000000003',NULL,NULL,NULL,'SQ0056','HALF FAN W40',NULL,'30','19.60000038','10','3','Q303','1',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000058','2024-05-07 11:04:10','2024-05-20 20:13:38','BLACK','BO000000009',NULL,NULL,NULL,'SQ0057','SMALL FAN - NP25-80',NULL,'36','30','10',NULL,'Q702','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000059','2024-05-07 11:04:10','2024-05-20 20:13:38','WHITE','BO000000003',NULL,NULL,NULL,'SQ0058','HALF FAN W150',NULL,'30','19.60000038','10',NULL,'Q303','0.75',NULL,NULL,NULL,NULL,NULL,'2030 #140/170','10',NULL,NULL,NULL,NULL,NULL),('SE000000060','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0059','MID FAN W80',NULL,'42','31.60000038','10',NULL,'Q303','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000061','2024-05-07 11:04:10','2024-05-20 20:13:38','RED','BO000000006',NULL,NULL,NULL,'SQ0060','BIG FAN R40',NULL,'42.5','43.5','12',NULL,'Q501','1.100000024',NULL,NULL,NULL,NULL,NULL,'2050 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000062','2024-05-07 11:04:10','2024-05-20 20:13:38','BLACK','BO000000009',NULL,NULL,NULL,'SQ0061','SMALL FAN - NP25-30',NULL,'36','30','10',NULL,'Q702','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000063','2024-05-07 11:04:10','2024-05-20 20:13:38',NULL,'BO000000003','DI000000009',NULL,NULL,'SQ0062','RECT-50L-W40',NULL,'50','8','7',NULL,'Q303','1.100000024',NULL,NULL,NULL,NULL,NULL,'2040 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000064','2024-05-07 11:04:10','2024-05-20 20:13:38',NULL,'BO000000003',NULL,NULL,NULL,'SQ0063','RECT-50L-W80',NULL,'50','8','7',NULL,'Q303','0.75',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000065','2024-05-07 11:04:10','2024-05-20 20:13:38','WHITE','BO000000003',NULL,NULL,NULL,'SQ0064','HALF FAN W16',NULL,'30','19.60000038','10',NULL,'Q303','1.539999962',NULL,NULL,NULL,NULL,NULL,'2040 #16/18','10',NULL,NULL,NULL,NULL,NULL),('SE000000066','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0065','MID FAN W60',NULL,'42','31.60000038','10',NULL,'Q303','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000067','2024-05-07 11:04:10','2024-05-20 20:13:38','PINK-황동','BO000000005',NULL,NULL,NULL,'SQ0066','SMALL FAN - P150',NULL,'36','30','10',NULL,'Q305','0.75',NULL,NULL,NULL,NULL,NULL,'2030 #140/160','10',NULL,NULL,NULL,NULL,NULL),('SE000000068','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003','DI000000009',NULL,NULL,'SQ0067','MID FAN W40',NULL,'42','31.60000038','10',NULL,'Q303','1',NULL,NULL,NULL,NULL,NULL,'2040 #40/50','10',NULL,NULL,NULL,NULL,NULL),('SE000000069','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0068','BIG FAN W60',NULL,'42.5','43.5','12',NULL,'Q303','0.850000024',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000070','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0069','BIG FAN W16',NULL,'42.5','43.5','12','10.3','Q303','1.65',NULL,NULL,NULL,NULL,NULL,'2040 #16/18','8','2040 40/50','2',NULL,NULL,NULL),('SE000000071','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0070','CHANNEL Y30',NULL,'42','45','12',NULL,'Q303','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000072','2024-05-07 11:04:10','2024-05-20 20:13:38','RED','BO000000006',NULL,NULL,NULL,'SQ0071','CHANNEL R30',NULL,'42','45','12',NULL,'Q501','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000073','2024-05-07 11:04:10','2024-05-20 20:13:38','BLUE','BO000000007',NULL,NULL,NULL,'SQ0072','CHANNEL BLU30',NULL,'42','45','12',NULL,'Q502','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti 30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000074','2024-05-07 11:04:10','2024-05-20 20:13:38','BLUE','BO000000007',NULL,NULL,NULL,'SQ0073','CHANNEL BLU60',NULL,'42','45','12',NULL,'Q502','0.850000024',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000075','2024-05-07 11:04:10','2024-05-20 20:13:38','BLUE','BO000000007',NULL,NULL,NULL,'SQ0074','CHANNEL BLU150',NULL,'42','45','12',NULL,'Q502','0.75',NULL,NULL,NULL,NULL,NULL,'2030 #140/160','10',NULL,NULL,NULL,NULL,NULL),('SE000000076','2024-05-07 11:04:10','2024-05-20 20:13:38','WHITE','BO000000003',NULL,NULL,NULL,'SQ0075','HALF FAN W60',NULL,'30','19.60000038','10',NULL,'Q303','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000077','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0077','BIG FAN OR30',NULL,'42.5','43.5','12',NULL,'Q305','1.539999962',NULL,NULL,NULL,NULL,NULL,'2050 Ti30/40','10',NULL,NULL,NULL,NULL,NULL),('SE000000078','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0078','BIG FAN OR60',NULL,'42.5','43.5','12',NULL,'Q305','0.899999976',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000079','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0079','BIG FAN OR150',NULL,'42.5','43.5','12',NULL,'Q305','0.75',NULL,NULL,NULL,NULL,NULL,'2030 #140/160','10',NULL,NULL,NULL,NULL,NULL),('SE000000080','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0080','BIG FAN OR80',NULL,'42.5','43.5','12',NULL,'Q305','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000081','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0081','HALF FAN OR60',NULL,'30','19.60000038','10',NULL,'Q305','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000082','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000005',NULL,NULL,NULL,'SQ0082','OVAL OR60',NULL,'30','17','10',NULL,'Q305','0.699999988',NULL,NULL,NULL,NULL,NULL,'2030 #60/80','10',NULL,NULL,NULL,NULL,NULL),('SE000000083','2024-05-07 11:04:10','2024-05-20 20:13:38','ORANGE','BO000000003',NULL,NULL,NULL,'SQ0083','CONE Y80',NULL,'46','26.79999924','4',NULL,'Q303','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000084','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000006',NULL,NULL,NULL,'SQ0085','RADIUS32 R32-Y80',NULL,'32','37','5',NULL,'Q501','0.800000012',NULL,NULL,NULL,NULL,NULL,'2030 #80/100','10',NULL,NULL,NULL,NULL,NULL),('SE000000085','2024-05-07 11:04:10','2024-05-20 20:13:38','YELLOW','BO000000003',NULL,NULL,NULL,'SQ0092','SMALL FAN Y150',NULL,'36','30','10','5.27','Q303','0.7',NULL,NULL,NULL,NULL,NULL,'2030 #140/160','10',NULL,NULL,NULL,NULL,NULL),('SE000000086','2024-05-07 11:14:55','2024-05-20 21:13:29',NULL,'BO000000001','DI000000003','DI000000007','DI000000011','SQ9999','test_seg','TEST','99','99','99','99','Q301','99',NULL,'TEST_TXT','TEST_IMG','99','99','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','2024-SP0029'),('SE000000087','2024-05-19 20:36:31','2024-05-20 20:13:39',NULL,'BO000000003','DI000000006',NULL,NULL,'SQ0090','H-FANW20(Y20)','H-FAN','30','4/19.6','10','3','Q303','1.35',NULL,'부채꼴 1/2',NULL,'760',NULL,'2040 #20/30','10',NULL,NULL,NULL,NULL,NULL),('SE000000088','2024-05-20 17:17:47','2024-05-20 20:13:39',NULL,'BO000000006','DI000000010','DI000000010','DI000000010','SQ0002','DDDOD','3DOD','13','23','132','123','Q501','1.32','SF-TE','SF23F',NULL,'123','132','2040 #50/60','1','2040 #50/60','3','2040 #50/60','2',NULL);
/*!40000 ALTER TABLE `segment` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_segment_insert` BEFORE INSERT ON `segment` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM segment;
    SET NEW.sys_id = CONCAT('SE', LPAD(next_id, 9, '0'));
    -- ----------------------------------------------------------------------
	IF NEW.`bond_name` IS NOT NULL THEN
        SET NEW.sys_bond_id = (SELECT sys_id FROM bond WHERE bond.product_name = NEW.bond_name);
    END IF;          
    
	IF NEW.`dia1` IS NOT NULL THEN
        SET NEW.sys_dia1_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia1);
    END IF;      
    
	IF NEW.`dia2` IS NOT NULL THEN
        SET NEW.sys_dia2_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia2);
    END IF;  
    
	IF NEW.`dia3` IS NOT NULL THEN
        SET NEW.sys_dia3_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia3);
    END IF;        
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `segment_BEFORE_UPDATE` BEFORE UPDATE ON `segment` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
	IF NEW.`bond_name` IS NOT NULL THEN
        SET NEW.sys_bond_id = (SELECT sys_id FROM bond WHERE bond.product_name = NEW.bond_name);
    END IF;          
    
	IF NEW.`dia1` IS NOT NULL THEN
        SET NEW.sys_dia1_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia1);
    END IF;      
    
	IF NEW.`dia2` IS NOT NULL THEN
        SET NEW.sys_dia2_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia2);
    END IF;  
    
	IF NEW.`dia3` IS NOT NULL THEN
        SET NEW.sys_dia3_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.dia3);
    END IF;      
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `shank`
--

DROP TABLE IF EXISTS `shank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shank` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `specification` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shank`
--

LOCK TABLES `shank` WRITE;
/*!40000 ALTER TABLE `shank` DISABLE KEYS */;
INSERT INTO `shank` VALUES ('SH000000001','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"DISC-CCW','5000','D78mm x 10T x Short TAB x CCW'),('SH000000002','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"DISC-CW','5000','D78mm x 10T x Short TAB x CW '),('SH000000003','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"DISC-T','3800','D78mm x 8.5T x 1/2\"-20T'),('SH000000004','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"PCD-CCW','8000','D78 x 타원2 x 33L- CCW'),('SH000000005','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"PCD-CW','8000','D78 x 타원2 x 33L- CW'),('SH000000006','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"PCD-TCCW','10000','D78 x 타원2 x 1/2\"-20T - CCW'),('SH000000007','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'3\"PCD-TCW','10000','D78 x 타원2 x 1/2\"-20T - CW'),('SH000000008','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'5\"CUP-5/8-11T','',''),('SH000000009','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'5\"CUP-B22.23H','',''),('SH000000010','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'7\"CUP-5/8-11T','',''),('SH000000011','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'7\"CUP-B22.23H','',''),('SH000000012','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'BULLET','',''),('SH000000013','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'CONE','',''),('SH000000014','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'DBS-CCW','6500','사각 89 x 41 x 12T - CCW'),('SH000000015','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'DBS-CW','6500','사각 89 x 41 x 12T - CW'),('SH000000016','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'DCHAN-CCW','',''),('SH000000017','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'DCHAN-CW','',''),('SH000000018','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'HTC','','80x50x절곡'),('SH000000019','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'HUQ','',''),('SH000000020','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'MIP1-1/4\"-80L','',''),('SH000000021','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'MIP2\"80L','',''),('SH000000022','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'MIP3\"-100L','',''),('SH000000023','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'MIP3\"80L','',''),('SH000000024','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RD948-CCW','9000','D78 x 6H - LONG TAB - CCW'),('SH000000025','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RD948-CW','9000','D78 x 6H - LONG TAB - CW'),('SH000000026','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RDS948-CCW','9000','D78-32 x 6H - LONG TAB - CCW'),('SH000000027','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RDS948-CW','9000','D78/32 x 6H - LONG TAB - CW'),('SH000000028','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RX948-CCW','10000','사각 76 x 62 x 14T - CCW'),('SH000000029','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'RX948-CW','10000','사각 76 x 62 x 14T - CW'),('SH000000030','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SBED-CCW','8000','사각 127 x 38 x 12T - CCW'),('SH000000031','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SBED-CW','8000','사각 127 x 38 x 12T - CW'),('SH000000032','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SCHAN-CCW','',''),('SH000000033','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SCHAN-CW','',''),('SH000000034','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SQ948-CCW','9000','사각 88 x 56 x 12T - CCW'),('SH000000035','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'SQ948-CW','9000','사각 88 x 56 x 12T - CW'),('SH000000036','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'TRAPEZOID-MG','',''),('SH000000037','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'TRAPEZOID-TAB','',''),('SH000000038','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'USBS-CCW','4900','사각 45 x 50 x 10T - CCW'),('SH000000039','2024-05-07 11:21:46','2024-05-07 11:21:46',NULL,'USBS-CW','4900','사각 45 x 50 x 10T - CW'),('SH000000040','2024-05-20 17:14:12','2024-05-20 17:14:12',NULL,'WMP','800','가느다란마법사'),('SH000000041','2024-05-20 21:19:32','2024-05-20 21:19:32',NULL,'격투가',NULL,NULL),('SH000000042','2024-05-20 21:19:42','2024-05-20 21:19:42',NULL,'격투가',NULL,NULL),('SH000000043','2024-05-20 21:19:47','2024-05-20 21:19:47',NULL,'근육인형',NULL,NULL),('SH000000044','2024-05-20 21:20:10','2024-05-20 21:20:10',NULL,NULL,'5000',NULL),('SH000000045','2024-05-20 21:22:32','2024-05-20 21:22:32',NULL,'크와와왕',NULL,NULL),('SH000000046','2024-05-20 21:22:36','2024-05-20 21:22:36',NULL,'크와와왕',NULL,NULL),('SH000000047','2024-05-20 21:22:43','2024-05-20 21:22:43',NULL,NULL,'123',NULL),('SH000000048','2024-05-20 21:22:47','2024-05-20 21:22:47',NULL,NULL,'123',NULL);
/*!40000 ALTER TABLE `shank` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_shank_insert` BEFORE INSERT ON `shank` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM shank;
    SET NEW.sys_id = CONCAT('SH', LPAD(next_id, 9, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `shank_BEFORE_UPDATE` BEFORE UPDATE ON `shank` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `sp`
--

DROP TABLE IF EXISTS `sp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sp` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `sys_ip_id` varchar(45) DEFAULT NULL,
  `sys_seg_id` varchar(45) DEFAULT NULL,
  `sys_bond_id` varchar(45) DEFAULT NULL,
  `sys_dia1_id` varchar(45) DEFAULT NULL,
  `sys_dia2_id` varchar(45) DEFAULT NULL,
  `sys_dia3_id` varchar(45) DEFAULT NULL,
  `sp_no` varchar(45) DEFAULT NULL,
  `sp_no1` varchar(45) DEFAULT NULL,
  `sp_no2` varchar(45) DEFAULT NULL,
  `sp_no3` varchar(45) DEFAULT NULL,
  `creation_date` varchar(45) DEFAULT NULL,
  `seg_no` varchar(45) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `amount_net` varchar(45) DEFAULT NULL,
  `amount_work` varchar(45) DEFAULT NULL,
  `specification_l` varchar(45) DEFAULT NULL,
  `specification_t` varchar(45) DEFAULT NULL,
  `specification_w` varchar(45) DEFAULT NULL,
  `specification_v` varchar(45) DEFAULT NULL,
  `specification_model_text` varchar(45) DEFAULT NULL,
  `specification_model_img` varchar(45) DEFAULT NULL,
  `bond_select` varchar(45) DEFAULT NULL,
  `bond_abs_density` varchar(45) DEFAULT NULL,
  `bond_hardness` varchar(45) DEFAULT NULL,
  `diamond_dia1_name` varchar(45) DEFAULT NULL,
  `diamond_dia1_ratio` varchar(45) DEFAULT NULL,
  `diamond_dia2_name` varchar(45) DEFAULT NULL,
  `diamond_dia2_ratio` varchar(45) DEFAULT NULL,
  `diamond_dia3_name` varchar(45) DEFAULT NULL,
  `diamond_dia3_ratio` varchar(45) DEFAULT NULL,
  `diamond_concent1` varchar(45) DEFAULT NULL,
  `diamond_concent2` varchar(45) DEFAULT NULL,
  `sint_temp` varchar(45) DEFAULT NULL,
  `sint_time` varchar(45) DEFAULT NULL,
  `sint_test_theo_density` varchar(45) DEFAULT NULL,
  `sint_test_benchmark` varchar(45) DEFAULT NULL,
  `forming_pressure` varchar(45) DEFAULT NULL,
  `forming_height` varchar(45) DEFAULT NULL,
  `dosing_diamix` varchar(45) DEFAULT NULL,
  `dosing_bond` varchar(45) DEFAULT NULL,
  `diamixing_bondmix_name` varchar(45) DEFAULT NULL,
  `diamixing_bondmix_amount` varchar(45) DEFAULT NULL,
  `diamixing_dia1_name` varchar(45) DEFAULT NULL,
  `diamixing_dia1_amount` varchar(45) DEFAULT NULL,
  `diamixing_dia2_name` varchar(45) DEFAULT NULL,
  `diamixing_dia2_amount` varchar(45) DEFAULT NULL,
  `diamixing_dia3_name` varchar(45) DEFAULT NULL,
  `diamixing_dia3_amount` varchar(45) DEFAULT NULL,
  `diamixing_zinc_check` varchar(45) DEFAULT NULL,
  `diamixing_zinc_amount` varchar(45) DEFAULT NULL,
  `diamixing_paraffin_check` varchar(45) DEFAULT NULL,
  `diamixing_paraffin_amount` varchar(45) DEFAULT NULL,
  `diamixing_mixing_time` varchar(45) DEFAULT NULL,
  `powdermixing_ballmill_time` varchar(45) DEFAULT NULL,
  `powdermixing_bond_name` varchar(45) DEFAULT NULL,
  `powdermixing_bond_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder1_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder1_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder1_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder2_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder2_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder2_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder3_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder3_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder3_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder4_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder4_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder4_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder5_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder5_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder5_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder6_name` varchar(45) DEFAULT NULL,
  `powdermixing_powder6_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder6_amount` varchar(45) DEFAULT NULL,
  `powdermixing_powder_total_ratio` varchar(45) DEFAULT NULL,
  `powdermixing_powder_total_amount` varchar(45) DEFAULT NULL,
  `memo1` varchar(300) DEFAULT NULL,
  `memo2` varchar(300) DEFAULT NULL,
  `memo3` varchar(300) DEFAULT NULL,
  `memo4` varchar(300) DEFAULT NULL,
  `workload` varchar(45) DEFAULT NULL,
  `weight_volume` varchar(45) DEFAULT NULL,
  `weight_abs_density` varchar(45) DEFAULT NULL,
  `weight_rel_density` varchar(45) DEFAULT NULL,
  `weight_loss` varchar(45) DEFAULT NULL,
  `weight_weight` varchar(45) DEFAULT NULL,
  `density_theo_density1` varchar(45) DEFAULT NULL,
  `density_theo_density2` varchar(45) DEFAULT NULL,
  `density_final_density` varchar(45) DEFAULT NULL,
  `density_final_rel_density` varchar(45) DEFAULT NULL,
  `veri_weight` varchar(45) DEFAULT NULL,
  `veri_count` varchar(45) DEFAULT NULL,
  `dia_volume` varchar(45) DEFAULT NULL,
  `dia_volume_rate` varchar(45) DEFAULT NULL,
  `dia_weight` varchar(45) DEFAULT NULL,
  `bond_volume` varchar(45) DEFAULT NULL,
  `bond_volume_rate` varchar(45) DEFAULT NULL,
  `bond_weight` varchar(45) DEFAULT NULL,
  `total_volume` varchar(45) DEFAULT NULL,
  `total_volume_rate` varchar(45) DEFAULT NULL,
  `total_weight` varchar(45) DEFAULT NULL,
  `checked` varchar(45) DEFAULT NULL,
  `ip_no` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sp`
--

LOCK TABLES `sp` WRITE;
/*!40000 ALTER TABLE `sp` DISABLE KEYS */;
INSERT INTO `sp` VALUES ('SP000000001','2024-05-06 14:19:25','2024-05-06 14:19:25',NULL,NULL,NULL,NULL,'DI000000003','DI000000004',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'d1',NULL,'d2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000002','2024-05-06 14:19:36','2024-05-06 14:19:36',NULL,NULL,NULL,'BO000000002',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'b1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000003','2024-05-13 08:56:33','2024-05-13 08:56:33',NULL,NULL,'SE000000001',NULL,NULL,NULL,NULL,'2024-SP0001','2024','SP0001',NULL,'2024-05-13','SQ0000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000004','2024-05-13 09:00:35','2024-05-13 09:00:35',NULL,NULL,'SE000000001',NULL,NULL,NULL,NULL,'2024-SP0002','2024','SP0002',NULL,'2024-05-13','SQ0000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000005','2024-05-13 09:00:52','2024-05-13 09:00:52',NULL,NULL,'SE000000001',NULL,NULL,NULL,NULL,'2024-SP0003','2024','SP0003',NULL,'2024-05-13','SQ0000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000006','2024-05-13 09:11:05','2024-05-13 09:11:05',NULL,NULL,'SE000000001',NULL,NULL,NULL,NULL,'2024-SP0004','2024','SP0004','2024-SP0003','2024-05-13','SQ0000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000007','2024-05-14 19:18:57','2024-05-14 19:18:57',NULL,NULL,'SE000000086',NULL,NULL,NULL,NULL,'2024-SP0005','2024','SP0005',NULL,'2024-05-14','SQ9999','SQ9999','2',NULL,'99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99','99',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000008','2024-05-17 10:37:43','2024-05-17 10:37:43',NULL,NULL,'SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0006','2024','SP0006','2024-SP0005','2024-05-17','SQ9999','SQ9999','2',NULL,'99','99','99','99','TEST_TXT','TEST_IMG','Q301',NULL,NULL,'2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99',NULL,'878',NULL,NULL,NULL,'99','99',NULL,NULL,'Q301',NULL,'2040 #120/140',NULL,'2040 #30/40',NULL,'2040 #6/8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Q301',NULL,'Co','45',NULL,'Cu#300','26',NULL,'Ni','24',NULL,'P₂O₅','0.5',NULL,'Sn#600','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000009','2024-05-17 10:39:13','2024-05-17 10:39:13',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0007','2024','SP0007','2024-SP0006','2024-05-17','SQ9999','SQ9999','2',NULL,'99','99','99','99','TEST_TXT','TEST_IMG','Q301',NULL,NULL,'2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99',NULL,'878',NULL,NULL,NULL,'99','99',NULL,NULL,'Q301',NULL,'2040 #120/140',NULL,'2040 #30/40',NULL,'2040 #6/8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Q301',NULL,'Co','45',NULL,'Cu#300','26',NULL,'Ni','24',NULL,'P₂O₅','0.5',NULL,'Sn#600','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0011'),('SP000000010','2024-05-17 10:44:09','2024-05-17 10:44:09',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0008','2024','SP0008','2024-SP0007','2024-05-17','SQ9999','SQ9999','2',NULL,'99','99','99','99','TEST_TXT','TEST_IMG','Q301',NULL,NULL,'2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99',NULL,'878',NULL,NULL,NULL,'99','99',NULL,NULL,'Q301',NULL,'2040 #120/140',NULL,'2040 #30/40',NULL,'2040 #6/8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Q301',NULL,'Co','45',NULL,'Cu#300','26',NULL,'Ni','24',NULL,'P₂O₅','0.5',NULL,'Sn#600','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0011'),('SP000000011','2024-05-17 10:50:37','2024-05-17 10:50:37',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0009','2024','SP0009','2024-SP0008','2024-05-17','SQ9999','SQ9999','2',NULL,'99','99','99','99','TEST_TXT','TEST_IMG','Q301',NULL,NULL,'2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99',NULL,'878',NULL,NULL,NULL,'99','99',NULL,NULL,'Q301',NULL,'2040 #120/140',NULL,'2040 #30/40',NULL,'2040 #6/8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Q301',NULL,'Co','45',NULL,'Cu#300','26',NULL,'Ni','24',NULL,'P₂O₅','0.5',NULL,'Sn#600','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-IP0011'),('SP000000012','2024-05-17 19:05:31','2024-05-17 19:05:31',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0010','2024','SP0010','2024-SP0009','2024-05-17','SQ9999','SQ9999','2',NULL,'99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,NULL,NULL,'99','99',NULL,NULL,'Q301',NULL,'2040 #120/140',NULL,'2040 #30/40',NULL,'2040 #6/8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Q301',NULL,'Co','45',NULL,'Cu#300','26',NULL,'Ni','24',NULL,'P₂O₅','0.5',NULL,'Sn#600','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92',NULL,NULL,'558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0011'),('SP000000013','2024-05-17 20:16:44','2024-05-17 20:16:44',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0011','2024','SP0011','2024-SP0010','2024-05-17','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0011'),('SP000000014','2024-05-17 20:20:21','2024-05-17 20:20:21',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0012','2024','SP0012','2024-SP0011','2024-05-17','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0011'),('SP000000015','2024-05-17 20:31:14','2024-05-17 20:31:14',NULL,'IP000000012','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0013','2024','SP0013','2024-SP0012','2024-05-17','SQ9999','SQ9999','1','-3.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','11665.02','2040 #120/140','-2940.00','2040 #30/40','-1764.00','2040 #6/8','-1176.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','10000.00','Co','45','4500.00','Cu#300','26','2600.00','Ni','24','2400.00','P₂O₅','0.5','50.00','Sn#600','5','500.00',NULL,NULL,NULL,'100.50','10050.00',NULL,NULL,NULL,NULL,'1.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','5785.02','5784.42','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0012'),('SP000000016','2024-05-17 20:33:24','2024-05-17 20:33:24',NULL,'IP000000011','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0014','2024','SP0014','2024-SP0013','2024-05-17','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0011'),('SP000000017','2024-05-17 20:36:51','2024-05-17 20:36:51',NULL,'IP000000013','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0015','2024','SP0015','2024-SP0014','2024-05-17','SQ9999','SQ9999','1','-3.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','11665.02','2040 #120/140','-2940.00','2040 #30/40','-1764.00','2040 #6/8','-1176.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','10000.00','Co','45','4500.00','Cu#300','26','2600.00','Ni','24','2400.00','P₂O₅','0.5','50.00','Sn#600','5','500.00',NULL,NULL,NULL,'100.50','10050.00',NULL,NULL,NULL,NULL,'1.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','5785.02','5784.42','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0013'),('SP000000018','2024-05-18 09:07:47','2024-05-18 09:07:47',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0016','2024','SP0016','2024-SP0015','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000019','2024-05-18 09:31:21','2024-05-18 09:31:21',NULL,'IP000000013','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0017','2024','SP0017','2024-SP0016','2024-05-18','SQ9999','SQ9999','1','-3.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','11665.02','2040 #120/140','-2940.00','2040 #30/40','-1764.00','2040 #6/8','-1176.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','10000.00','Co','45','4500.00','Cu#300','26','2600.00','Ni','24','2400.00','P₂O₅','0.5','50.00','Sn#600','5','500.00',NULL,NULL,NULL,'100.50','10050.00',NULL,NULL,NULL,NULL,'1.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','5785.02','5784.42','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0013'),('SP000000020','2024-05-18 09:33:07','2024-05-18 09:33:07',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0018','2024','SP0018','2024-SP0017','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000021','2024-05-18 09:34:27','2024-05-18 09:44:11',NULL,'IP000000013','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0019','2024','SP0019','2024-SP0018','2024-05-18','SQ9999','SQ9999','1','-3.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878','','-21.13','-19.86%','99','99','-1928.14','837.82','Q301','11665.02','2040 #120/140','-2940.00','2040 #30/40','-1764.00','2040 #6/8','-1176.00','','','','','','','Q301','10000.00','Co','45','4500.00','Cu#300','26','2600.00','Ni','24','2400.00','P₂O₅','0.5','50.00','Sn#600','5','500.00','','','','100.50','10050.00','memo','','','','1.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','5785.02','5784.42','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14','1','2024-IP0013'),('SP000000022','2024-05-18 09:34:27','2024-05-18 16:55:06',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0020','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','1','1','1','1','1','1','','','','','','','','','','','','','','','','3','2024-IP0014'),('SP000000023','2024-05-18 15:04:31','2024-05-18 15:04:31',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0021','2024','SP0021','2024-SP0020','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000024','2024-05-18 16:43:57','2024-05-18 16:43:57',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0022','2024','SP0022','2024-SP0021','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000025','2024-05-18 18:58:13','2024-05-18 18:58:13',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0023','2024','SP0023','2024-SP0022','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000026','2024-05-18 18:59:02','2024-05-18 18:59:02',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0024','2024','SP0024','2024-SP0023','2024-05-18','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000027','2024-05-19 20:11:29','2024-05-19 20:11:29',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0025','2024','SP0025','2024-SP0024','2024-05-19','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000028','2024-05-19 21:02:11','2024-05-19 21:02:11',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0026','2024','SP0026','2024-SP0025','2024-05-19','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000029','2024-05-19 21:02:43','2024-05-19 21:02:43',NULL,'IP000000014','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0027','2024','SP0027','2024-SP0026','2024-05-19','SQ9999','SQ9999','2','1.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-3888.34','2040 #120/140','981.00','2040 #30/40','589.00','2040 #6/8','393.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-5000.00','Co','45','-2250.00','Cu#300','26','-1300.00','Ni','24','-1200.00','P₂O₅','0.5','-25.00','Sn#600','5','-250.00',NULL,NULL,NULL,'100.50','-5025.00',NULL,NULL,NULL,NULL,'2.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-1925.34','-1928.14','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0014'),('SP000000030','2024-05-20 17:22:23','2024-05-20 17:22:23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2024-SP0028','2024','SP0028',NULL,'2024-05-20',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('SP000000031','2024-05-20 21:13:29','2024-05-20 21:13:29',NULL,'IP000000018','SE000000086','BO000000001','DI000000003','DI000000007','DI000000011','2024-SP0029','2024','SP0029','2024-SP0027','2024-05-20','SQ9999','SQ9999','3','2.00','99','99','99','99','TEST_TXT','TEST_IMG','Q301','8.82','64','2040 #120/140','5','2040 #30/40','3','2040 #6/8','2','99','2250.00%','878',NULL,'-21.13','-19.86%','99','99','-1928.14','837.82','Q301','-7776.68','2040 #120/140','1961.00','2040 #30/40','1177.00','2040 #6/8','785.00',NULL,NULL,NULL,NULL,NULL,NULL,'Q301','-10000.00','Co','45','-4500.00','Cu#300','26','-2600.00','Ni','24','-2400.00','P₂O₅','0.5','-50.00','Sn#600','5','-500.00',NULL,NULL,NULL,'100.50','-10050.00',NULL,NULL,NULL,NULL,'3.00','99','8.82','0.95','1.01','837.82','-21.13','-21.12','-19.48','0.92','-3853.68','-3856.28','558.46','5.64','1960.20','-459.46','-4.64','-3888.34','99.00','1.00','-1928.14',NULL,'2024-IP0018');
/*!40000 ALTER TABLE `sp` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_sp_insert` BEFORE INSERT ON `sp` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM sp;
    SET NEW.sys_id = CONCAT('SP', LPAD(next_id, 9, '0'));
    
	SELECT IFNULL(MAX(SUBSTRING(`sp_no2`, 3)) + 1, 1) INTO next_id FROM sp;
    SET NEW.`sp_no2` = CONCAT('SP', LPAD(next_id, 4, '0'));
    SET NEW.`sp_no1` = DATE_FORMAT(NOW(), '%Y');
    SET NEW.`sp_no` = CONCAT(NEW.`sp_no1`,'-', NEW.`sp_no2`);
    SET NEW.`creation_date` = DATE_FORMAT(NOW(), '%Y-%m-%d');
    -- ----------------------------------------------------------------------
	IF NEW.ip_no IS NOT NULL THEN
        SET NEW.sys_ip_id = (SELECT sys_id FROM ip WHERE ip.ip_no = NEW.ip_no);
    END IF;       
	IF NEW.seg_no IS NOT NULL THEN
        SET NEW.sys_seg_id = (SELECT sys_id FROM segment WHERE segment.seg_no = NEW.seg_no);
		SET NEW.sp_no3 = (SELECT recent_sp FROM segment WHERE segment.seg_no = NEW.seg_no);          
    END IF;
	IF NEW.bond_select IS NOT NULL THEN
        SET NEW.sys_bond_id = (SELECT sys_id FROM bond WHERE bond.product_name = NEW.bond_select);
    END IF;
	IF NEW.diamond_dia1_name IS NOT NULL THEN
        SET NEW.sys_dia1_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.diamond_dia1_name);
    END IF;          
	IF NEW.diamond_dia2_name IS NOT NULL THEN
        SET NEW.sys_dia2_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.diamond_dia2_name);
    END IF;       
	IF NEW.diamond_dia3_name IS NOT NULL THEN
        SET NEW.sys_dia3_id = (SELECT sys_id FROM diamond WHERE diamond.product_name = NEW.diamond_dia3_name);
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `sp_AFTER_INSERT` AFTER INSERT ON `sp` FOR EACH ROW BEGIN
    UPDATE ip
    SET seg1_sp_no = NEW.sp_no, sys_sp1_id = NEW.sys_id
    WHERE ip.seg1_sp_no IS NULL
		AND ip.seg1_no = NEW.seg_no ;
        
    UPDATE ip
    SET seg2_sp_no = NEW.sp_no, sys_sp2_id = NEW.sys_id
    WHERE ip.seg2_sp_no IS NULL
		AND ip.seg2_no = NEW.seg_no ;
        
    UPDATE item_order
    SET sp_no = NEW.sp_no, sys_sp_id = NEW.sys_id
	WHERE item_order.sp_no IS NULL
		AND item_order.ip_no = NEW.ip_no ;
        
    UPDATE segment
    SET recent_sp = NEW.sp_no
    WHERE segment.seg_no = NEW.seg_no ;   
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `sp_BEFORE_UPDATE` BEFORE UPDATE ON `sp` FOR EACH ROW BEGIN
	SET NEW.sys_update_date = CURRENT_TIMESTAMP;

	IF NEW.checked IS NULL OR NEW.checked = '' THEN
		SET NEW.checked = 1;
	ELSE
		SET NEW.checked = NEW.checked + 1;
	END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `submaterial`
--

DROP TABLE IF EXISTS `submaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `submaterial` (
  `sys_id` varchar(11) NOT NULL,
  `sys_reg_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '자동생성',
  `sys_description` varchar(300) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sys_id`),
  UNIQUE KEY `sys_id_UNIQUE` (`sys_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `submaterial`
--

LOCK TABLES `submaterial` WRITE;
/*!40000 ALTER TABLE `submaterial` DISABLE KEYS */;
INSERT INTO `submaterial` VALUES ('SU000000001','2024-05-07 10:52:18','2024-05-07 10:52:18','US$6.00','PCD10','9000'),('SU000000002','2024-05-07 10:52:18','2024-05-07 10:52:18','US$6.30','PCD12','10000'),('SU000000003','2024-05-07 10:52:18','2024-05-07 10:52:18','','PCD20',''),('SU000000004','2024-05-07 10:52:18','2024-05-07 10:52:18','','PCD5X5',''),('SU000000005','2024-05-07 10:52:18','2024-05-07 10:52:18','','PCD8','11500'),('SU000000006','2024-05-07 10:52:18','2024-05-07 10:52:18','','POST10','1000'),('SU000000007','2024-05-07 10:52:18','2024-05-07 10:52:18','','POST12','1200'),('SU000000008','2024-05-07 10:52:18','2024-05-07 10:52:18','','POST6',''),('SU000000009','2024-05-07 10:52:18','2024-05-07 10:52:18','','TSP',''),('SU000000010','2024-05-20 17:14:46','2024-05-20 17:14:46',NULL,'AAA','2000');
/*!40000 ALTER TABLE `submaterial` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `before_submaterial_insert` BEFORE INSERT ON `submaterial` FOR EACH ROW BEGIN
    DECLARE next_id INT;
    SELECT IFNULL(MAX(SUBSTRING(sys_id, 3)) + 1, 1) INTO next_id FROM submaterial;
    SET NEW.sys_id = CONCAT('SU', LPAD(next_id, 9, '0'));
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `submaterial_BEFORE_UPDATE` BEFORE UPDATE ON `submaterial` FOR EACH ROW BEGIN
SET NEW.sys_update_date = CURRENT_TIMESTAMP;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping events for database 'nova_db'
--

--
-- Dumping routines for database 'nova_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-29 18:53:16
