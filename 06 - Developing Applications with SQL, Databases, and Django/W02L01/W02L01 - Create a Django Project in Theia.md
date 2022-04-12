# Create Your First Django Model

**Estimated time needed:** 15 minutes

## Learning Objectives

*   Get familiar with Theia IDE and Django
*   Setup a standalone Django ORM app
*   Create your first Django project and application
*   Create and test your first Django model

# Start PostgreSQL in Theia

`PostgreSQL`, also known as `Postgres`,  is an open-source relational database management system and
it is one of the main databases Django uses.

If you are using the Theia environment hosted by [Skills Network Labs](https://labs.cognitiveclass.ai/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMCD0251ENSkillsNetwork21879158-2021-01-01),
a pre-installed PostgreSQL instance is provided for you.

You can start PostgreSQL from UI by finding the SkillsNetwork icon on the left menu bar and selecting PostgreSQL
from the DATABASES menu item:

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/start_postgres.png)

Once the PostgreSQL has been started, you can check the server connection information from the UI.
Please markdown the connection information such as generated `username`, `password`, and `host`, etc,
which will be used to configure Django app to connect to this database.

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/postgres_started.png)

*   Django needs an adapter called `Psycopg` as an interface to work with PostgreSQL, you can install it using following command:

```
pip3 install psycopg2-binary

```

{: codeblock}

Also, a `pgAdmin` instance is installed and started for you. It is a popular PostgreSQL admin and development tool for you to manage
your PostgreSQL server interactively.

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/start_pgadmin.png)

# Setup Your First Django App

First, we need to install Django related packages.

*   Go to terminal and run:

```
pip3 install Django
```

{: codeblock}

NOTE: Theia IDE may ask you to install  `pylint` for checking the syntax errors of your Python code. If you installed `pylint`,
it may generate false positive errors for source code in this lab and you could simply ignore them.

*   Run the following command-lines to download a code template for this lab.

```
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3_django_orm/lab1_template.zip"  
unzip lab1_template.zip
rm lab1_template.zip

```

{: codeblock}

You may need to press `Enter` key to run the last `rm` command.

After downloading and unzipping is done, click the `Explorer` on the left menu (the first button).

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/theia_explorer.png)

and your first Django project should look like the following:

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/lab1\_project.png)

In the created project, you could find some important project files:

*   `manage.py` is a command-line interface that allows you to interact with and manage your Django project
*   `settings.py` contains setting information about this project such as databases or installed Django apps
*   `orm` folder is a container for a standalone Django ORM app
*   `orm/models.py` contains model definitions

You will learn more details about these files in subsequent learning modules and labs.

Next let's connect our Django project to the `PostgreSQL` we started.

*   Open `settings.py` and scroll to `DATABASES` section.

```python
# Postgre SQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Place it with your password saved in Step 1',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

*   Replace the value of `PASSWORD` to be the generated `PostgreSQL` password generated in Step 1.

After that, your `settings.py` file should look like the following:

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/lab1\_orm_app.png)

*   OK now you first Django `orm` app is ready and  you can start defining your first Django model in the next step

# Define Your First Django Model

*   Open `orm/models.py` (under `lab1_template/orm/` folder ) and copy / paste the following snippet under comment

` # Define your first model from here:  ` to define a `User` model

```python
class User(models.Model):
    # CharField for user's first name
    first_name = models.CharField(null=False, max_length=30, default='john')
    # CharField for user's last name
    last_name = models.CharField(null=False, max_length=30, default='doe')
    # CharField for user's date for birth
    dob = models.DateField(null=True)

```

{: codeblock}

Now you have defined a very simple `User` model that only contains `first_name`  and `last_name` as `CharField`
and `dob` as `DateField`

# Activate the User Model

After the `User` model is defined, Django will be creating a corresponding database table
called `orm_user`. The first part `orm` is your app name and the second part `user` is the
model name.

Whenever you make changes to your models such as creating new models or modifying existing models,
you need to perform database migrations. Django provides utils via `manage.py` interface to help you perform migrations.

*   If your current working directory is not `/home/project/lab1_template`, `cd` to the project folder

```
cd lab1_template
```

{: codeblock}

*   First, you will need to generate migration scripts for `orm` app

```
python3 manage.py makemigrations orm
```

{: codeblock}

and you should see the following result in the terminal:

```
Migrations for 'orm':
  orm/migrations/0001_initial.py
    - Create model User
```

*   `orm/migrations` folder is where Django stores the changes to your models and you may wonder

what SQL statements Django has created for your model migrations. You can check the SQL statements
by running

```
python3 manage.py sqlmigrate orm 0001
```

{: codeblock}

It prints the `orm_user` table creation SQL statement for you.

```
BEGIN;
--
-- Create model User
--
CREATE TABLE "orm_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "dob" date NULL);
COMMIT;
```

In most cases, with Django Model works as ORM component, you don't need to worry about the SQL part at all. You can just
use Django Model APIs provided to query/manipulate data in databases.

*   Next, you can perform the migration to create `orm_user` table by running:

```
python3 manage.py migrate
```

{: codeblock}

Django will perform migrations for all the installed apps including `orm` app.

```
Operations to perform:
  Apply all migrations: orm
Running migrations:
  Applying orm.0001_initial... OK
```

*   Click `Launch Application` tab on the top menu and enter `5050` to open `pgAdmin`

*   Once `pgAdmin` is started in a new browser tab, choose `Skills Network` server and enter the password

generated from Step 1

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/pgadmin_password.png)

*   Then expand `Databases->posstgres->Schemas->public->Tables`, you should see the `orm_user` table created

in previous migration step.

![image](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3\_django_orm/images/pgadmin_tables.png)

# Test the Model

*   Open `test.py` and you can find a `test_setup()` method to save a mockup `user` object and try to

check if the user object was saved successfully.

*   You could run the `test.py` to test your model:

```
python3 test.py
```

{: codeblock}

and you should see

```
Django Model setup completed.
```

That's it, you have set up your first Django ORM app with first Django model.

# Summary

In this lab, you have set up your first Django project and application. You also
created and tested your first Django model.

In the next lab, you will try to create some more real Django Models and perform Create, Read, Update, and Delete (CRUD)
operations on them.

