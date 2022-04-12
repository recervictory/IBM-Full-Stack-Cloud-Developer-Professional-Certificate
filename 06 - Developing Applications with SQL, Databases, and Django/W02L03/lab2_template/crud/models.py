from django.db import models
from django.utils.timezone import now

# Define your models from here:

# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length= 30,default='jhon')
    last_name = models.CharField(null=False, max_length= 30, default='doe')
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name


# Instructor model
class Instructor(User):
    full_time = models.BooleanField(default= True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return "First Name: " + self.first_name + ", " + \
                "Last Name: " + self.last_name + ", " + \
                "Is full time: " + str(self.full_time) + ", " + \
                "Total Learners :" + str(self.total_learners)

# Course Model
class Course(models.Model):
    name = models.CharField(null = False, max_length= 100, default="online course")
    description = models.CharField(max_length=500)

    # Many-to-Many relationship with Instructor
    instructor = models.ManyToManyField(Instructor)
    # Many-to-Many relationship with leaners via enrollment realtionship
    leaners = models.ManyToManyField('Learner', through= 'Enrollment')

    # Create t toString method for object sting reprentation 
    def __str__(self):
        return "Name : " + self.name + ", " + \
            "Descriptions: " + self.description


# Lesson Model
class Lesson(models.Model):
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null= True, on_delete = models.CASCADE)
    content = models.TextField()

# Learner Model
class Learner(User):
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    OCUPATION_CHOICES = [
        (STUDENT , 'student'),
        (DEVELOPER , 'developer'),
        (DATA_SCIENTIST , 'data_scientist'), 
        (DATABASE_ADMIN , 'dba')
    ]
    occupation = models.CharField(
        null= False,
        max_length= 20,
        choices= OCUPATION_CHOICES,
        default= STUDENT
    )
    social_link = models.URLField(max_length=200)

    def __str__(self):
        return "First name: " + self.first_name + ", " + \
                "Last name: " + self.last_name + ", " \
                "Date of Birth: " + str(self.dob) + ", " + \
                "Occupation: " + self.occupation + ", " + \
                "Social Link: " + self.social_link

# Enrollment model as a lookup table with additional enrollment info

class Enrollment(models.Model):
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODE = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor')
    ]
    # Add a learner foreign Key
    learner = models.ForeignKey(Learner, on_delete= models.CASCADE)

    # Add a course foreign Key
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

    # Enrollment Date
    date_enrolled = models.DateField(default=now)

    # Enrollment Mode
    mode = models.CharField( max_length=5, choices= COURSE_MODE, default= AUDIT)


