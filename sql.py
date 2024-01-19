import sqlite3

def create_table_agents():
    con = sqlite3.connect('money_bot.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS agents(id INTEGER PRIMARY KEY, `agent_id` VARCHAR(20))")

    cur.close()
    con.close()


def create_table_passwords():
    con = sqlite3.connect('money_bot.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS passwords(id INTEGER PRIMARY KEY, `password` VARCHAR(20))")

    cur.close()
    con.close()


def create_table_files():
    con = sqlite3.connect('money_bot.db')
    cur = con.cursor()   

    cur.execute("CREATE TABLE IF NOT EXISTS files(id INTEGER PRIMARY KEY, `req_id` VARCHAR(20), `file_id` VARCHAR(250), `file_name` VARCHAR(2048), `type` VARCHAR(20))")

    cur.close()
    con.close()


def create_table_requests():
    con = sqlite3.connect('money_bot.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS requests(req_id INTEGER PRIMARY KEY, `user_id` VARCHAR(20), `req_status` VARCHAR(20))")

    cur.close()
    con.close()


def create_table_messages():
    con = sqlite3.connect('money_bot.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, `req_id` VARCHAR(20), `message` VARCHAR(4096), `user_status` VARCHAR(20), `date` VARCHAR(50))")

    cur.close()
    con.close()



create_table_agents()
create_table_passwords()
create_table_files()
create_table_requests()
create_table_messages()