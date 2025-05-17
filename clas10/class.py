# append在程式執行的過程當中可以將資料加入到列表的最後面
L = ["hello", "world"]
L.append("python")
print(L)

# insert在程式執行的過程當中可以將資料加入到列表的指定位置
L = ["hello", "world"]
L.insert(0, "python")
print(L)


# 修改列表的元素
L = ["hello", "world"]
L[0] = "python"
print(L)
import asyncio
import python_weather


async def get_weather(city: str) -> None:
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # 查詢指定城市的天氣
        weather = await client.get(city)

        print(f"🌤 {city} 的天氣資訊：")
        print(f"  當前溫度：{weather.temperature}°C")
        print(f"  天氣狀況：{weather.sky_text}")
        print(f"  濕度：{weather.humidity}%")
        print(f"  預計風速：{weather.wind_speed} km/h")
        print(f"  預計降雨機率：{weather.precipitation}%")

        print("\n📅 預報：")
        for forecast in weather.forecasts:
            print(
                f"  {forecast.date}: {forecast.sky_text}, 預計高溫 {forecast.high}°C, 低溫 {forecast.low}

weather=["晴天”,“多雲”,“雨天”,“晴天”,“多雲”,“雷陣雨”,“晴天”]
print(weather)

while True:

try:

ans= int(input("請輸入要修改的星期數字(1~7):"))
except :

print("請輸入數字編號”)
else:

if ans > len(weather) or ans < 1:
print("輸入錯誤查無此星期,請重新輸入”)
else:

print(“您要修改的星期是”+str(ans))
print("原本的天氣是”+weather[ans-1])
new_weather = input("請輸入新的天氣:")
weather[ans - 1] = new_weather
print("修改後的天氣是”+weather[ans-1])
print(weather)
break