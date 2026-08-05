from urllib import request
import json

city=input('Enter city : ')
response=request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5ea9269ece0f0c287803a5b69fca4d80")
data=response.read()
info=json.loads(data)

#print(info)

desc=info['weather'][0]['description']
k=info['main']['feels_like']
cel=k-272.15

print('Weather Description :',desc)
print('Temperature : %.2f' %cel)
