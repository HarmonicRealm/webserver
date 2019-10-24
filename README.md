# webserver

run `python3 main.py` and it'll pop open on 127.0.0.1:5000

you can check it in browser or in python with requests

`import requests`

`rq = requests.get('http://127.0.0.1:5000/')`


`rq.content` will return 


`b"[{'id': None, 'location_id': 1, 'tdate': '2019-10-10', 'ttime': '21:02:13', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}, {'id': None, 'location_id': 1, 'tdate': '2019-10-10', 'ttime': '21:02:37', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}, {'id': None, 'location_id': 2, 'tdate': '2019-10-10', 'ttime': '21:02:43', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}, {'id': None, 'location_id': 2, 'tdate': '2019-10-10', 'ttime': '21:02:44', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}, {'id': None, 'location_id': 3, 'tdate': '2019-10-10', 'ttime': '21:02:49', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}, {'id': None, 'location_id': 3, 'tdate': '2019-10-10', 'ttime': '21:02:50', 'tph': 7, 'ttemperature': 25, 'tturbidity': 7, 'tdepth': None}]"`


