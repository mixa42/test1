from django import template
from django.utils.safestring import mark_safe
from django.db import connections


from . import models
register = template.Library()

@register.filter
def test(value):
    return mark_safe(value)


@register.filter
def quest_count(value):
    '''
        определение кол-во заданных вопросов на пользователе
    '''
    html = '<span class="tag"> %s </span>' % len(models.DialogLog.objects.filter(user=value))
    return mark_safe(html)

@register.filter
def qst_exist(value):
    cons = connections['default']
    with cons.cursor() as cursor:
        sql = '''select au.username, count(nd.uid) as c FROM  ngpt_dialoglog nd 
            inner join auth_user au on au.id=nd.user_id
            WHERE nd.question=%s GROUP BY nd.user_id'''
        cursor.execute(sql, (value,))
        res = cursor.fetchall()
        raws = list(map(lambda x: (dict(zip(map(lambda y: y[0], cursor.description), x))), res))
    html=''
    for r in raws:
        html+='<div>%s <span class="tag is-success"> %s </span></div>' % (r['username'],  r['c'])
    return mark_safe(html)