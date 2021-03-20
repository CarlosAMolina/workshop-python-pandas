CREATE TABLE funds.profitability (
	id int unsigned NOT NULL AUTO_INCREMENT,
	`year` SMALLINT UNSIGNED NOT NULL,
	profitability DECIMAL(5,2) NULL,
	CONSTRAINT profitability_PK PRIMARY KEY (id,`year`),
	CONSTRAINT profitability_FK FOREIGN KEY (id) REFERENCES funds.name(id) ON DELETE CASCADE ON UPDATE CASCADE
);
