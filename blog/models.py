
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()
    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__  # __str__にも同じ関数を適用


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class row_1(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_2(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_3(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_4(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_5(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_6(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class row_7(models.Model):
    Class = models.ForeignKey(Class, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
