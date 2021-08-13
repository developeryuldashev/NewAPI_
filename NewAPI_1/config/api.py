from rest_framework import routers
from main_app import views

router=routers.DefaultRouter()

router.register(r'article',views.ArticleView, basename='article')
router.register(r'linked_files',views.FileView, basename='linked_files')
router.register(r'tarifs',views.TarifView, basename='tarifs')
router.register(r'services',views.ServicView, basename='services')
router.register(r'experts',views.ExpertView, basename='experts')
router.register(r'results',views.ResultView, basename='results')
router.register(r'article_by_tag',views.ArticleByTagView, basename='article_by_tag')
router.register(r'experts_by_level', views.ExpertByLevelView,basename='experts_by_level')