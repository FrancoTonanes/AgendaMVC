USE [master]
GO

/****** Object:  Database [AgendaDB2]    Script Date: 21/9/2020 12:17:45 ******/
CREATE DATABASE [AgendaDB2]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'AgendaDB2', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\AgendaDB2.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'AgendaDB2_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\AgendaDB2_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [AgendaDB2].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [AgendaDB2] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [AgendaDB2] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [AgendaDB2] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [AgendaDB2] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [AgendaDB2] SET ARITHABORT OFF 
GO

ALTER DATABASE [AgendaDB2] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [AgendaDB2] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [AgendaDB2] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [AgendaDB2] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [AgendaDB2] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [AgendaDB2] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [AgendaDB2] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [AgendaDB2] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [AgendaDB2] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [AgendaDB2] SET  DISABLE_BROKER 
GO

ALTER DATABASE [AgendaDB2] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [AgendaDB2] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [AgendaDB2] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [AgendaDB2] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [AgendaDB2] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [AgendaDB2] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [AgendaDB2] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [AgendaDB2] SET RECOVERY SIMPLE 
GO

ALTER DATABASE [AgendaDB2] SET  MULTI_USER 
GO

ALTER DATABASE [AgendaDB2] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [AgendaDB2] SET DB_CHAINING OFF 
GO

ALTER DATABASE [AgendaDB2] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [AgendaDB2] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [AgendaDB2] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [AgendaDB2] SET QUERY_STORE = OFF
GO

ALTER DATABASE [AgendaDB2] SET  READ_WRITE 
GO

USE [AgendaDB2]
GO

/****** Object:  Table [dbo].[agenda]    Script Date: 21/9/2020 12:19:57 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[agenda](
	[id_agenda] [varchar](50) NOT NULL,
	[propietario] [varchar](50) NOT NULL,
 CONSTRAINT [PK_agenda] PRIMARY KEY CLUSTERED 
(
	[id_agenda] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [AgendaDB2]
GO

/****** Object:  Table [dbo].[contacto]    Script Date: 21/9/2020 12:20:42 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[contacto](
	[dni] [int] NOT NULL,
	[id_agenda] [varchar](50) NOT NULL,
	[nombre] [varchar](50) NOT NULL,
	[telefono] [int] NULL,
	[email] [varchar](50) NULL,
 CONSTRAINT [PK_contacto] PRIMARY KEY CLUSTERED 
(
	[dni] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[contacto]  WITH CHECK ADD  CONSTRAINT [FK_contacto_agenda] FOREIGN KEY([id_agenda])
REFERENCES [dbo].[agenda] ([id_agenda])
GO

ALTER TABLE [dbo].[contacto] CHECK CONSTRAINT [FK_contacto_agenda]
GO



