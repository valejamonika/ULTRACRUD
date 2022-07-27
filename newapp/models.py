from django.db import models

class Employee(models.Model):
    designation_choices=(
        ("Software Engineer","Software Engineer"),
        ("Quality Analyst","Quality Analyst"),
        ("Product Manager","Product Manager")
    )
    fname =  models.CharField(max_length=100,verbose_name="First Name",blank=True,null=True)
    lname = models.CharField(max_length=100,verbose_name="Last Name",blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True,verbose_name="Age")
    salary = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    email = models.EmailField(verbose_name="Email",blank=True,null=True)
    joining_date = models.DateField(verbose_name="Joining Date",blank=True,null=True)
    designation = models.CharField(max_length=100,verbose_name="Designation",choices=designation_choices,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
    
    def __str__(self) -> str:
        return str(self.fname +" "+self.lname)
    
class Task(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)  #  many to one
    attendance = models.BooleanField(default=False,verbose_name="Task Attendent")
    title = models.CharField(max_length=100,verbose_name="Title",blank=True,null=True)
    task = models.TextField(blank=True,null=True,verbose_name="task")
    dead_line = models.DateField(blank=True,null=True,verbose_name="Last Date Of Submission")
    timestamp = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return str(self.employee.fname +"-"+"Task Title-"+self.title)
