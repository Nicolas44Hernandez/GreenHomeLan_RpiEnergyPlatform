# GreenHomeLan_RpiEnergyPlatform
Energy platform to send energy recommendations to orchestrators


1. Install nginx
2. Install docker
3. Copy nginx config 
```cd ressources```
```sudo cp nginx.conf  /etc/nginx/sites-enabled/eip-app```   
4. test nginx conf
```sudo nginx -t``` 
5. Restart nginx service
```sudo service nginx restart``` 
6. Run docker compose
```docker compose up -d```