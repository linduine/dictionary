from django.db import models
import uuid
# Create your models here.

class Meta(models.Model):
    source = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    CTH = models.CharField(max_length=100)
    title = models.CharField(max_length=5000)
    publication = models.CharField(max_length=5000)
    duplicate = models.CharField(max_length=100, null=True, blank=True)
    text_index = models.CharField(max_length=100)
    #key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

          
    def __str__(self):
        return str(self.publication)

class Clause(models.Model):
    paragraph = models.IntegerField()
    lines = models.CharField(max_length=300)
    syllabic_transliteration = models.TextField()
    broad_transliteration = models.TextField()
    text_translation = models.TextField()
   # group_key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #lemmas = models.OneToManyField(Lemma)

    def __str__(self):
        return str(self.syllabic_transliteration)

class Lemma(models.Model):
    wordform = models.TextField()
    translation = models.TextField()
    lemma = models.TextField()
    pos = models.CharField(max_length=500)
    synt_role = models.CharField(max_length=500, null=True, blank=True)
    word_order = models.IntegerField()
    dependency = models.IntegerField()
    key = models.ForeignKey(Meta, on_delete=models.CASCADE, blank=True, null=True)
    group_key = models.ForeignKey(Clause, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.wordform)

