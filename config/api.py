from rest_framework import routers
from monand.store.views import *
from monand.about.views import *
from monand.customer.views import CheckView, UserView, UserInfoView, ResetPasswordView

router = routers.DefaultRouter()

router.register(r'categories', CategoryView, basename='categories')
router.register(r'products', ProductView, basename='products')
router.register(r'products_by_category', ProductByCategory, basename='products_by_category')
router.register(r'review_famous', RewiewFamousView, basename='review_famous')
router.register(r'review_client', ReviewClientView, basename='review_client')
router.register(r'infographics', InfographicView, basename='infographics')
router.register(r'news', NewsView, basename='news')
router.register(r'sliders', SliderView, basename='sliders')
router.register(r'blogs', BlogView, basename='blogs')
router.register(r'orders', OrderView, basename='orders')
router.register(r'orders_by_customer', OrderByCustomerView, basename='orders_by_customer')
router.register(r'order_details', OrderDetailView, basename='order_details')
router.register(r'details_by_order', DetailsByOrderView, basename='details_by_order')
router.register(r'order_history', OrderHistory, basename='order_history')
router.register(r'cards', CardView, basename='cards')
router.register(r'payment_click', CardsUiView, basename='payment_click')
router.register(r'payment_payme', CardsUiPaymiView, basename='payment_payme')
router.register(r'card_delete', CardDeleteView, basename='card_delete')
router.register(r'card_by_customer', CardByCustomer, basename='card_by_customer')
router.register(r'clear_card', ClearCard, basename='clear_card')
router.register(r'likes', LikeView, basename='likes')
router.register(r'like_by_customer', LikeByCustomer, basename='like_by_customer')
router.register(r'add_order', AddOrder, basename='add_order')
router.register(r'phone_check', CheckView, basename='phone_check')
router.register(r'users', UserView, basename='users')
router.register(r'password', ResetPasswordView, basename='password')
# router.register(r'user_info', UserInfoView, basename='user_info')
router.register(r'news', NewsView, basename='news')
router.register(r'sliders', SliderView, basename='sliders')
router.register(r'blogs', BlogView, basename='blogs')
router.register(r'abouts', AboutView, basename='abouts')
router.register(r'partners', PartnerView, basename='partners')
router.register(r'location', LocationView, basename='location')
router.register(r'product_recomendation', ProductRecomendation, basename='product_recomendation')
