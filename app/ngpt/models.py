import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# варианты ответов
AnswersList = [
    'Да',
    'Нет',
    'Возможно',
    'Вопрос не ясен',
    'Абсолютно точно',
    'Никогда',
    'Даже не думай',
    'Сконцентрируйся и спроси опять'
]
    

class DialogLog(models.Model):
    '''
        Лог диалоговых событий
    '''
    uid = models.UUIDField(_(""), primary_key=True, default=uuid.uuid4)
    dt_record = models.DateTimeField(_("Дата события"), null=False, blank=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=False, blank=False)
    question = models.TextField(_("Вопрос пользователя"), null=True, blank=True)
    answer = models.TextField(_("Ответ бота"), null=True, blank=False)
    client_ip = models.CharField(verbose_name="IP клиента", null=True, blank=False, max_length=30)
    
    class Meta:
        verbose_name = "Хроника диалога"
        verbose_name_plural = "Диалоги"