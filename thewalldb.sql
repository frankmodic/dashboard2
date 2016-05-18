-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: thewalldb
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message_id` int(11) NOT NULL,
  `comment` text,
  `message_receiver_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (4,1,4,'Keep the streak alive!',NULL,'2016-05-11 15:18:55','2016-05-11 15:18:55'),(5,2,4,'we will!',NULL,'2016-05-11 19:07:26','2016-05-11 19:07:26'),(6,1,5,'THIS IS FOR NAZIM',NULL,'2016-05-11 19:20:24','2016-05-11 19:20:24'),(7,1,6,'WTF did you do!?',NULL,'2016-05-11 19:29:58','2016-05-11 19:29:58'),(8,1,3,'PLEASE WORK',NULL,'2016-05-11 19:36:44','2016-05-11 19:36:44'),(9,1,5,'whoooo!\r\n',NULL,'2016-05-11 19:44:49','2016-05-11 19:44:49'),(20,1,10,'ewfogpghgh4og4g4',10,'2016-05-17 18:00:34',NULL),(21,1,10,'wqf3f3f23g32g23g',10,'2016-05-17 18:02:52',NULL),(22,1,10,'eewgwg4hg5eht5hhae',10,'2016-05-17 18:09:46',NULL),(23,1,10,'egewgwegwg',10,'2016-05-17 18:24:45',NULL),(24,1,10,'PRINT THIS',10,'2016-05-17 18:33:47',NULL),(25,1,15,'FUUUUUUUUUUCK!',15,'2016-05-17 18:44:10',NULL),(26,1,15,'^ it works!',15,'2016-05-17 19:16:46',NULL),(27,1,15,'test this shit again!',15,'2016-05-17 19:17:22',NULL),(28,1,15,'OMG AGAIN',15,'2016-05-17 19:20:01',NULL),(29,2,15,'ahhhhhhhhhh',15,'2016-05-17 19:43:40',NULL),(30,2,15,'ahhhhhhhhhh',15,'2016-05-17 19:43:50',NULL),(31,2,15,'fuck fuck fuck ',15,'2016-05-17 19:44:37',NULL);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `receiver_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `messagescol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,1,'FUCK THE WALL!',NULL,'2016-05-11 14:29:38','2016-05-11 14:29:38',NULL),(3,1,'AHHHHHHHHHHHHHHHHHHHHH',NULL,'2016-05-11 14:32:06','2016-05-11 14:32:06',NULL),(4,2,'FUCK!',NULL,'2016-05-11 15:09:11','2016-05-11 15:09:11',NULL),(5,1,'NOT WORKING ANYMORE',NULL,'2016-05-11 19:19:47','2016-05-11 19:19:47',NULL),(6,1,'WTF!',NULL,'2016-05-11 19:20:41','2016-05-11 19:20:41',NULL),(10,6,'duuuuuuuuude!',1,'2016-05-17 15:53:51',NULL,NULL),(11,1,'I BROKE DIS SOME HOW',2,'2016-05-17 16:21:34',NULL,NULL),(12,1,'Thank you for the help!',6,'2016-05-17 16:40:29',NULL,NULL),(14,1,'WHO NEEDS COMMENTS WHEN I CAN POST?!',6,'2016-05-17 18:12:34',NULL,NULL),(15,1,'oiwebfoaiewgbge',1,'2016-05-17 18:43:44',NULL,NULL);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `user_level` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `description` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Frank','Modic','123fake@gmail.com',9,'$2b$12$vbGY2bHSCUqb1VFD9xNSJeX.dLqK1/5SDi.Rx4Gk.u57o5xflktrq','Where will this end up??','2016-05-17 00:37:08','2016-05-17 11:12:52'),(2,'Grant','Rosen','321fake@gmail.com',8,'$2b$12$b0DzyZkeiEUcWbP2bujtx.qyc.oav2INhkFUcV36ZDoDyI3VL6gnG',NULL,'2016-05-11 14:35:43','2016-05-11 14:35:43'),(6,'Nazim','Chilno','123@gmail.com',1,'$2b$12$ZLnhaGtlBOusQ26jwNlyquzhjrQiq00CVZlvW8lR.5UqwufIEEfKW','YEEEEEHAW!','2016-05-17 11:37:43',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-18 15:30:22
