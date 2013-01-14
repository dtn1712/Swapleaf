from django.conf.urls.defaults import *
from swapleaf import settings

urlpatterns = patterns('swapleaf.app.book.views',
    url(r"^buy/$","buy_book_form"), 
    url(r"^buy/author/available_book/confirm/$","buy_book_available_author_confirm"), 
    # url(r"^buy/author/available_book/listed/$","buy_book_available_author_listed"), 
    url(r"^buy/author/available_book/process/$","buy_book_available_author_process"), 
    url(r"^buy/author/available_book/delete/$","delete_available_book_author"), 
    url(r"^buy/author/available_book/delete/error/$","delete_available_book_author_error"), 
    url(r"^buy/add_item/process/(?P<book_isbn>\w+)/$","buy_book_add_item_process"), 
    url(r'^buy/item/delete/$', "delete_buy_book_item"),
    url(r'^buy/item/delete/error/$', "delete_buy_book_item_error"),
    url(r'^buy/item/edit/$', "edit_buy_book_item"),
    url(r'^buy/item/edit/process/$', "edit_buy_book_item_process"),
    url(r'^buy/item/edit/error/$', "edit_buy_book_item_error"),
    url(r'^buy/course/confirm/$','buy_book_course_confirm'), 
    url(r'^buy/course/process/$','buy_book_course_process'), 
    url(r'^buy/search/course/listed/$','buy_book_search_course_listed'),    
    url(r'^buy/search/isbn/listed/$','buy_book_search_isbn_listed'),       
    url(r'^buy/search/not_found/$','buy_book_search_not_found'),
    url(r'^buy/search/title_author/$','buy_book_search_title_author'),
    url(r"^buy/search/isbn/(?P<book_isbn>\w+)/$","buy_book_search_isbn"),
    url(r'^buy/error/$','buy_book_error'),

    url(r'^sell/$',"sell_book_form"),
    url(r'^sell/confirm/$','sell_book_confirm'),
    url(r'^sell/process/$','sell_book_process'),
    url(r'^sell/search/$','sell_book_search'),
    url(r'^sell/error/$','sell_book_error'),
    url(r'^sell/delete/$', "delete_sell_book"),
    url(r'^sell/delete/error/$', "delete_sell_book_error"),
    url(r'^sell/delete/process/$', "delete_sell_book_process"),
    url(r'^sell/edit/$', "edit_sell_book"),
    url(r'^sell/edit/error/$', "edit_sell_book_error"),
    url(r'^sell/edit/process/$', "edit_sell_book_process"),
    url(r"^sell/(?P<book_isbn>\w+)/$","sell_book_action"),

    url(r'^trade_give/$',"trade_give_book_form"),
    url(r'^trade_give/confirm/$','trade_give_book_confirm'),
    url(r'^trade_give/process/$','trade_give_book_process'),
    url(r'^trade_give/search/$','trade_give_book_search'),
    url(r'^trade_give/error/$','trade_give_book_error'),
    url(r"^trade_give/(?P<book_isbn>\w+)/$","trade_give_book_action"),

    # url(r"^offer/price/$","offer_form_price"),
    # url(r'^offer/price/process/$','offer_process_price'),
    # url(r"^offer/time_location/$","offer_form_time_location"),
    # url(r'^offer/time_location/process/$','offer_process_time_location'),
    # url(r'^offer/price/success/$','offer_price_success'),
    # url(r'^offer/error/$','offer_error'),
    # url(r'^offer/counter/price/(?P<offer_id>\d+)/$','counter_offer_price'),
    # url(r'^offer/counter/price/process/$','counter_offer_price_process'),
    # url(r'^offer/counter/time_location/(?P<offer_id>\d+)/$','counter_offer_time_location'),
    # url(r'^offer/counter/time_location/process/$','counter_offer_time_location_process'),
    # url(r'^offer/accept/price/confirm/$','accept_offer_price_confirm'),
    # url(r'^offer/accept/price/process/$','accept_offer_price_process'),
    # url(r'^offer/accept/time_location/confirm/$','accept_offer_time_location_confirm'),
    # url(r'^offer/accept/time_location/process/$','accept_offer_time_location_process'),
    # url(r'^offer/decline/$','decline_offer'),
)