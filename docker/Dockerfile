FROM python:3

WORKDIR /usr/src/geo_classifier

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
#docker run -it --rm --name python-script -v /home/manueljmorillo/environment/proyectos/VIDEOS-TURASA/geo_classifier:/usr/geo_classifier -v /home/manueljmorillo/environment/proyectos/SIGC/entregas/Mapea4/mapea-js/src/facade/js:/opt/volume/files -w /usr/geo_classifier geo/classifier python -B src/read_files.py
#docker run -it --rm --name python-script -v /home/manueljmorillo/environment/proyectos/VIDEOS-TURASA/geo_classifier:/usr/geo_classifier -v /media/manueljmorillo/My\ Passport/:/opt/volume/files -w /usr/geo_classifier geo/classifier python -B src/classify_files.py
