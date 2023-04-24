from django.urls import path
from . import views

urlpatterns=[
  path('',views.homepage,name="homepage"),
  path('login/',views.login_user,name="login"),
  path('logout',views.logout,name="logout"),
  path('signup/',views.signup,name="signup"),
  path('menu/',views.menu,name="menu"),
  # path('menu/starters/',views.starters,name="starters-dishes"),
  # path('menu/mains/',views.mains,name="main-dishes"),
  # path('menu/desserts/',views.desserts,name="desserts-menu"),
  # path('menu/drinks/',views.drinks,name="drinks-menu"),
  path('menu/cart/',views.cart,name="my-cart"),
  path('menu/add-dish-to-cart/',views.add_dish_to_cart,name="add-dish-to-cart"),
  path('menu/show_dishes/<int:id>/',views.show_dishes,name="show-dishes"),
  # path('remove-dish/',views.remove_dish,name="remove_dish"),
  # path('checkout/',views.checkout,name="checkout")
]
