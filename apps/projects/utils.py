from django.db.models import Count

from apps.interfaces.models import Interface


def get_count_by_project(datas):
    datas_list = []
    for item in datas:
        # 通过id进行分组,计算每个id下的testcases总数量,values根据id进行分组
        project_id = item["id"]
        get_biubiubiu = Interface.objects.values('id').annotate(testcases=Count('testcases')). \
            filter(project_id=project_id, is_delete=False)
        datas_list.append(get_biubiubiu)
        return datas_list


def get_create_date(request):
    data = request.data
    data["name"] = "sunxy666"
    return data
