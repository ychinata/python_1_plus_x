from django.db import models


class Tencent(models.Model):
    # 搜索岗位名称
    input_job_name = models.CharField(max_length=200)
    # post_id
    post_id = models.CharField(max_length=200)
    # 岗位名称
    name = models.CharField(max_length=200)
    # 岗位地点
    location = models.CharField(max_length=200)
    # 岗位类型
    kind = models.CharField(max_length=200)
    # 岗位职责
    duty = models.CharField(max_length=5000)
    # 岗位需求
    require = models.CharField(max_length=5000)
    # 更新时间
    update_time = models.CharField(max_length=200)

    class Meta:
        db_table = "tencent"
