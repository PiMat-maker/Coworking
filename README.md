# Coworking

*Project is run on Yandex Cloud*

### Project architecture
![image](https://user-images.githubusercontent.com/54264954/209219498-c7e00fbd-a3a9-42bd-9b59-7dc5a7abb206.png)  


### Use-case model
![image](https://user-images.githubusercontent.com/54264954/209219551-feb37b5e-6bf6-4a78-8588-765d6a96d5b2.png)  


### Database architecture
![image](https://user-images.githubusercontent.com/54264954/209219394-499008e0-b28b-4a09-af9b-6ddae549081d.png)  


### Deploy
To run server
`ssh -i <path-to-cloud-ssh-key> -L 8000:localhost:8000 <user>@<public-ip-container> -p 22`  

To run project
`python3 manage.py runserver`  

To connect to database  
`psql "host=c-<database-id>.rw.mdb.yandexcloud.net 
      port=<port> 
      sslmode=verify-full 
      dbname=db1 
      user=<user> 
      target_session_attrs=read-write"`
