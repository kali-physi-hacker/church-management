# Church Management App

### Features (atm)
1. Entry of church member details (ADD)
2. Update of church member details (UPDATE)
3. View Church Members
4. View Single Church Member Details
5. Delete a church member
6. Add member ministries

### Setup and Configurations

#### Environment Setup 
##### 1. Backend - Python Virtualenv in bash

1. `python3 -m virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirments.txt`

##### 2. Frontend - React (JS) in bash
1. `npm install`

#### Running Server (Backend)
**note: From the project root**
```bash
cd backend
python manage.py runserver --settings=church_management.settings_dev
```

#### Running Server (Frontend)
**note: From the project root**
```bash
cd frontend
npm run dev
```