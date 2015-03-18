DROP TABLE tracks;

CREATE TABLE IF NOT EXISTS `tracks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `location` point NOT NULL ,
  `elevation` double DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;
-- ENGINE=InnoDB 
-- ALTER TABLE tracks ADD SPATIAL INDEX(location);