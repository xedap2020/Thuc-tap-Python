from rest_framework import pagination
from rest_framework.response import Response


class Pagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 1000

    def dataResult(self, data):
        return data

    def get_paginated_response(self, data):
        count = int(self.count)
        return Response({
            'results': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'total_items': count if count <= 1000 else 'hơn 1000',
                'item_per_page': int(self.limit),
                "data": self.dataResult(data),
            }
        })