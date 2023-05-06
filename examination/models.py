from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class ExamCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Examination Type')

    class Meta:
        verbose_name = 'Exam Category'

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    duration = models.IntegerField()
    isPopularAndUpcoming = models.BooleanField(default=False)
    categories = models.ForeignKey(ExamCategory, on_delete=models.CASCADE)
    exam_logo = models.ImageField(upload_to='exam_logo/', blank=True)

    def __str__(self):
        return self.name


class Exam_Description(models.Model):
    exam_id = models.OneToOneField(Exam, on_delete=models.CASCADE)
    exam_description = RichTextField(blank=True)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    total_marks = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class TypeOfTest(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class TestSeries(models.Model):
#     name = models.TextField(max_length=100)
#     test_type = models.TextField(max_length=50)
#     test_price = models.IntegerField()
#     test_year = models.DateField()
#     isFree = models.BooleanField()
#     typeOfTest = models.ForeignKey(TypeOfTest, on_delete=models.CASCADE)
#     listOfTests = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    


class TestPaper(models.Model):
    test_category = models.ForeignKey(Exam, on_delete=models.CASCADE)
    test_series_name = models.TextField(max_length=100)
    test_type = models.TextField(max_length=50)
    test_year = models.DateField()
    isFree = models.BooleanField()

    def __str__(self):
        return self.test_category.name + " " + self.test_series_name

class TestSeries(models.Model):
    test_category = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    test_type = models.TextField(max_length=50)
    test_price = models.IntegerField()
    test_year = models.DateField()
    isFree = models.BooleanField()
    # typeOfTest = models.ForeignKey(TypeOfTest, on_delete=models.CASCADE)
    listOfTests = models.ManyToManyField('TestPaper')

class Question(models.Model):
    text = models.TextField()
    marks = models.IntegerField()
    marks = models.IntegerField(default=0)
    is_negative = models.IntegerField(default=0)
    test_series_category = models.ForeignKey(TestPaper, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Option(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
