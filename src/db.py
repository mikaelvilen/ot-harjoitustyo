import sqlite3

def init_database():
    conn = sqlite3.connect('highscores.db')
    conn.execute('''
        DROP TABLE IF EXISTS HIGH_SCORES''')
    conn.execute('''CREATE TABLE HIGH_SCORES
        (NAME TEXT NOT NULL,
        SCORE INT NOT NULL)''')
    conn.commit()
    conn.close()

def set_sample_scores():
    conn = sqlite3.connect('highscores.db')
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES ('random9000', 9000)")
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES ('xyz', 8000)")
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES ('asd', 5000)")
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES ('qwerty', 4000)")
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES ('555', 100)")
    conn.commit()
    conn.close()

def get_scores():
    conn = sqlite3.connect('highscores.db')
    cursor = conn.execute("SELECT * FROM HIGH_SCORES ORDER BY SCORE DESC LIMIT 5")
    high_scores = []
    for row in cursor:
        high_scores.append((row[0], row[1]))
    return high_scores

def set_new_score(name, score):
    conn = sqlite3.connect('highscores.db')
    conn.execute("INSERT INTO HIGH_SCORES (NAME, SCORE) \
        VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
