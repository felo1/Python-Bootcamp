-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: telovendo_db
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `run` varchar(12) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `seccion` varchar(100) DEFAULT NULL,
  `porcentaje_comision` decimal(3,1) DEFAULT NULL,
  `edad` int DEFAULT NULL,
  `comision` int DEFAULT NULL,
  `sueldo` int DEFAULT NULL,
  PRIMARY KEY (`run`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES ('11223344-2','Ricardo','Morales','Belleza',3.9,55,220000,800000),('11223344-5','Pedro','González','Hogar',7.8,45,300000,900000),('12345678-9','Juan','Pérez','Electrónica',5.5,30,200000,800000),('22334455-6','Luis','Hernández','Electrodomésticos',4.9,32,180000,750000),('55667788-2','Carolina','Ramírez','Deportes',2.5,28,100000,600000),('66554433-8','Ana','Torres','Joyería',1.7,35,120000,650000),('77889900-4','Laura','Castro','Alimentos',6.7,33,280000,950000),('98765432-1','María','López','Ropa',3.2,40,150000,700000),('99887766-1','Sofía','Gómez','Libros',8.3,42,350000,1000000),('99887766-3','Fernando','Silva','Muebles',6.1,50,250000,850000);
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `sku` varchar(6) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `categoria` varchar(100) DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `precio` int DEFAULT NULL,
  PRIMARY KEY (`sku`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES ('000','Camiseta','Ropa','Confecciones Moderna Ltda','Blanco',15000),('001','Pantalón','Ropa','Moda Urbana S.A.','Negro',30000),('002','Zapatos','Calzado','Calzados Elegantes SPA','Marrón',50000),('003','Televisor','Electrónica','Tecnología Avanzada S.A.','Negro',250000),('004','Refrigerador','Electrodomésticos','Electrohogar Ltda','Plata',350000),('005','Mesa','Muebles','Diseño Interior S.A.','Blanco',100000),('006','Reloj','Accesorios','Accesorios de Moda SPA','Dorado',80000),('007','Libro','Libros','Editorial Cultural Ltda','Varios',20000),('008','Cámara','Electrónica','Tecnología Innovadora S.A.','Negro',180000),('009','Lámpara','Iluminación','Luz Ambiental Ltda','Plateado',50000);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` varchar(12) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  `saldo` int DEFAULT NULL,
  `total_comprado` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('11111111-3','Valentina','Fuentes','valentina.fuentes@example.com','2021-05-01',60000,450000),('11223344-2','Ricardo','Morales','ricardo.morales@example.com','2021-09-20',25000,450000),('11223344-5','Pedro','González','pedro.gonzalez@example.com','2022-03-10',200000,400000),('12345678-9','Juan','Pérez','juan.perez@example.com','2022-05-18',50000,500000),('22222222-4','Diego','Sánchez','diego.sanchez@example.com','2021-04-15',30000,250000),('22334455-6','Luis','Hernández','luis.hernandez@example.com','2021-12-10',50000,300000),('33333333-5','Camila','Morales','camila.morales@example.com','2021-03-20',100000,150000),('34567890-1','Andrea','Martínez','andrea.martinez@example.com','2021-07-10',80000,400000),('44444444-6','Ignacio','López','ignacio.lopez@example.com','2021-02-10',70000,200000),('55555555-7','Isabella','García','isabella.garcia@example.com','2021-01-05',25000,100000),('55667788-2','Carolina','Ramírez','carolina.ramirez@example.com','2022-02-05',10000,100000),('66554433-8','Ana','Torres','ana.torres@example.com','2021-11-05',75000,200000),('77889900-4','Laura','Castro','laura.castro@example.com','2021-08-15',5000,500000),('87654321-2','Gabriel','Rodríguez','gabriel.rodriguez@example.com','2021-06-05',120000,300000),('98765432-1','María','López','maria.lopez@example.com','2022-04-15',150000,250000),('99887766-1','Sofía','Gómez','sofia.gomez@example.com','2021-10-01',100000,350000),('99887766-3','Fernando','Silva','fernando.silva@example.com','2022-01-01',0,150000);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-23 20:28:46
