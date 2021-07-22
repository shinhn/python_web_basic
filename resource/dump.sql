BEGIN TRANSACTION;
CREATE TABLE users(id interger primary key, username text, email text,     phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kang','rkdrpgml@naver.com','010-0000-0000','shinhn.github.io','2021-07-21 15:20:04');
INSERT INTO "users" VALUES(2,'park','park@naver.com','010-1111-1111','park.github.io','2021-07-21 15:20:04');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','010-3333-3333','Lee.github.io','2021-07-21 15:20:04');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','010-4444-4444','Cho.github.io','2021-07-21 15:20:04');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@naver.com','010-5555-5555','Yoo.github.io','2021-07-21 15:20:04');
COMMIT;
