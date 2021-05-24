-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2021-05-22 15:42:28
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
  `create_time` int(11) DEFAULT NULL,
  `assessment_id` int(11) NOT NULL,
  `type` varchar(100) NOT NULL,
  `percentage` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `cilo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `cilo`
--

CREATE TABLE `cilo` (
  `create_time` int(11) DEFAULT NULL,
  `cilo_id` int(11) NOT NULL,
  `ciloNumber` int(11) NOT NULL,
  `ciloContent` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `cilo`
--

INSERT INTO `cilo` (`create_time`, `cilo_id`, `ciloNumber`, `ciloContent`) VALUES
(1621688981, 1, 1, '12'),
(1621688981, 2, 2, '123'),
(1621689053, 3, 1, '1535432523453'),
(1621689053, 4, 2, '1342354356435436535');

-- --------------------------------------------------------

--
-- 表的结构 `cilo_precilo`
--

CREATE TABLE `cilo_precilo` (
  `create_time` int(11) DEFAULT NULL,
  `cilo_precilo_id` int(11) NOT NULL,
  `cilo_id` int(11) NOT NULL,
  `preCilo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `course`
--

CREATE TABLE `course` (
  `create_time` int(11) DEFAULT NULL,
  `course_id` int(11) NOT NULL,
  `courseName` varchar(100) NOT NULL,
  `courseCode` int(11) NOT NULL,
  `courseType` varchar(100) NOT NULL,
  `academicYear` int(11) NOT NULL,
  `programme_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course`
--

INSERT INTO `course` (`create_time`, `course_id`, `courseName`, `courseCode`, `courseType`, `academicYear`, `programme_id`) VALUES
(1621688981, 2, 'woshidashiabi', 0, 'GE', 1231, 1),
(1621689053, 3, 'woshidashiabi2', 33333, 'MJ', 1231, 1);

-- --------------------------------------------------------

--
-- 表的结构 `course_curcilo`
--

CREATE TABLE `course_curcilo` (
  `create_time` int(11) DEFAULT NULL,
  `course_curCILO_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `curCILO_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course_curcilo`
--

INSERT INTO `course_curcilo` (`create_time`, `course_curCILO_id`, `course_id`, `curCILO_id`) VALUES
(1621688981, 1, 2, 1),
(1621688981, 2, 2, 2),
(1621689053, 3, 3, 3),
(1621689053, 4, 3, 4);

-- --------------------------------------------------------

--
-- 表的结构 `course_designer`
--

CREATE TABLE `course_designer` (
  `create_time` int(11) DEFAULT NULL,
  `userName` varchar(50) NOT NULL,
  `fullName` varchar(50) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `courDes_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `course_designer`
--

INSERT INTO `course_designer` (`create_time`, `userName`, `fullName`, `type`, `programme`, `password`, `courDes_id`) VALUES
(1621243863, 'cname1', 'name1', 3, 'CST', '123', 1),
(1621243867, 'cname2', 'name2', 3, 'CST', '123', 2),
(1621243907, 'cname3', 'name3', 3, 'CST', '123', 4),
(1621243910, 'cname4', 'name4', 3, 'CST', '123', 5),
(1621243915, 'cname5', 'name5', 3, 'CST', '123', 6),
(1621243919, 'cname6', 'name6', 3, 'CST', '123', 7),
(1621243937, 'cname7', 'name7', 3, 'CST', '123', 10),
(1621243940, 'cname8', 'name8', 3, 'CST', '123', 11),
(1621243942, 'cname9', 'name9', 3, 'CST', '123', 12),
(1621243944, 'cname10', 'name10', 3, 'CST', '123', 13);

-- --------------------------------------------------------

--
-- 表的结构 `course_precourse`
--

CREATE TABLE `course_precourse` (
  `create_time` int(11) DEFAULT NULL,
  `course_preCourse_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `preCourse_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `file`
--

CREATE TABLE `file` (
  `create_time` int(11) DEFAULT NULL,
  `file_id` int(11) NOT NULL,
  `fileData` varchar(100) NOT NULL,
  `fileAddress` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `lecturer`
--

CREATE TABLE `lecturer` (
  `create_time` int(11) DEFAULT NULL,
  `userName` varchar(50) NOT NULL,
  `fullName` varchar(50) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `lec_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `programme`
--

CREATE TABLE `programme` (
  `create_time` int(11) DEFAULT NULL,
  `programme_id` int(11) NOT NULL,
  `programmeName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `programme`
--

INSERT INTO `programme` (`create_time`, `programme_id`, `programmeName`) VALUES
(12312, 1, 'cst'),
(1231, 2, 'cst2');

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE `student` (
  `create_time` int(11) DEFAULT NULL,
  `userName` varchar(50) NOT NULL,
  `fullName` varchar(50) NOT NULL,
  `type` int(11) DEFAULT NULL,
  `programme` varchar(50) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `stu_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转储表的索引
--

--
-- 表的索引 `assessment`
--
ALTER TABLE `assessment`
  ADD PRIMARY KEY (`assessment_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `cilo_id` (`cilo_id`);

--
-- 表的索引 `cilo`
--
ALTER TABLE `cilo`
  ADD PRIMARY KEY (`cilo_id`);

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
-- 表的索引 `course_curcilo`
--
ALTER TABLE `course_curcilo`
  ADD PRIMARY KEY (`course_curCILO_id`),
  ADD KEY `course_id` (`course_id`),
  ADD KEY `curCILO_id` (`curCILO_id`);

--
-- 表的索引 `course_designer`
--
ALTER TABLE `course_designer`
  ADD PRIMARY KEY (`courDes_id`),
  ADD UNIQUE KEY `userName` (`userName`);

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
-- 表的索引 `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`lec_id`),
  ADD UNIQUE KEY `userName` (`userName`);

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
  ADD UNIQUE KEY `userName` (`userName`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `assessment`
--
ALTER TABLE `assessment`
  MODIFY `assessment_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `cilo`
--
ALTER TABLE `cilo`
  MODIFY `cilo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `cilo_precilo`
--
ALTER TABLE `cilo_precilo`
  MODIFY `cilo_precilo_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- 使用表AUTO_INCREMENT `course_curcilo`
--
ALTER TABLE `course_curcilo`
  MODIFY `course_curCILO_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `course_designer`
--
ALTER TABLE `course_designer`
  MODIFY `courDes_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用表AUTO_INCREMENT `course_precourse`
--
ALTER TABLE `course_precourse`
  MODIFY `course_preCourse_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `file`
--
ALTER TABLE `file`
  MODIFY `file_id` int(11) NOT NULL AUTO_INCREMENT;

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
  MODIFY `stu_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 限制导出的表
--

--
-- 限制表 `assessment`
--
ALTER TABLE `assessment`
  ADD CONSTRAINT `assessment_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `assessment_ibfk_2` FOREIGN KEY (`cilo_id`) REFERENCES `cilo` (`cilo_id`);

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
-- 限制表 `course_curcilo`
--
ALTER TABLE `course_curcilo`
  ADD CONSTRAINT `course_curcilo_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_curcilo_ibfk_2` FOREIGN KEY (`curCILO_id`) REFERENCES `cilo` (`cilo_id`);

--
-- 限制表 `course_precourse`
--
ALTER TABLE `course_precourse`
  ADD CONSTRAINT `course_precourse_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_precourse_ibfk_2` FOREIGN KEY (`preCourse_id`) REFERENCES `course` (`course_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
