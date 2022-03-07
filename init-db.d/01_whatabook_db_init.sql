DROP USER IF EXISTS 'whatabook_user' @'localhost';

CREATE USER 'whatabook_user' @'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user' @'localhost';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user' @'%';

USE whatabook;

-- drop tables if they are present
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS store;

-- create tables for user, book, wishlist, and store
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR (75) NOT NULL,
    PRIMARY KEY(user_id)
);

CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT,
    book_name VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_user
    FOREIGN KEY(user_id) 
        REFERENCES user(user_id),
    CONSTRAINT fk_book 
    FOREIGN KEY(book_id)
        REFERENCES book(book_id)
);

CREATE TABLE store (
    store_id INT NOT NULL AUTO_INCREMENT,
    locale VARCHAR(500) NOT NULL,
    PRIMARY KEY(store_id)
);

-- insert user statement 
INSERT INTO user (first_name, last_name) VALUES 
('Scoot', 'GlizzyGang');

INSERT INTO user (first_name, last_name) VALUES
('David', 'Blaine');

INSERT INTO user (first_name, last_name) VALUES
('Leroy', 'Jenkins');

-- insert book statement
INSERT INTO book (book_name, author, details) 
VALUES ('The Grapes of Wrath','John Steinbeck','The great depression and a low income family distressed by ruthless economics');

INSERT INTO book (book_name, author, details)
VALUES ('In Search of Lost Time', 'Marcel Proust', 'Proust introduces the seven part cycle of his life');

INSERT INTO book (book_name, author, details)
VALUES ('Jane Eyre','Charlotte Bronte','First person narrative about a small, plain faced, intelligent english orphan');

INSERT INTO book (book_name, author, details)
VALUES ('Invisible Man','Ralph Ellison','Addresses many of the social and intellectual issues facing african americans');

INSERT INTO book (book_name, author, details)
VALUES ('The canterbury Tales','Geoffrey Chaucer','Astonishing tales that have become a touchstone of medieval literature');

INSERT INTO book (book_name, author, details)
VALUES ('Heart of Darkness','Joseph Conrad','A foreign assignment taken by an Englishmen from a Belgian trading company');

INSERT INTO book (book_name, author, details)
VALUES ('Talent is overrated','Geoff Colvin','Hard word beats talet');

INSERT INTO book (book_name, author, details)
VALUES ('War and Peace', 'Leo Tolstoy', 'War and peace leading up to Napoleons invasion of Russia');

INSERT INTO book (book_name, author, details)
VALUES ('Middlemarch', 'George Eliot', 'A study of provincial life');

-- insert wishlist
INSERT INTO wishlist(user_id, book_id) 
VALUES (1,1);

INSERT INTO wishlist(user_id, book_id) 
VALUES (2,1);

INSERT INTO wishlist(user_id, book_id) 
VALUES (3,1);

-- insert store into stores
INSERT INTO store(locale) VALUES ('04112 Kyiv, Ukraine');