-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 04, 2023 at 02:02 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quiz_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
CREATE TABLE IF NOT EXISTS `answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `quiz_id` int NOT NULL,
  `question_id` int NOT NULL,
  `option_id` int NOT NULL,
  `is_right` tinyint(1) NOT NULL COMMENT ' 1 = right, 0 = wrong',
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `user_id`, `quiz_id`, `question_id`, `option_id`, `is_right`, `date_updated`) VALUES
(17, 2214219, 11, 37, 215, 1, '2023-02-04 22:55:17'),
(18, 2214219, 11, 39, 241, 1, '2023-02-04 22:55:17'),
(19, 2214219, 11, 40, 238, 1, '2023-02-04 22:55:17'),
(20, 2214219, 11, 41, 235, 0, '2023-02-04 22:55:17'),
(21, 2214219, 11, 42, 245, 1, '2023-02-04 22:55:17'),
(22, 2214219, 12, 27, 152, 1, '2023-02-04 22:56:34'),
(23, 2214219, 12, 28, 162, 1, '2023-02-04 22:56:34'),
(24, 2214219, 12, 29, 157, 1, '2023-02-04 22:56:34'),
(25, 2214219, 12, 30, 172, 1, '2023-02-04 22:56:34'),
(26, 2214219, 12, 31, 176, 0, '2023-02-04 22:56:34'),
(27, 2214219, 12, 32, 180, 0, '2023-02-04 22:56:34'),
(28, 2214219, 12, 33, 184, 0, '2023-02-04 22:56:34'),
(29, 2214219, 12, 34, 187, 0, '2023-02-04 22:56:34'),
(30, 2214219, 12, 35, 189, 1, '2023-02-04 22:56:34'),
(31, 2214219, 12, 36, 196, 0, '2023-02-04 22:56:34');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
CREATE TABLE IF NOT EXISTS `faculty` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `subject` varchar(100) NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`id`, `user_id`, `subject`, `date_updated`) VALUES
(1, 1111, 'Soft Eng', '2023-02-04 22:32:52'),
(2, 2222, 'Math', '2023-02-04 22:33:13');

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
CREATE TABLE IF NOT EXISTS `history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quiz_id` int NOT NULL,
  `user_id` int NOT NULL,
  `score` int NOT NULL,
  `total_score` int NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`id`, `quiz_id`, `user_id`, `score`, `total_score`, `date_updated`) VALUES
(9, 11, 2214219, 8, 10, '2023-02-04 22:55:17'),
(10, 12, 2214219, 5, 10, '2023-02-04 22:56:34');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` text NOT NULL,
  `qid` int NOT NULL,
  `order_by` int NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `question`, `qid`, `order_by`, `date_updated`) VALUES
(27, 'Which of the following is NOT included in Generic Process Models?', 12, 0, '2023-02-04 22:39:05'),
(28, 'Which of the following is NOT included in Specific Process Models?', 12, 0, '2023-02-04 22:39:34'),
(29, 'Which of the following is NOT included in Characteristics of Software?', 12, 0, '2023-02-04 22:40:05'),
(30, 'Which of the following is NOT included in Fundamental Process Activities of Software Process?', 12, 0, '2023-02-04 22:44:41'),
(31, 'Which of the following is NOT an advantage of the Waterfall Model?', 12, 0, '2023-02-04 22:45:20'),
(32, 'Which of the following is NOT a description of the Waterfall model?', 12, 0, '2023-02-04 22:45:45'),
(33, 'Which of the following is NOT a disadvantage of Evolutionary Development?', 12, 0, '2023-02-04 22:46:14'),
(34, 'Which of the following is NOT a description of the Incremental model?', 12, 0, '2023-02-04 22:46:41'),
(35, 'Which of the following is NOT an advantage of the Spiral Development Model?', 12, 0, '2023-02-04 22:47:14'),
(36, 'Which of the following is NOT included in best practices for Rational Unified Process?', 12, 0, '2023-02-04 22:47:46'),
(37, 'It is often a straightforward proposition to determine the performance of a system as a function of its parameters.', 11, 0, '2023-02-04 22:49:26'),
(39, 'This is the discrepancy between an exact value and some approximation to it.', 11, 0, '2023-02-04 22:58:03'),
(40, 'This is the summation of the truncation and round-off errors', 11, 0, '2023-02-04 22:51:43'),
(41, '_________ refers to how closely a computed or measured value agrees with the true value.', 11, 0, '2023-02-04 22:52:03'),
(42, 'It is a special type of software that allows the user to enter and perform calculations on rows and columns of data.', 11, 0, '2023-02-04 22:53:14');

-- --------------------------------------------------------

--
-- Table structure for table `question_opt`
--

DROP TABLE IF EXISTS `question_opt`;
CREATE TABLE IF NOT EXISTS `question_opt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `option_txt` text NOT NULL,
  `question_id` int NOT NULL,
  `is_right` tinyint NOT NULL DEFAULT '0' COMMENT '1= right answer',
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=253 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `question_opt`
--

INSERT INTO `question_opt` (`id`, `option_txt`, `question_id`, `is_right`, `date_updated`) VALUES
(113, 'Large versus systems', 24, 0, '2023-02-04 22:36:58'),
(114, 'Nonlinear versus linear', 24, 0, '2023-02-04 22:36:58'),
(115, 'Design', 24, 0, '2023-02-04 22:36:58'),
(116, 'Sensitivity analysis', 24, 0, '2023-02-04 22:36:58'),
(121, 'Waterfall model', 26, 0, '2023-02-04 22:39:03'),
(122, 'Evolutionary development', 26, 0, '2023-02-04 22:39:03'),
(123, 'Formal systems development', 26, 0, '2023-02-04 22:39:03'),
(124, 'Use-based development', 26, 0, '2023-02-04 22:39:03'),
(149, 'Waterfall model', 27, 0, '2023-02-04 22:42:22'),
(150, 'Evolutionary development', 27, 0, '2023-02-04 22:42:22'),
(151, 'Formal systems development', 27, 0, '2023-02-04 22:42:22'),
(152, 'Use-based development', 27, 1, '2023-02-04 22:42:22'),
(157, 'Software does “wear out”.', 29, 1, '2023-02-04 22:42:59'),
(158, 'Software is abstract and intangible.', 29, 0, '2023-02-04 22:42:59'),
(159, 'Software is developed or engineered; it is not manufactured in the classical sense.', 29, 0, '2023-02-04 22:42:59'),
(160, 'Most software is custom-built, rather than being assembled from existing components.', 29, 0, '2023-02-04 22:42:59'),
(161, 'Incremental model', 28, 0, '2023-02-04 22:43:41'),
(162, 'Object-Based Development Model', 28, 1, '2023-02-04 22:43:41'),
(163, 'Spiral Development Model', 28, 0, '2023-02-04 22:43:41'),
(164, 'Package-Based Development Model', 28, 0, '2023-02-04 22:43:41'),
(169, 'Specification', 30, 0, '2023-02-04 22:44:49'),
(170, 'Development', 30, 0, '2023-02-04 22:44:49'),
(171, 'Validation', 30, 0, '2023-02-04 22:44:49'),
(172, 'None of the above', 30, 1, '2023-02-04 22:44:49'),
(173, 'Very clear from a managerial viewpoint - easy to model, plan, monitor, and understand', 31, 0, '2023-02-04 22:45:20'),
(174, 'Many existing tools support this model', 31, 0, '2023-02-04 22:45:20'),
(175, 'Development is relatively slow and deliberate and thus, results in solid, well-constructed systems', 31, 0, '2023-02-04 22:45:20'),
(176, 'Last explicit process model', 31, 0, '2023-02-04 22:45:20'),
(177, 'Linear sequential model', 32, 0, '2023-02-04 22:45:45'),
(178, 'Describe a set of clear stages in the development process', 32, 0, '2023-02-04 22:45:45'),
(179, 'Based on engineering practice', 32, 0, '2023-02-04 22:45:45'),
(180, 'None of the above', 32, 0, '2023-02-04 22:45:45'),
(181, 'Cost, time, and resource estimation is difficult ', 33, 0, '2023-02-04 22:46:14'),
(182, 'Process is not visible', 33, 0, '2023-02-04 22:46:14'),
(183, 'Progress is difficult to measure ', 33, 0, '2023-02-04 22:46:14'),
(184, 'Less effective than waterfall model', 33, 0, '2023-02-04 22:46:14'),
(185, 'Suggested by Mills 1980', 34, 0, '2023-02-04 22:46:41'),
(186, 'In between waterfall and evolutionary', 34, 0, '2023-02-04 22:46:41'),
(187, 'Increase rework in the development process', 34, 0, '2023-02-04 22:46:41'),
(188, 'Give customers opportunity to delay decisions', 34, 0, '2023-02-04 22:46:41'),
(189, 'Delayed error elimination', 35, 1, '2023-02-04 22:47:14'),
(190, 'Puts quality objectives up front', 35, 0, '2023-02-04 22:47:14'),
(191, 'Integrates development and maintenance', 35, 0, '2023-02-04 22:47:14'),
(192, 'None of the above', 35, 0, '2023-02-04 22:47:14'),
(193, 'Develop software iteratively', 36, 0, '2023-02-04 22:47:46'),
(194, 'Manage requirements', 36, 0, '2023-02-04 22:47:46'),
(195, 'Component based architecture', 36, 0, '2023-02-04 22:47:46'),
(196, 'None of the above', 36, 0, '2023-02-04 22:47:46'),
(197, 'Round-off errors', 25, 0, '2023-02-04 22:48:53'),
(198, 'Total numerical error', 25, 0, '2023-02-04 22:48:53'),
(199, 'Truncation error', 25, 0, '2023-02-04 22:48:53'),
(200, 'Approximation error ', 25, 1, '2023-02-04 22:48:53'),
(205, 'Large versus systems', 38, 0, '2023-02-04 22:49:29'),
(206, 'Nonlinear versus linear', 38, 0, '2023-02-04 22:49:29'),
(207, 'Design', 38, 0, '2023-02-04 22:49:29'),
(208, 'Sensitivity analysis', 38, 0, '2023-02-04 22:49:29'),
(213, 'Large versus systems', 37, 0, '2023-02-04 22:50:01'),
(214, 'Nonlinear versus linear', 37, 0, '2023-02-04 22:50:01'),
(215, 'Design', 37, 1, '2023-02-04 22:50:01'),
(216, 'Sensitivity analysis', 37, 0, '2023-02-04 22:50:01'),
(233, 'Precision', 41, 0, '2023-02-04 22:52:03'),
(234, 'True value', 41, 0, '2023-02-04 22:52:03'),
(235, 'Accuracy', 41, 0, '2023-02-04 22:52:03'),
(236, 'Round-off errors', 41, 0, '2023-02-04 22:52:03'),
(237, 'Round-off errors', 40, 0, '2023-02-04 22:52:11'),
(238, 'Total numerical error', 40, 1, '2023-02-04 22:52:11'),
(239, 'Truncation error', 40, 0, '2023-02-04 22:52:11'),
(240, 'Approximation error ', 40, 0, '2023-02-04 22:52:11'),
(245, 'Excel', 42, 1, '2023-02-04 22:53:14'),
(246, 'Matlab', 42, 0, '2023-02-04 22:53:14'),
(247, 'Mathcad', 42, 0, '2023-02-04 22:53:14'),
(248, 'Gitlab', 42, 0, '2023-02-04 22:53:14'),
(249, 'Round-off errors', 39, 0, '2023-02-04 22:58:03'),
(250, 'Total numerical error', 39, 0, '2023-02-04 22:58:03'),
(251, 'Truncation error', 39, 0, '2023-02-04 22:58:03'),
(252, 'Approximation error ', 39, 1, '2023-02-04 22:58:03');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_list`
--

DROP TABLE IF EXISTS `quiz_list`;
CREATE TABLE IF NOT EXISTS `quiz_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `qpoints` int NOT NULL DEFAULT '1',
  `user_id` int NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quiz_list`
--

INSERT INTO `quiz_list` (`id`, `title`, `qpoints`, `user_id`, `date_updated`) VALUES
(11, 'Math', 2, 2222, '2023-02-04 22:35:54'),
(12, 'Soft Engineer', 1, 1111, '2023-02-04 22:38:30');

-- --------------------------------------------------------

--
-- Table structure for table `quiz_student_list`
--

DROP TABLE IF EXISTS `quiz_student_list`;
CREATE TABLE IF NOT EXISTS `quiz_student_list` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quiz_id` int NOT NULL,
  `user_id` int NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quiz_student_list`
--

INSERT INTO `quiz_student_list` (`id`, `quiz_id`, `user_id`, `date_updated`) VALUES
(15, 11, 2211737, '2023-02-04 22:37:17'),
(16, 11, 2213543, '2023-02-04 22:37:23'),
(17, 11, 2214219, '2023-02-04 22:37:34'),
(18, 11, 2215422, '2023-02-04 22:37:40'),
(19, 12, 2211737, '2023-02-04 22:47:53'),
(20, 12, 2213543, '2023-02-04 22:47:56'),
(21, 12, 2214219, '2023-02-04 22:48:00'),
(22, 12, 2215422, '2023-02-04 22:48:04');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `level_section` varchar(100) NOT NULL,
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2215219 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `user_id`, `level_section`, `date_updated`) VALUES
(1, 2211737, 'BSCS 3', '2023-02-04 22:30:26'),
(2, 2213543, 'BSCS 3', '2023-02-04 22:31:11'),
(3, 2215422, 'BSCS 3', '2023-02-04 22:31:56'),
(4, 2214219, 'BSCS 3', '2023-02-04 22:32:09');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `user_type` tinyint(1) NOT NULL DEFAULT '1' COMMENT '1 = admin, 2= faculty , 3 = student',
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT ' 0 = incative , 1 = active',
  `date_updated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2215423 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `user_type`, `username`, `password`, `status`, `date_updated`) VALUES
(1111, 'SoftEngProf', 2, 'softeng', 'faculty', 1, '2023-02-04 22:25:40'),
(2222, 'MathProf', 2, 'math', 'faculty', 1, '2023-02-04 22:27:00'),
(2211737, 'Benedict', 3, 'Benedict', 'student', 1, '2023-02-04 22:21:14'),
(2213543, 'Fiona', 3, 'Fiona', 'student', 1, '2023-02-04 22:19:44'),
(2214219, 'Dave', 3, 'Dave', 'student', 1, '2023-02-04 22:18:13'),
(2215422, 'Kent', 3, 'Kent', 'student', 1, '2023-02-04 22:22:16');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
