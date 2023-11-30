from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок поста')
    content = models.TextField(verbose_name='Содержание поста')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор поста')
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост, к которому относится комментарий')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Содержание комментария')
    

    def __str__(self):
        return f"Комментарий от {self.author} к посту '{self.post.title}'"