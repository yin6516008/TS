from django.db import models

# Create your models here.
class Node(models.Model):
    online_choice = ((0,'在线'),(1,'离线'),)
    node = models.CharField(max_length=20,unique=True)
    ip = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=4096,null=True)
    online= models.IntegerField(null=True,default=None,choices=online_choice)

    def __str__(self):
        return self.node
    class Meta:
        verbose_name_plural = "检测节点"

class Project(models.Model):
    name = models.CharField(max_length=20,unique=True,null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "项目"

class CDN(models.Model):
    cdn = models.CharField(null=True, default=None, max_length=60)
    def __str__(self):
        return self.cdn
    class Meta:
        verbose_name_plural = "CDN厂商"

class Domain(models.Model):
    # check_id_choice = (
    #     (0,'检查'),
    #     (1,'不检查'),
    # )
    #
    # warning_choice = (
    #     (0,'警告'),
    #     (1,'不警告')
    # )
    domain = models.CharField(max_length=60,unique=True)
    project = models.ForeignKey('Project',to_field='id',null=True)
    status = models.ForeignKey('StatusCode',to_field='id',null=True,default=1)
    cert_valid_date = models.CharField(null=True,max_length=20,default=None)
    cert_valid_days = models.IntegerField(null=True,default=None)
    check = models.BooleanField(default=True)
    warning = models.BooleanField(default=True)
    cdn = models.ForeignKey('CDN',null=True)
    detection_interval = models.IntegerField(default=300)
    trigger = models.IntegerField(default=1)
    nodes = models.ManyToManyField('Node')

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name_plural = "域名信息"

class MonitorData(models.Model):
    node = models.ForeignKey('Node',to_field='id')
    url = models.ForeignKey('Domain',to_field='id')
    http_code = models.IntegerField(null=True)
    total_time = models.IntegerField(null=True)
    datetime = models.DateTimeField(db_index=True)

class StatusCode(models.Model):
    status_code = models.IntegerField(unique=True)
    status_description = models.CharField(max_length=60,unique=True)
    def __str__(self):
        return self.status_description
    class Meta:
        verbose_name_plural = "状态码"

class EventLog(models.Model):
    node = models.ForeignKey('Node',to_field='id')
    url = models.ForeignKey('Domain',to_field='id')
    event_type = models.ForeignKey('StatusCode',to_field='id')
    datetime = models.DateTimeField()