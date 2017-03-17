# sudo ln -s /etc/nginx/sites-available/api.bgeo.io /etc/nginx/sites-enabled/api.bgeo.io

server {
        listen 80;
        listen [::]:80;

        server_name api.bgeo.io;
        if ($http_x_forwarded_proto = "http") {
            return 301 https://$server_name$request_uri;
        }

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/var/www/rvau-api/api.sock;
        }

        # letsencrypt well known
        location ~ /.well-known {
            allow all;
        }
}
