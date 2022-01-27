# soil_app

a website for the university which specialized to learn soil

# systemd [django]  soil.service

```
[Unit]
Description=Gunicorn daemon for Soil
After=network.target

[Service]
User=user
Group=user
WorkingDirectory=/home/user/soil_app
ExecStart=/home/user/soil_app/venv/bin/gunicorn --access-logfile - --workers 5 --bind 0.0.0.0:8001  soil.wsgi:application
Restart=always
SyslogIdentifier=gunicorn

[Install]
WantedBy=multi-user.target
```

___

# nginx  [django] soil

```
server {
    listen 8001;

    client_max_body_size 100M;
    server_name 62.209.128.34 www.62.209.128.34;

    # keepalive_timeout 5;
    location = /favicon.ico { access_log off; log_not_found off; }

    # Your Django project's media files - amend as required
    location /media  {
        alias /home/user/soil_app/media;
    }

    # your Django project's static files - amend as required
    location /static {
        alias /home/user/soil_app/static;
    }

    location / {
        include proxy_params;
        proxy_pass http://0.0.0.0:8001;
    }
}
```