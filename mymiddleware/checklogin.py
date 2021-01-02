from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.utils.deprecation import MiddlewareMixin
import re


class MyMiddleWare(MiddlewareMixin):
    # process_request   执行视图之前被调用 返回none或者httpResponse对象
    # process_view      调用视图之前被调用 返回none或者httpResponse对象
    # process_response  所有响应返回浏览器之前被调用 返回httpResponse对象
    # process_exception 处理过程中抛出异常被调用 返回httpResponse对象
    # process_template_response 视图刚好执行完毕之后被调用 返回实现了render方法的响应对象

    def process_request(self, request):
        print('中间件MyMiddleWare.process_request,方法被调用')
        # return HttpResponse('请求被拦截')

        if re.match(r'^/book', request.path_info) \
                and ('userinfo' not in request.session):
            return HttpResponseRedirect('/userinfo/login')
            # return None
