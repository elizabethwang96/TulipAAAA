-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2021-05-27 10:52:45
-- 服务器版本： 10.4.19-MariaDB
-- PHP 版本： 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `tulipdb`
--

-- --------------------------------------------------------

--
-- 表的结构 `assessment`
--

CREATE TABLE `assessment` (
  `assessment_id` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `assessment`
--

INSERT INTO `assessment` (`assessment_id`, `type`, `course_id`) VALUES
(1, 'quiz', 2),
(2, 'asdf', 3),
(3, 'asdf', 3),
(4, 'asdf', 3),
(5, 'asdf', 3),
(6, 'asdf', 4),
(7, 'asdf', 4),
(8, 'asdf', 4),
(9, 'asdfkljhl', 4),
(10, 'asdf', 4),
(11, 'asdf', 4),
(12, 'qweer', 4),
(13, 'asdf', 4),
(14, 'qweer', 4),
(15, 'asdassda', 4),
(16, '123', 4),
(17, 'asdf', 4),
(18, 'saaas', 6),
(19, 'saaas', 6),
(20, 'ASD', 6),
(21, 'hahaha7', 7),
(22, 'hahaha7', 7),
(23, 'asd', 7),
(24, 'asdsa', 7),
(25, 'asdkfjh', 7),
(26, 'asdkfjh', 7),
(27, 'asda', 7),
(28, 'asda', 7),
(29, 'quiz', 7),
(30, 'hello', 2),
(31, 'hello', 2),
(32, 'hello', 2),
(33, 'hahah', 2),
(34, 'hahah', 2),
(35, 'hahah', 2),
(36, '去你他妈的', 2),
(37, '去念你', 2),
(38, '去念你', 2),
(39, 'hahah', 7),
(40, 'hahah', 7),
(41, 'hahah', 7),
(42, 'halo', 8),
(43, 'halo', 8),
(44, 'halo', 8),
(45, 'workshop', 8),
(46, 'worrpshop1', 8),
(47, 'worrpshop1', 8),
(48, 'sdhajskd', 8),
(49, 'sdhajskd', 8),
(50, 'sdhajskd', 8),
(51, 'qunimamabni', 8),
(52, 'qunimamabni', 8),
(53, 'qunimamabni', 8),
(54, 'qunimamabni', 8),
(55, 'qunimamabni', 8),
(56, 'qunimamabni', 8),
(57, 'qunimamabni', 8),
(58, 'assi', 8),
(59, 'assi', 8),
(60, 'qunimamabi', 8),
(61, 'qunimamabi', 8),
(62, 'qunimamabi', 8),
(63, 'haha', 8);

-- --------------------------------------------------------

--
-- 表的结构 `assessment_cilo`
--

CREATE TABLE `assessment_cilo` (
  `assessment_cilo_id` int(11) NOT NULL,
  `assessment_id` int(11) NOT NULL,
  `cilo_id` int(11) NOT NULL,
  `percentage` int(11) NOT NULL,
  `numOfCilos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `assessment_cilo`
--

INSERT INTO `assessment_cilo` (`assessment_cilo_id`, `assessment_id`, `cilo_id`, `percentage`, `numOfCilos`) VALUES
(1, 1, 3, 50, 1),
(2, 1, 4, 50, 1),
(3, 2, 5, 15, 1),
(4, 2, 6, 15, 1),
(5, 3, 6, 70, 1),
(6, 4, 5, 15, 1),
(7, 4, 6, 15, 1),
(8, 5, 6, 70, 1),
(9, 6, 8, 50, 1),
(10, 6, 9, 50, 1),
(11, 7, 8, 50, 1),
(12, 7, 9, 50, 1),
(13, 8, 8, 50, 1),
(14, 8, 9, 50, 1),
(15, 9, 8, 100, 1),
(16, 10, 8, 50, 1),
(17, 10, 9, 50, 1),
(18, 11, 8, 40, 1),
(19, 11, 9, 40, 1),
(20, 12, 8, 10, 1),
(21, 12, 9, 10, 1),
(22, 13, 8, 40, 1),
(23, 13, 9, 40, 1),
(24, 14, 8, 10, 1),
(25, 14, 9, 10, 1),
(26, 15, 8, 100, 1),
(27, 16, 8, 100, 1),
(28, 17, 8, 100, 1),
(29, 18, 10, 100, 1),
(30, 19, 10, 100, 1),
(31, 20, 10, 100, 1),
(32, 21, 12, 100, 1),
(33, 22, 12, 100, 1),
(34, 23, 12, 100, 1),
(35, 24, 12, 100, 1),
(36, 25, 12, 100, 1),
(37, 26, 12, 100, 1),
(38, 27, 12, 100, 1),
(39, 28, 12, 100, 1),
(40, 29, 12, 100, 1),
(42, 32, 3, 100, 1),
(43, 33, 3, 100, 1),
(44, 34, 3, 100, 1),
(45, 35, 3, 100, 1),
(46, 36, 3, 100, 1),
(47, 37, 3, 100, 1),
(48, 38, 3, 100, 1),
(49, 39, 12, 100, 1),
(50, 40, 12, 100, 1),
(51, 41, 12, 100, 1),
(52, 42, 14, 100, 1),
(53, 43, 14, 100, 1),
(54, 44, 14, 100, 1),
(55, 45, 14, 100, 1),
(56, 46, 14, 100, 1),
(57, 47, 14, 100, 1),
(58, 48, 14, 100, 1),
(59, 49, 14, 100, 1),
(60, 50, 14, 100, 1),
(61, 51, 14, 100, 1),
(62, 52, 14, 100, 1),
(63, 53, 14, 100, 1),
(64, 54, 14, 100, 1),
(65, 55, 14, 100, 1),
(66, 56, 14, 100, 1),
(67, 57, 14, 100, 1),
(68, 58, 14, 100, 1),
(69, 59, 14, 100, 1),
(70, 60, 14, 100, 1),
(71, 61, 14, 100, 1),
(72, 62, 14, 100, 1),
(73, 63, 14, 100, 1);

-- --------------------------------------------------------

--
-- 表的结构 `cilo`
--

CREATE TABLE `cilo` (
  `cilo_id` int(11) NOT NULL,
  `ciloNumber` int(11) NOT NULL,
  `ciloContent` varchar(100) NOT NULL,
  `course_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `cilo`
--

INSERT INTO `cilo` (`cilo_id`, `ciloNumber`, `ciloContent`, `course_id`) VALUES
(1, 1, 'hh', 1),
(2, 2, 'xx', 1),
(3, 1, 'cilo111', 2),
(4, 2, 'cilo222', 2),
(5, 1, 'asdf', 3),
(6, 2, 'asdf', 3),
(7, 3, 'asdf', 3),
(8, 1, 'asd', 4),
(9, 2, 'asd', 4),
(10, 1, 'asd', 6),
(11, 2, 'asd', 6),
(12, 1, 'askjdfh', 7),
(13, 2, 'askjdhk', 7),
(14, 1, 'DHGF', 8),
(15, 2, 'FGJHK', 8);

-- --------------------------------------------------------

--
-- 表的结构 `cilo_precilo`
--

CREATE TABLE `cilo_precilo` (
  `cilo_precilo_id` int(11) NOT NULL,
  `cilo_id` int(11) NOT NULL,
  `preCilo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `cilo_precilo`
--

INSERT INTO `cilo_precilo` (`cilo_precilo_id`, `cilo_id`, `preCilo_id`) VALUES
(1, 5, 1);

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `courseName` varchar(100) NOT NULL,
  `courseCode` int(11) NOT NULL,
  `courseType` varchar(100) NOT NULL,
  `academicYear` int(11) NOT NULL,
  `programme_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`course_id`, `courseName`, `courseCode`, `courseType`, `academicYear`, `programme_id`) VALUES
(1, 'c language', 7788, 'MJ', 1231, 1),
(2, 'java', 2020, 'MJ', 1231, 2),
(3, 'data mining', 123, 'MJ', 1231, 2),
(4, 'woshidashiabi', 2020202, 'MJ', 1231, 2),
(6, 'data mining123', 11, 'MJ', 1231, 2),
(7, 'woshidashiabi2', 12, 'MJ', 1231, 2),
(8, 'data mining123', 1111, 'MJ', 1231, 2);

-- --------------------------------------------------------

--
-- 表的结构 `coursedesigner`
--

CREATE TABLE `coursedesigner` (
  `courDes_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `coursedesigner`
--

INSERT INTO `coursedesigner` (`courDes_id`, `user_id`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `course_precourse`
--

CREATE TABLE `course_precourse` (
  `course_preCourse_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `preCourse_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course_precourse`
--

INSERT INTO `course_precourse` (`course_preCourse_id`, `course_id`, `preCourse_id`) VALUES
(1, 3, 1);

-- --------------------------------------------------------

--
-- 表的结构 `file`
--

CREATE TABLE `file` (
  `file_id` int(11) NOT NULL,
  `fileData` varchar(100) NOT NULL,
  `fileAddress` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `gradereport`
--

CREATE TABLE `gradereport` (
  `id` int(11) NOT NULL,
  `grade` int(11) NOT NULL,
  `stu_id` int(11) NOT NULL,
  `assessment_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `lecturer`
--

CREATE TABLE `lecturer` (
  `lec_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `programme`
--

CREATE TABLE `programme` (
  `programme_id` int(11) NOT NULL,
  `programmeName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `programme`
--

INSERT INTO `programme` (`programme_id`, `programmeName`) VALUES
(1, 'cst'),
(2, 'ds');

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE `student` (
  `stu_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`stu_id`, `user_id`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `fullName` varchar(50) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `programme_id` int(11) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`user_id`, `userName`, `fullName`, `type`, `programme_id`, `password`) VALUES
(1, 'cname1', 'asd', 3, 1, '123'),
(2, 'sname1', 'asdd', 1, 1, '123');

--
-- 转储表的索引
--

--
-- 表的索引 `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`assessment_id`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `assessment_cilo`
--
ALTER TABLE `assessment_cilo`
  ADD PRIMARY KEY (`assessment_cilo_id`),
  ADD KEY `assessment_id` (`assessment_id`),
  ADD KEY `cilo_id` (`cilo_id`);

--
-- 表的索引 `cilo`
--
ALTER TABLE `cilo`
  ADD PRIMARY KEY (`cilo_id`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `cilo_precilo`
--
ALTER TABLE `cilo_precilo`
  ADD PRIMARY KEY (`cilo_precilo_id`),
  ADD KEY `cilo_id` (`cilo_id`),
  ADD KEY `preCilo_id` (`preCilo_id`);

--
-- 表的索引 `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD UNIQUE KEY `courseCode` (`courseCode`),
  ADD KEY `programme_id` (`programme_id`);

--
-- 表的索引 `coursedesigner`
--
ALTER TABLE `coursedesigner`
  ADD PRIMARY KEY (`courDes_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 表的索引 `course_precourse`
--
ALTER TABLE `course_precourse`
  ADD PRIMARY KEY (`course_preCourse_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `preCourse_id` (`preCourse_id`);

--
-- 表的索引 `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`file_id`);

--
-- 表的索引 `gradereport`
--
ALTER TABLE `gradereport`
  ADD PRIMARY KEY (`id`),
  ADD KEY `stu_id` (`stu_id`),
  ADD KEY `assessment_id` (`assessment_id`),
  ADD KEY `course_id` (`course_id`);

--
-- 表的索引 `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`lec_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 表的索引 `programme`
--
ALTER TABLE `programme`
  ADD PRIMARY KEY (`programme_id`,`programmeName`),
  ADD UNIQUE KEY `programmeName` (`programmeName`);

--
-- 表的索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`stu_id`),
  ADD KEY `user_id` (`user_id`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `userName` (`userName`),
  ADD KEY `programme_id` (`programme_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `assessment`
--
ALTER TABLE `assessment`
  MODIFY `assessment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- 使用表AUTO_INCREMENT `assessment_cilo`
--
ALTER TABLE `assessment_cilo`
  MODIFY `assessment_cilo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- 使用表AUTO_INCREMENT `cilo`
--
ALTER TABLE `cilo`
  MODIFY `cilo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- 使用表AUTO_INCREMENT `cilo_precilo`
--
ALTER TABLE `cilo_precilo`
  MODIFY `cilo_precilo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- 使用表AUTO_INCREMENT `coursedesigner`
--
ALTER TABLE `coursedesigner`
  MODIFY `courDes_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `course_precourse`
--
ALTER TABLE `course_precourse`
  MODIFY `course_preCourse_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `file`
--
ALTER TABLE `file`
  MODIFY `file_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `gradereport`
--
ALTER TABLE `gradereport`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `lec_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `programme`
--
ALTER TABLE `programme`
  MODIFY `programme_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `student`
--
ALTER TABLE `student`
  MODIFY `stu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 限制导出的表
--

--
-- 限制表 `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- 限制表 `assessment_cilo`
--
ALTER TABLE `assessment_cilo`
  ADD CONSTRAINT `assessment_cilo_ibfk_1` FOREIGN KEY (`assessment_id`) REFERENCES `assessment` (`assessment_id`),
  ADD CONSTRAINT `assessment_cilo_ibfk_2` FOREIGN KEY (`cilo_id`) REFERENCES `cilo` (`cilo_id`);

--
-- 限制表 `cilo`
--
ALTER TABLE `cilo`
  ADD CONSTRAINT `cilo_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- 限制表 `cilo_precilo`
--
ALTER TABLE `cilo_precilo`
  ADD CONSTRAINT `cilo_precilo_ibfk_1` FOREIGN KEY (`cilo_id`) REFERENCES `cilo` (`cilo_id`),
  ADD CONSTRAINT `cilo_precilo_ibfk_2` FOREIGN KEY (`preCilo_id`) REFERENCES `cilo` (`cilo_id`);

--
-- 限制表 `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`programme_id`) REFERENCES `programme` (`programme_id`);

--
-- 限制表 `coursedesigner`
--
ALTER TABLE `coursedesigner`
  ADD CONSTRAINT `coursedesigner_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- 限制表 `course_precourse`
--
ALTER TABLE `course_precourse`
  ADD CONSTRAINT `course_precourse_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_precourse_ibfk_2` FOREIGN KEY (`preCourse_id`) REFERENCES `course` (`course_id`);

--
-- 限制表 `gradereport`
--
ALTER TABLE `gradereport`
  ADD CONSTRAINT `gradereport_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`),
  ADD CONSTRAINT `gradereport_ibfk_2` FOREIGN KEY (`assessment_id`) REFERENCES `assessment` (`assessment_id`),
  ADD CONSTRAINT `gradereport_ibfk_3` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- 限制表 `lecturer`
--
ALTER TABLE `lecturer`
  ADD CONSTRAINT `lecturer_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- 限制表 `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- 限制表 `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`programme_id`) REFERENCES `programme` (`programme_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
