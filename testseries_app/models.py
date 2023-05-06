from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class TestSeriesCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Test Series Category')

    class Meta:
        verbose_name = 'Test Series Category'
        verbose_name_plural = "Test Series Category"

    def __str__(self):
        return self.name


choices = (("Full Test", "Full Test"),
           ("Chapter Test", "Chapter Test"),
           ("Sectional Test", "Sectional Test"))


class TestSeries(models.Model):
    name = models.CharField(max_length=255)
    overview = models.CharField(max_length=500)
    isPopularSeries1 = models.BooleanField(default=False)
    isNewSeries1 = models.BooleanField(default=False)
    test_categories = models.ForeignKey(TestSeriesCategory, on_delete=models.CASCADE)
    test_logo = models.ImageField(upload_to='exam_logo/', blank=True)

    def get_test_paper_count(self):
        return TestPaper.objects.filter(test_category=self).count()

    def get_free_test_paper_count(self):
        return TestPaper.objects.filter(test_category=self, isFree=True).count()

    def __str__(self):
        return self.name


class TestPaper(models.Model):
    test_category = models.ForeignKey(TestSeries, on_delete=models.CASCADE)
    test_series_name = models.TextField(max_length=100)
    paper_type_test = models.CharField(choices=choices, default="Full Test", max_length=100)
    total_marks = models.IntegerField()
    total_question = models.IntegerField()
    test_year = models.DateField()
    isFree = models.BooleanField()

    def get_total_questions(self):
        return Question.objects.filter(test_paper=self).count()

    def get_total_marks(self):
        return sum(q[0] for q in Question.objects.filter(test_paper=self).values_list('marks'))

    def __str__(self):
        return self.test_category.name + " " + self.test_series_name


class Question(models.Model):
    text = models.TextField()
    marks = models.IntegerField()
    is_negative = models.IntegerField(default=0)
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Option(models.Model):
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class TestPaperNew(TestPaper):
    """docstring for Menu"""

    class Meta:
        proxy = True
        verbose_name = "Test Paper"


class TestSeriesNew(TestSeries):
    """docstring for Menu"""

    class Meta:
        proxy = True
        verbose_name = "Test Series Add"
        verbose_name_plural = "Test Series Add"
