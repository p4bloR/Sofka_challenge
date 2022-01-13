import sqlite3

class Model:
    def __init__(self):
        print("")
        self.connection = sqlite3.connect('Trivia.db')
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.fill_tables()
        self.save_and_close()
        #self.run()

    def connect(self):
        self.connection = sqlite3.connect('Trivia.db')
        self.cursor = self.connection.cursor()

    def save_and_close(self):
        self.connection.commit()
        self.connection.close()


    def run(self):
        self.create_tables()
        #self.fill_tables()

    def create_tables(self):
        # create player scoreboard table
        command1 = "CREATE TABLE IF NOT EXISTS scoreboard(datetime TINYTEXT PRIMARY KEY, score INT, name CHAR(10))"
        command2 = "CREATE TABLE IF NOT EXISTS questions(sentence TINYTEXT PRIMARY KEY, categories TINYTEXT, difficulty INTEGER, answer TINYTEXT, option1 TINYTEXT, option2 TINYTEXT, option3 TINYTEXT)"

        self.cursor.execute(command1)
        self.cursor.execute(command2)

    def fill_tables(self):

        self.cursor.execute("""INSERT OR IGNORE INTO questions VALUES ('Which event triggered World War One?', 'History', 1 , "The assassination of Archduke Franci's Ferdinand", "Germany's invasion of Poland", 'The sinking of the Lusitania', "The tsar's refusal of an offer to visit Germany")""")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('World War 1 began in the year...', 'History', 2, '1914', '1945', '1939', '1918')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('Where was the Mayan civilization based?', 'History', 3, 'Around the Yucatan peninsula', 'Peru', 'Chile', 'California')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('Napoleon died during The Battle of Waterloo on June 22....', 'History', 4, '1815', '1701', '1764', '1890')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('Where was the Metric System developed?', 'History', 5, 'France', 'Ancient Greece', 'Italy', 'United States')")

        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('After how many Year’s FIFA World Cup is held?', 'sports', 1, '4 years', '2 years', '3 years', 'every year')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('In what country did the 1930 FIFA World Cup took place', 'sports', 2, 'Uruguay', 'Spain', 'France', 'Brazil')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('Which Sport is Performed by the Legend “Muhammad Ali”?', 'sports', 3, 'Boxing', 'Swiming', 'Weight lifing', 'Shooting')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('When did Cristiano Ronaldo join Juventus Football Club?', 'sports', 4, '2018', '2017', '2016', '2019' )")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('How many FIFA World Cup has been played till 2018?', 'sports', 5, '21', '29', '54', '14')")

        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What was the first commercially successful video game?', 'Videogames', 1, 'Pong', 'Mario bros', 'Pac-Man', 'Sonic')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What is the best selling videogame of all time?', 'Videogames', 2, 'Minecraft', 'Halo 1', 'Mario Bros', 'Fortnite')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What is the highest-selling gaming console to date?', 'Videogames', 3, 'Play Station 2', 'Nintendo wii', 'SNES', 'Xbox')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What video game company collaborated with SONY on the Playstation?', 'Videogames', 4, 'Nintendo', 'Sega', 'Microsoft', 'Apple')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What year was Nintendo founded?', 'Videogames', 5, '1889', '1990', '1985', '1978')")

        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('In chemistry, what element is represented by the symbol C?', 'Science', 1, 'Carbon', 'Calcium', 'Copper', 'Chlorine')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('How many elements are listed on the periodic table?', 'Science', 2, '118', '130', '101', '105')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('How many more bones do babies have than adults in the human body?', 'Science', 3, '100', 'None', '10', '150')")
        self.cursor.execute("""INSERT OR IGNORE INTO questions VALUES ("What's the hottest planet in our solar system?", "Science", 4, 'Venus', 'Mars', 'Mercury', 'Saturn')""")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What is the largest planet in our current solar system?', 'Science', 5, 'Jupiter', 'Saturn', 'Uranus', 'Neptune')")

        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What is it called when an actor breaks character to directly address the audience?', 'Cinema', 1, 'Breaking the 4th wall', 'Bending the narrative', 'Sweeping the rug', 'Following the loose thread')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('Which of the following is filmmaker Michael Bay known for?', 'Cinema', 2, 'Explosions', 'Romantic comedy', 'Fanciful costume design', 'Sweeping Western landscapes')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('In the movie Frozen, who is Olaf?', 'Cinema', 3, 'A snowman', 'A reindeer', 'a knight', 'a ghost')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('For which of these movies did Leonardo DiCaprio win an Oscar for Best Actor?', 'Cinema', 4, 'The Revenant', 'Titanic', 'Blood Diamond', 'The Wolf of Wall Street')")
        self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('What was the first movie in the Marvel Cinematic Universe?', 'Cinema', 5, 'Iron Man', 'Batman', 'The Flash', 'Captain America')")

        #self.cursor.execute("INSERT OR IGNORE INTO questions VALUES ('History', '¿En cual año terminó la segunda guerra mundial?', '1945', '1939', '1914', '1918')")

    def get_random_question(self, categories = "*", difficulty = 1, quantity = 1):
        self.connection = sqlite3.connect('Trivia.db')
        self.cursor = self.connection.cursor()
        #command = """select * from questions where categories == ? and difficulty == ? order by random() limit ?"""
        command = "select * from questions where categories = '" + categories + "' and difficulty = " + str(difficulty) + " order by random() limit " + str(int(quantity))
        #args = [categories,difficulty,quantity]
        #self.cursor.execute(command, (args))
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data


    def save_player_data(self, data):
        self.connect()
        command = "INSERT INTO scoreboard VALUES ('" + data[0] + "', '" + data[1] + "', '" + data[2]  + "')"
        self.cursor.execute(command)
        self.save_and_close()

    def get_all_rows(self, table):
        string = "SELECT * FROM " + table
        self.cursor.execute(string)
        data = self.cursor.fetchall()
        return data

    def get_scoreboard(self):
        self.connect()
        data = self.get_all_rows("scoreboard")
        self.connection.close()

        return data
