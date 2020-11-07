DROP TABLE IF EXISTS my_movies;

CREATE TABLE my_movies
(
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT    NOT NULL UNIQUE,
    genre  TEXT    NOT NULL,
    income INTEGER NOT NULL
);

INSERT INTO my_movies
    (title, genre, income)
VALUES ('Arcobaleno selvaggio', 'Action', 600000),
       ('Colpo basso', 'Action', 63860),
       ('Dove l''erba si tinge di sangue', 'Action', 1900000),
       ('A prova di proiettile', 'Action', 807947),
       ('Race for Glory', 'Action', 100326),
       ('La legge del drago', 'Action', 35154),
       ('Air Force - Aquile d''acciaio 3', 'Action', 2517600),
       ('Da solo contro tutti', 'Action', 1152117),
       ('Jie tou sha shou', 'Action', 14569178),
       ('Tae-poong', 'Action', 139059),
       ('Redline', 'Action', 6881022),
       ('Ong Bak 2 - La nascita del dragone', 'Action', 102458),
       ('Deep Gold', 'Action', 12000),
       ('Middonaito îguru', 'Action', 7116),
       ('Shinui Han Soo: Gwisoopyeon', 'Action', 67578),
       ('L''uomo con i pugni di ferro', 'Action', 15634090),
       ('The Korean', 'Action', 20279),
       ('Ong Bak 3', 'Action', 14890),
       ('The Protector 2', 'Action', 2463),
       ('Vettai', 'Action', 204373),
       ('Rowdy Rathore', 'Action', 777373),
       ('Gabbar Is Back', 'Action', 534601),
       ('Jeonseolui joomeok', 'Action', 134213),
       ('The Reliant', 'Action', 408747),
       ('Ism', 'Action', 134165),
       ('Take Point', 'Action', 112386),
       ('Dixie y la rebelión zombi', 'Animation', 120),
       ('Back to the Jurassic', 'Animation', 4351),
       ('Kuroshitsuji: Book of the Atlantic', 'Animation', 248286),
       ('The Boxcar Children: Surprise Island', 'Animation', 78676),
       ('Chaar Sahibzaade 2: Rise of Banda Singh Bahadur', 'Animation', 700723),
       ('Le polygraphe', 'Crime', 60000),
       ('Le dernier souffle', 'Crime', 316043),
       ('Todo el poder', 'Crime', 70920),
       ('The Pardon', 'Crime', 8845),
       ('Zhui xiong zhe ye', 'Crime', 82778),
       ('Drawing Restraint 9', 'Fantasy', 234743),
       ('Barbe bleue', 'Fantasy', 33490),
       ('Cirque du Soleil - Mondi lontani', 'Fantasy', 12512862),
       ('Ga-lyeo-jin si-gan', 'Fantasy', 57759)
;
