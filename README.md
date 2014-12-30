tornado-owm
===========

Simple async calls for Open Weather Map api.

How to use it
===========

`from tornadowm import forecast, get_result, result`

`forecast('daily', q='azazga', cnt=5, lang='fr') # make  the call`

`get_result() # check the validity of the result, else, the result will be saved into variable result`

`result # print the result`

for more informations: http://www.openweathermap.com/api


Important to know
===========
Please note that this is a simple library to make calls for OpenWeatherMap, it doesent do everything, for example there is no support for Historical data, nor searching withing a box, they are easy to implement, the library was intended, after all, to make non-blocking calls instead of `urllib`.

You can easily implement them ^_^
