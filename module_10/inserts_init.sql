INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

INSERT INTO book(book_name, author, details)
    VALUES('A Man Called Ove', 'Fredrik Backman', 'The story of a grumpy old man');

INSERT INTO book(book_name, author, details)
    VALUES('The Lost Hero', 'Rick Riordan', 'The heroes of Olympus');

INSERT INTO book(book_name, author, details)
    VALUES('Black Ice', 'Brad Thor', 'The new cold war is about to go hot');

INSERT INTO book(book_name, author, details)
    VALUES('The Book About Me', 'Andrew Lythgoe', 'The autobiography of Andrew');

INSERT INTO book(book_name, author, details)
    VALUES('The Book About You', 'Andrew Lythgoe', 'The biography of you');

INSERT INTO book(book_name, author, details)
    VALUES('The Adventures of Writing', 'Andrew Lythgoe', 'The novel of the biography of you');

INSERT INTO book(book_name, author, details)
    VALUES('Keepin Busy', 'Andrew Lythgoe', 'Struggles of a work/school/life balance');

INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'The book about life');

INSERT INTO book(book_name, author, details)
    VALUES('The Lincoln Highway', 'Armor Towles', 'A book of dreams');

INSERT INTO book(book_name, author, details)
    VALUES('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 'The most popular fantasy book out there');

INSERT INTO user(first_name, last_name) 
    VALUES('Andrew', 'Lythgoe');

INSERT INTO user(first_name, last_name)
    VALUES('Chase', 'Lythgoe');

INSERT INTO user(first_name, last_name)
    VALUES('James', 'Franco');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Andrew'), 
        (SELECT book_id FROM book WHERE book_name = 'The Lincoln Highway')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Chase'),
        (SELECT book_id FROM book WHERE book_name = 'A Man Called Ove')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'James'),
        (SELECT book_id FROM book WHERE book_name = 'Keepin Busy')
    );
