-- MySQL dump 10.13  Distrib 5.7.20, for osx10.13 (x86_64)
--
-- Host: localhost    Database: scrum
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'2019日常迭代'),(2,'微信通知二期');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scrum`
--

DROP TABLE IF EXISTS `scrum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scrum` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(11) unsigned DEFAULT NULL,
  `No` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `total_sprint` float DEFAULT NULL,
  `start_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `end_date` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrum`
--

LOCK TABLES `scrum` WRITE;
/*!40000 ALTER TABLE `scrum` DISABLE KEYS */;
INSERT INTO `scrum` VALUES (1,1,'0722',20,'2019-07-22','2019-08-02'),(2,1,'0805',36,'2019-08-05','2019-08-16'),(3,1,'0819',32.5,'2019-08-19','2019-08-30'),(4,2,'迭代1',22,'2019-08-19','2019-08-20');
/*!40000 ALTER TABLE `scrum` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scrum_sprint`
--

DROP TABLE IF EXISTS `scrum_sprint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scrum_sprint` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `scrum_id` int(11) DEFAULT NULL,
  `day` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `left_sprint` float DEFAULT NULL,
  `type` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scrum_sprint`
--

LOCK TABLES `scrum_sprint` WRITE;
/*!40000 ALTER TABLE `scrum_sprint` DISABLE KEYS */;
INSERT INTO `scrum_sprint` VALUES (1,1,'2019-07-22',18,NULL),(2,1,'2019-07-23',15,NULL),(3,1,'2019-07-24',12,NULL),(4,1,'2019-07-25',10,NULL),(5,1,'2019-07-26',10,NULL),(6,1,'2019-07-27',10,NULL),(7,1,'2019-07-28',10,NULL),(8,1,'2019-07-29',5,NULL),(9,1,'2019-07-30',3,NULL),(10,1,'2019-07-31',2,NULL),(11,1,'2019-08-01',0,NULL),(12,1,'2019-08-02',0,NULL),(13,2,'2019-08-05',36,NULL),(14,2,'2019-08-06',34,NULL),(15,2,'2019-08-07',29,NULL),(16,2,'2019-08-08',15,NULL),(17,2,'2019-08-09',13,NULL),(18,2,'2019-08-10',13,NULL),(19,2,'2019-08-11',13,NULL),(20,2,'2019-08-12',10,NULL),(21,2,'2019-08-13',1,NULL),(22,2,'2019-08-14',0,NULL),(23,3,'2019-08-19',32.5,NULL),(24,3,'2019-08-20',32.5,NULL),(25,3,'2019-08-21',29,NULL),(26,3,'2019-08-22',29.5,NULL),(27,4,'2019-08-12',12,NULL),(28,4,'2019-08-13',13,NULL);
/*!40000 ALTER TABLE `scrum_sprint` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-02 21:55:03
