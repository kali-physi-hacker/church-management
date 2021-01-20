# Church Management App

### Contribution Guidelines
1. Fork this repository to get a local copy of this repo in your repo
2. Clone your local copy
3. Set up the **upstream** push and pull link
4. Start working on a feature


#### Setting up the upstream push and pull link 
- After cloning this project, get the project's main link (not your local copy) which is **implicitly**: https://github.com/kali-physi-hacker/church-management.git
- open your terminal and navigate to the projects root
- Type and enter: `git remote add upstream https://github.com/kali-physi-hacker/church-management.git`

After performing the steps above, you now have the **project's main link** that you can push and pull from   
You can verify that by executing `git remote -v`

#### Working on a feature
- Check [**Asana**](https://app.asana.com/0/1199627043122142/list), our project management platform  
- pick an available task and assign it to yourself   
- next thing to do is to **create a new branch from the master branch**  
- the name of this new branch should be descriptive to the title of the task.   
- For instance if the task is *implementing authentication*, then the branch name
is going to be `desmond-implementing-authentication`, where **desmond** is the name of 
the person implementing the feature
  
#### Command Guides
1. Clone a project --> `git clone [the-project-link]`
2. Create a branch --> `git checkout -b [branch-name]`
3. Pulling **master** branch changes --> `git pull upstream master`

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