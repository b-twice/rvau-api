# sudo vim /etc/nginx/sites-available/api.brianbrown.dev
# sudo ln -s /etc/nginx/sites-available/api.brianbrown.dev /etc/nginx/sites-enabled/api.brianbrown.dev

server {
        listen 80;
        listen [::]:80;

        server_name api.brianbrown.dev;
	return 301 https://$server_name$request_uri;
}
server {
    	listen 443 ssl http2;
    	listen [::]:443 ssl http2;
    	include snippets/ssl-brianbrown.dev.conf;
    	include snippets/ssl-params.conf;
	
	server_name api.brianbrown.dev;

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/var/www/rvau-api/api.sock;
        }

        # letsencrypt well known
        location ~ /.well-known {
            allow all;
            root /var/www/rvau-api;
        }
}

