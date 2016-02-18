from django.shortcuts import render
from django.core.paginator import Paginator
from security.safe.models import Base
import datetime

# Create your views here.

# 全局变量
nowTime_w = int(datetime.datetime.now().strftime('%w'))
weekday = {0:'日', 1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六'}
nowTime = datetime.datetime.now().strftime("%Y年%m月%d日 星期{} %H:%M:%S").format(weekday[nowTime_w])

# 定义获取文章中图片地址的函数
def get_img_url(words):
    words = words.split('<img')[1].split('src="')[1].split('"')[0]
    return words

# 定义首页视图
def index(request):
    notices = Base.objects.all().filter(label = 'NO').order_by('-time')[0:7]
    dynamics = Base.objects.all().filter(label = 'SD').order_by('-time')[0:7]
    # 获取主题含图片的文章数据
    topics = Base.objects.filter(is_photo = True).order_by('-time')[0:7]
    # 从数据中获得图片地址
    img_topic = []
    i = 0
    for topic in topics:
        words = get_img_url(topic.content)
        img_topic.append((i, topic, words))
        i = i + 1
    # 获取侧边栏有图的文章的数据
    photos = Base.objects.filter(is_photo = True).order_by('-time')[0:4]
    # 从数据中获得图片地址
    img_article = []
    for photo in photos:
        words = get_img_url(photo.content)
        img_article.append((photo, words))
    return render(request, 'index.html',{
        'nowTime': nowTime,
        'notices': notices,
        'dynamics': dynamics,
        'img_article': img_article,
        'img_topic': img_topic
        })

# 定义各个子页面视图
def group(request, pageGroup, tag = 'all', page = 1):
    # 根据路由中的参数设置对应的类别
    pageGroups = {
    'notice': {
        'NO': '通知公告'
    },
    'action': {
        'SD': '安全动态'
    },
    'group': {
        'DS': '部门设置'
    },
    'knowledge': {
        'SK': '安全知识'
    },
    'system': {
        'SS': '安全制度'
    },
    'govern': {
        'CM': '综合治理'
    },
    'guide': {
        'SG': '服务指南'
    }
    }
    tags = {
    'group': {
        'intro': '部门简介',
        'staff': '工作人员',
        'response': '工作职责'
    },
    'knowledge': {
        'fire': '消防安全',
        'police': '治安安全',
        'traffic': '交通安全'
    },
    'system': {
        'law': '国家法律法规',
        'rule': '校园规章制度'
    },
    'guide': {
        'lost': '失物招领',
        'share': '资料分享',
        'download': '资料分享'
    }
    }
    child_label_option = {
    '部门简介': 'DI',
    '工作人员': 'PE',
    '工作职责': 'JR',
    '消防安全': 'FS',
    '治安安全': 'SE',
    '交通安全': 'TS',
    '国家法律法规': 'NR',
    '校园规章制度': 'SR',
    '失物招领': 'LF',
    '资料分享': 'IS',
    '下载专区': 'DO',
    }
    tags_key = sorted(tags.keys()) # 获得标签所属的组别
    if pageGroup in tags_key:
        child_tags = tags[pageGroup] # 得到一个组的标签所有成员
    else:
        child_tags = {}
    # 从数据库中取出相应类别的所有文章并返回一个列表
    if tag == 'all':
        groups = Base.objects.filter(label = list(pageGroups[pageGroup].keys())[0]).order_by('-time')
    elif tag in list(tags[pageGroup].keys()):
        groups = Base.objects.filter(child_label = child_label_option[tags[pageGroup][tag]]).order_by('-time')
    # 分页显示
    paginator = Paginator(groups, 20) # 每页显示3个
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    numbers = [number for number in range(1,paginator.num_pages+1)]
    return render(request, 'child.html',{
        'nowTime': nowTime,
        'pageGroup': pageGroup,
        'pageTag': list(pageGroups[pageGroup].values())[0],
        'groups': paginator,
        'numbers': numbers,
        'page': page,
        'tags': child_tags,
        'Tag': tag,
        'contacts': contacts
        }
        )

def article(request, pageId):
    articles = Base.objects.get(id = pageId)
    return render(request, "article.html",{
        'nowTime': nowTime,
        'article': articles
        }
        )