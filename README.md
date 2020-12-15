# Data_eng_prjt2
### By Nayel HAMANI & Karthikeyan PAVADE

### Requirements :
- Docker 
- docker-compose


### Installation :
- `git clone https://github.com/shunbolt/data-engineering-final-project-EFREI-Tran-Torrado.git`
- `cd data-engineering-final-project-EFREI-Tran-Torrado`

### Starting the app :
- use `docker-compose up` to start the app 
- You can then access the webapp on `http://localhost:5000`

### Running tests  :
- `python test_app.py` to test the webapp
- `python test_recommendations.py` to test the model 

### Running Grafana :
- 1st Step: Run following files 'prometheus.exe' , 'alermanager.exe' and 'windows_exporter.exe'
- 2nd Step: Verify that you can access the webapp on `http://localhost:5000` and `http://localhost:9090`
- 3rd Step: Go into 'http://localhost:3000' then access to Configuration then Data Source.
- 4th Step: Select Prometheus and write `http://localhost:9090` on The URL of HTTP that you see.
- 5th Step: Save
- 6th Step: Upload dashboard.json file into the dashboard menu
And now you can access to some beautifull process of differents metrics from our application. 
