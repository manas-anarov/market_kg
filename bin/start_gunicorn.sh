#!/bin/bash
	source /home/up_pro/venv/bin/activate
	source /home/up_pro/venv/bin/postactivate
	exec gunicorn  -c "/home/up_pro/market_kg/gunicorn_config.py" un_project.wsgi


