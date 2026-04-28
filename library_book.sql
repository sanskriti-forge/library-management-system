-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(60) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `pages` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `publisher` varchar(60) DEFAULT NULL,
  `edition` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'Things We Never Got Over','Lucy Score',540,250,'available','Bloom Books','2021'),(2,'Atomic Habits','James Clear',290,210,'available','Random House Business','2022'),(3,'Verity','Collen Hoover',288,199,'available','Hachette Book Groups','2022'),(4,'Beach Read','Emily Henry',291,190,'available','Penguin Publishing Group','2020'),(5,'Harry Potter and the Chamber of Secrets','J.K. Rowling',341,389,'issue','Scholastic Inc.','2001'),(6,'Harry Potter and The Philosopher Stone','J.K Rowling',223,199,'issue','Scholastic Inc.','1997'),(7,'Harry Potter and the Order of Pheonix','J.K Rowling',896,230,'available','Scholastic Inc.','349'),(8,'Harry Potter and the Sorcerer\'s Stone','J.K Rowling',320,199,'available','Scholastic Inc.','2001'),(9,'Harry Potter and the Goblet Of Fire','J.K Rowling',431,259,'available','Scholastic Inc.','2007'),(10,'Harry Potter and the Deathly Hallows','J.k Rowling',784,345,'available','Scholastic Inc.','2010'),(11,'Harry Potter and the Half Blood Prince','J.K. Rowling',297,199,'available','Scholastic Inc.','2007'),(12,'Harry Potter and The Prisoner Of Azkaban','J.K. Rowling',431,260,'available','Scholastic Inc','2008'),(13,'Book Lovers','Emily Henry',342,210,'available','Blackstone Inc.','2019'),(14,'Karna\'s Wheel','Michael Tobert',252,180,'available','Synopsis ','2018'),(15,'All The Bright Places','Jennifer Niven',256,300,'available','Knopf Publishing Group','2014'),(16,'The Reunion','Kayla Olson',388,659,'available','Gen n George Publishing grp','2023'),(17,'Twisted series-games, love, hate, lies.','Ana Huang',530,299,'available','Boba Press.','2020'),(18,'Twisted Games','Ana Huang',340,250,'available','Boba Press.','2020'),(19,'Twisted Hate',' Ana Huang',356,300,'available','Boba Press','2021'),(20,'A Court Of Thorns And Roses','Sarah Maas',1879,2980,'available','divergg','2023');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;


