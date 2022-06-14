SELECT * FROM hasil 
INTO OUTFILE '~/nilai/score.csv'
FIELDS TERMINATED BY ','

mysqldump -u root -p score hasil > score.xls
mysqldump -u root -p -t -T/nilai score hasil --fields-terminated-by=,