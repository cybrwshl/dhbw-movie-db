# Movie Database

## Test data
### Export test data
To export all data from the database simply call
```
python manage.py dumpdata --output dump.json
```

### Import test data
To import all previously exported data, use this command:
```
python manage.py loaddata dump.json
```