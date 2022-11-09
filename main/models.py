from django.db import models

# Create a Database Object with Attribute
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    def __str__(self):
        return self.text
class User (models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=255)
    age = models.IntegerField
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Questions (models.Model):
    id = models.IntegerField
    form_id = models.IntegerField
    field_type = models.CharField(max_length=255)
    text = models.CharField(max_length=300)
    def __str__(self):
        return self.id
class Answers (models.Model):
    id = models.IntegerField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=300)
    def __str__(self):
        return self.id
class Report (models.Model):
    id = models.IntegerField
    type = models.CharField(max_length=255)
    answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    def __str__(self):
        return self.id
class Forms (models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.id
class AnswerVariants (models.Model):
    id=models.IntegerField
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer= models.ForeignKey(Answers, on_delete=models.CASCADE)

