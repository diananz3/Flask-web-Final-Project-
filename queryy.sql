CREATE TABLE hasil AS SELECT nilai.id_siswa, nilai.nama, nilai.nrp,
MAX(CASE WHEN nilai.id_mapel=1 THEN nilai.score ELSE 0
END) AS "fisika",
MAX(CASE WHEN nilai.id_mapel=2 THEN nilai.score ELSE 0
END) AS "kimia",
MAX(CASE WHEN nilai.id_mapel=3 THEN nilai.score ELSE 0
END) AS "matematika",
MAX(CASE WHEN nilai.id_mapel=4 THEN nilai.score ELSE 0
END) AS "biologi",
MAX(CASE WHEN nilai.id_mapel=5 THEN nilai.score ELSE 0
END) AS "agama",
MAX(CASE WHEN nilai.id_mapel=6 THEN nilai.score ELSE 0
END) AS "indonesia",
MAX(CASE WHEN nilai.id_mapel=7 THEN nilai.score ELSE 0
END) AS "inggris"
FROM nilai 
GROUP BY nilai.id_siswa;
