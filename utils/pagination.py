from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    page_size = 4  # 指定第几页
    page_size_query_param = 's'  # 每页显示的条数
    max_page_size = 50
