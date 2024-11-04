# from datetime import datetime
# from pathlib import Path
# from decouple import config
# import subprocess
# import schedule


# DB_NAME = config('DB_NAME')
# DB_USER = config('DB_USER')
# DB_PASSWORD = config('DB_PASSWORD')
# DB_HOST = config('DB_HOST')
# DB_PORT = config('DB_PORT')

# # sudo apt-get install postgresql-client
# def backup_faith_battle_database():
#     backup_dir = Path(__file__).resolve().parent
#     file_name = f'faith_battle_users.{datetime.now().strftime("%Y_%m_%d")}'
    
#     pg_dump_command = f'pg_dump -h{DB_HOST} -U {DB_USER} -d {DB_NAME} -f {backup_file} -W {DB_PASSWORD}'
#     print(pg_dump_command)
#     subprocess.run(pg_dump_command, shell=True, check=True, env={'PGPASSWORD': DB_PASSWORD})
    
    
# # schedule.every()
# backup_faith_battle_database()