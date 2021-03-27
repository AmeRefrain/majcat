from django.shortcuts import render
from django.http.response import HttpResponse


def cathome(request):
    """
    主界面
    :param request:/majcat/cathome/
    :return:cathome.html
    """
    # 返回一个网页
    return render(request, 'cathome.html')


def px_text(request):
    """
    接收用户输入的牌形数据
    :param request:/majcat/px_text/
    :return:字符串索引
    """
    # 接收牌型数据
    px_data = request.POST

    # todo(fish)：判断输入数据的格式是否正确
    if px_data == 0:
        pass

    # 调用majcat_cut计算何切结果
    res = majcat_cut(px_data)

    return HttpResponse(res)


def px_image(request):
    """
    接收用户输入的图片
    :param request:/majcat/cathome/
    :return:字符串索引
    """
    image = request.POST

    # todo(fish)：判断输入图片的格式是否正确
    if image == 0:
        pass

    # 图片分析
    px_data = image_analyse(image)

    # 调用majcat_cut计算何切结果
    res = majcat_cut(px_data)

    return HttpResponse(res)


def image_analyse(image):
    """
    分析图片信息，获取px_data
    :param request:/majcat/cathome/
    :return:字符串索引
    """
    print(image)

    # todo(yuan)：图像分析
    px_data = f'1112345678999m1z'

    return px_data


def majcat_cut(px_data):
    """
    计算何切结果
    :param px_data：14位字符串
    :return:字符串索引
    """
    # todo(yuan)：majcat何切算法
    res = f'何切结果'

    return res


if __name__ == '__main__':
    pass
