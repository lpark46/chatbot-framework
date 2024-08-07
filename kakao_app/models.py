from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100)
    researcher = models.CharField(max_length=100)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.team_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_contact = models.CharField(max_length=15)

    def __str__(self):
        return self.subject_name

class Test(models.Model):
    test_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name

class Visit(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    visit_date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    group_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.visit_date} - {self.time_start} - {self.subject}"
