import string
import random
import sqlite3

#had lablasa dyel database
conn = sqlite3.connect("vegfrgame.db")
cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS scores(
               player_id INTEGER PRIMARY KEY,
               player_name Text,
               score INTEGER
               )
               ''')
conn.commit()


with open("game.txt","r")as f:
    game = f.read()
def mygame():
    print("\t *****welcome to Kamal Game*****\n")

    def roll():
        roll = random.choice('abcdefghijklmnopqrstuvwxyz')
        return roll
    while True:
        players = input("how many players will particip (1-4) : ")
        if players.isdigit():
            players = int(players) 
            if 1<= players <= 4:
                break
            else:
                print("you need to put number beetwen 1 and 4")
            
        else:
            print("invalid")



    words=[]
    start_of_word = -1
    target_start= "<"
    target_end= ">"

    for i, char in enumerate(game):
        if char == target_start:
            start_of_word = i
        if char == target_end and start_of_word != -1 :
            word = game[start_of_word: i + 1]
            words.append(word)
            start_of_word= -1




    player_score = [0 for _ in range(players)]
    answers = {}
    roll = roll()

    for player_index in range(players):
        player_name = input("whats is name of player namber : "+str(player_index+1)+" \n")
        print(player_name +':'+str(player_index+1))
        score=0
        for word in words:
            answer = input("enter a word begin with this letter " + roll +" for "+ word+" : ")
            answers[word]=answer
            if not answer or answer[0]!=roll:
                score += 0
            else:
                score += 5
            player_score[player_index]=score
        print("your score is : " ,player_score[player_index])
        cursor.execute("INSERT INTO scores (player_name, score) VALUES (?,?)",(f"{player_name}{player_index+1}",player_score[player_index]))
        conn.commit()

def table_score():
    print("\nGame scores:")
    cursor.execute("SELECT * FROM scores")
    rows=cursor.fetchall()
    for row in rows:
        print(f"{row[1]}:{row[2]}")

def play_again():
    return input("do you wanna play again? (yes/no): ").lower().startswith('y')


while True:
    mygame()
    table_score()

    if not play_again():
        print("sir t9awed")
        break


conn.close()
