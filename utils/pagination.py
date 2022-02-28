from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    page_size = 5  # 指定第几页
    page_size_query_param = 's'  # 每页显示的条数
    max_page_size = 10

    # page_size = 5  # 每页显示记录数，前端没有传入page_num，则默认显示此参数
    # page_size_query_param = 'page_num'  # 前端传入每页显示条数
    # page_query_param = "page"  # 前端传入第几页
    # max_page_size = 10  # 后端控制每页显示最大记录数
    #
