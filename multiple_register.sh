python main.py 05:46:45 06:00:00 --id .\id_info\a8ching.yml &
python main.py 05:46:45 06:00:00 --id .\id_info\futsai.yml &
python main.py 05:46:45 06:00:00 --id .\id_info\a8ching.yml --delay -0.5 &
python main.py 05:46:45 06:00:00 --id .\id_info\futsai.yml --delay -0.5 &
python wait_from_website_time.py 05:45:00 05:59:55 &
python wait_from_website_time.py 05:45:00 05:59:55 --delay 0.5 &
wait
