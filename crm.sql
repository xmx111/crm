/*
Navicat MySQL Data Transfer

Source Server         : 221
Source Server Version : 50527
Source Host           : 192.168.1.221:3316
Source Database       : crm

Target Server Type    : MYSQL
Target Server Version : 50527
File Encoding         : 65001

Date: 2013-08-14 17:40:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `rainbow_custom`
-- ----------------------------
DROP TABLE IF EXISTS `rainbow_custom`;
CREATE TABLE `rainbow_custom` (
  `customId` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) DEFAULT NULL,
  `customType` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `cardid` varchar(45) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `marriage` int(11) DEFAULT NULL,
  `addr` varchar(200) DEFAULT NULL,
  `regAddr` varchar(200) DEFAULT NULL,
  `creditCardInfo` varchar(200) DEFAULT NULL,
  `linkmanInfo` varchar(400) DEFAULT NULL,
  `houseAddr` varchar(200) DEFAULT NULL,
  `company` varchar(200) DEFAULT NULL,
  `companyTel` varchar(15) DEFAULT NULL,
  `companyAttr` varchar(200) DEFAULT NULL,
  `companyDate` date DEFAULT NULL,
  `salary` float DEFAULT NULL,
  `consultTime` date DEFAULT NULL,
  `creditDate` date DEFAULT NULL,
  `repayDate` date DEFAULT NULL,
  `creditMoney` float DEFAULT NULL,
  `creditInterest` float DEFAULT NULL,
  `creditTerm` int(11) DEFAULT NULL,
  `enterTime` date DEFAULT NULL,
  `applyCompany` varchar(400) DEFAULT NULL,
  `creditCompany` varchar(400) DEFAULT NULL,
  `saveTime` datetime DEFAULT NULL,
  `notPassReazon` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`customId`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `cardid` (`cardid`),
  KEY `userId` (`userId`),
  CONSTRAINT `rainbow_custom_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `rainbow_user` (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rainbow_custom
-- ----------------------------
INSERT INTO `rainbow_custom` VALUES ('5', '1', '2', '唐翔', null, '43010219710422101x', '0', '0', '复兴街上宜园4号', null, null, null, null, '恒网网络科技有限公司', '82559732', '芙蓉南路名城1002号', '2010-05-01', '15000', '2013-07-01', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 21:45:10', null);
INSERT INTO `rainbow_custom` VALUES ('6', '1', '2', '冯常青', '15084772961', '432302197504235413', '0', '1', '长沙市岳麓区青青家园7栋411室', null, null, null, null, '长沙市天心区噫嘻饭店', '0731-85500077', '长沙市天心区新开铺街道办事处石人村14组', '2011-11-01', '100000', '2013-07-02', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 21:50:46', null);
INSERT INTO `rainbow_custom` VALUES ('7', '1', '4', '汤国煜', '13787001009', '430121197109077511', '0', '1', '雨花区第37中教工宿舍2栋106', '雨花区劳动东路115号', '最高额度1万', '老婆杨玲娟13677490318 父亲汤楚健15088485108', '雨花区雅塘冲27号5栋106', '长沙汽车工业学校', '85189017', '雨花区环科园圭白路109号', '2012-01-01', '20000', '2013-07-01', '1899-12-30', '1899-12-30', '50000', '2.45', '24', '2013-07-01', null, '平安，宜信，证大', '2013-08-07 21:57:46', null);
INSERT INTO `rainbow_custom` VALUES ('8', '1', '1', '陈芳', '13974872111', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 21:59:23', null);
INSERT INTO `rainbow_custom` VALUES ('9', '1', '0', '陈汪龙', '18073137733', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 21:59:59', null);
INSERT INTO `rainbow_custom` VALUES ('10', '1', '2', '谢明欣', '15387557798', '430403196501110514', '0', '1', '长沙市雨花区劳动东路219号长沙铜铝村有限公司宿舍楼220', null, null, null, null, '湖南家润多超市有限公司', '0731-84776211', '长沙市四方坪金帆路1191号', '2008-10-01', '8000', '2013-06-27', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:00:23', null);
INSERT INTO `rainbow_custom` VALUES ('11', '1', '0', '崔龙庆', '13787200851', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:00:46', null);
INSERT INTO `rainbow_custom` VALUES ('12', '1', '0', '方德葵', '13975112738', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:02:12', null);
INSERT INTO `rainbow_custom` VALUES ('13', '1', '0', '高峰', '13973178687', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:02:39', null);
INSERT INTO `rainbow_custom` VALUES ('14', '1', '0', '高明', '18711009494', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:03:05', null);
INSERT INTO `rainbow_custom` VALUES ('15', '1', '0', '郭梦奇', '13974871695', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:03:43', null);
INSERT INTO `rainbow_custom` VALUES ('16', '1', '0', '黄波', '13908457738', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:04:11', null);
INSERT INTO `rainbow_custom` VALUES ('17', '1', '0', '黄丽', '15874183382', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:06:05', null);
INSERT INTO `rainbow_custom` VALUES ('18', '1', '0', '黄圣莎', '15377338405', null, '1', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:06:46', null);
INSERT INTO `rainbow_custom` VALUES ('19', '1', '0', '蒋海洲', '15211049911', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:07:31', null);
INSERT INTO `rainbow_custom` VALUES ('20', '1', '0', '李龙刚', '13875809552', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:07:58', null);
INSERT INTO `rainbow_custom` VALUES ('21', '1', '0', '梁勇', '13786105966', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:08:32', null);
INSERT INTO `rainbow_custom` VALUES ('22', '1', '0', '梁超', '13467578351', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:09:06', null);
INSERT INTO `rainbow_custom` VALUES ('23', '1', '0', '刘超', '18670745322', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:09:28', null);
INSERT INTO `rainbow_custom` VALUES ('24', '1', '0', '刘晖', '15974191298', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:09:56', null);
INSERT INTO `rainbow_custom` VALUES ('25', '1', '2', '张平清', '18008476939', '431081197511066097', '0', '1', '长沙市开福区住房安置7号地12栋', null, null, null, null, '琼宇商务宾馆', '0731-82289939', '长沙市开福区住房安置7号地12栋', '2012-05-01', '17000', '2013-06-27', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:10:05', null);
INSERT INTO `rainbow_custom` VALUES ('26', '1', '0', '罗建军', '13975118096', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:10:29', null);
INSERT INTO `rainbow_custom` VALUES ('27', '1', '0', '牛丽', '13975140402', null, '1', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:12:13', null);
INSERT INTO `rainbow_custom` VALUES ('28', '1', '0', '潘双', '13787293379', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:12:43', null);
INSERT INTO `rainbow_custom` VALUES ('29', '1', '0', '彭娜', '18684688758', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:13:23', null);
INSERT INTO `rainbow_custom` VALUES ('30', '1', '0', '彭珊', '13469048750', null, '1', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:13:57', null);
INSERT INTO `rainbow_custom` VALUES ('31', '1', '0', '彭少辉', '13107490171', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:14:36', null);
INSERT INTO `rainbow_custom` VALUES ('32', '1', '0', '盛庭', '13637370337', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:15:11', null);
INSERT INTO `rainbow_custom` VALUES ('33', '1', '0', '施子珍', '13875982996', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:16:00', null);
INSERT INTO `rainbow_custom` VALUES ('34', '1', '0', '孙立强', '13875966420', null, '0', '0', null, null, null, null, null, null, null, null, '1899-12-30', null, '1899-12-30', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:17:05', null);
INSERT INTO `rainbow_custom` VALUES ('35', '1', '2', '刘建民', '13974870233', '430105196206020512', '0', '1', '长沙市芙蓉区古汉城蔬菜公司宿舍1栋2单元303房', null, null, null, null, '长沙市马王堆蔬菜食品股份有限公司', '0731-84771278', '长沙市芙蓉区嘉雨路248号', '1980-01-01', '20000', '2013-06-18', '1899-12-30', '1899-12-30', null, null, null, '1899-12-30', null, null, '2013-08-07 22:23:23', null);

-- ----------------------------
-- Table structure for `rainbow_custom_file`
-- ----------------------------
DROP TABLE IF EXISTS `rainbow_custom_file`;
CREATE TABLE `rainbow_custom_file` (
  `fileId` int(11) NOT NULL AUTO_INCREMENT,
  `customId` int(11) DEFAULT NULL,
  `fileType` int(11) DEFAULT NULL,
  `fileName` varchar(200) DEFAULT NULL,
  `filePathName` varchar(200) DEFAULT NULL,
  `saveTime` datetime DEFAULT NULL,
  PRIMARY KEY (`fileId`),
  KEY `customId` (`customId`),
  CONSTRAINT `rainbow_custom_file_ibfk_1` FOREIGN KEY (`customId`) REFERENCES `rainbow_custom` (`customId`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rainbow_custom_file
-- ----------------------------
INSERT INTO `rainbow_custom_file` VALUES ('7', '5', '0', 'IMG_20130715_145530.jpg', '8f168bb0-ff67-11e2-9902-c446195116ce.jpg', '2013-08-07 21:45:10');
INSERT INTO `rainbow_custom_file` VALUES ('9', '6', '0', 'IMG_20130702_123641.jpg', '599ab911-ff68-11e2-aac4-c446195116ce.jpg', '2013-08-07 21:50:46');
INSERT INTO `rainbow_custom_file` VALUES ('10', '7', '0', 'IMG_20130627_174920.jpg', '02504480-ff69-11e2-ad49-c446195116ce.jpg', '2013-08-07 21:57:46');
INSERT INTO `rainbow_custom_file` VALUES ('13', '10', '0', 'IMG_20130627_174906.jpg', 'b06a1f4f-ff69-11e2-9fa7-c446195116ce.jpg', '2013-08-07 22:00:23');
INSERT INTO `rainbow_custom_file` VALUES ('17', '25', '0', 'IMG_20130627_101733.jpg', '0b610f30-ff6b-11e2-887f-c446195116ce.jpg', '2013-08-07 22:10:05');
INSERT INTO `rainbow_custom_file` VALUES ('23', '35', '0', 'IMG_20130618_151256.jpg', 'e612f88f-ff6c-11e2-874c-c446195116ce.jpg', '2013-08-07 22:23:23');

-- ----------------------------
-- Table structure for `rainbow_user`
-- ----------------------------
DROP TABLE IF EXISTS `rainbow_user`;
CREATE TABLE `rainbow_user` (
  `userId` int(11) NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `secName` varchar(45) DEFAULT NULL,
  `cardid` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `birsday` date DEFAULT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `userName` (`userName`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `cardid` (`cardid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rainbow_user
-- ----------------------------
INSERT INTO `rainbow_user` VALUES ('1', '李彩娟', '97F24C13BAB4E948557DEA107C714F8A', '李彩娟', null, null, null, '1', '1986-10-08');
