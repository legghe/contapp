from django.db import models

class Counter(models.Model):
    nome = models.CharField(unique=True, max_length=200, default="contaVisite")
    openedpage = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
    
class WebPageTxt(models.Model):
    text = models.CharField(null=True, max_length=200)

    def __str__(self):
        return self.text