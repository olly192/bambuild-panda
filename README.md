# BamBuild Panda
Backend service for BamBuild

## Database Migrations
To run database migrations, run the following command:
```bash
$ flask --app app:app db migrate
```
```bash
$ flask --app app:app db upgrade
```
https://flask-migrate.readthedocs.io/en/latest/


## Storing Images
```python
user = User()
user.profile = request.files['fileimg'].read()
```
https://stackoverflow.com/a/42300920
