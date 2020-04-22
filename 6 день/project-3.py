import feedparser

# Feedparser - это API-интерфейс Python для манипулирования данными RSS-канала в формате словаря с несколькими парами ключ / значение


def printChannelInfo(feedInfo):
    # Этот метод манипулирует общей информацией о канале RSS, такой как его URL, описание, версия и т. Д.
    args = ["title","description","link"]
    
    if "url" in feedInfo:
        print (("\n The url for this feed is: \n %s \n") % feedInfo["url"])

    if "version" in feedInfo:
        print (("The version for this feed is: \n %s \n") % feedInfo["version"])

    if "channel" in feedInfo:
        for arg in args:
            if arg in feedInfo["channel"]:
                print (("The channel %s  : \n %s ") % (arg,feedInfo["channel"][arg]))
        print ("\n")

    

def printFeedItemInfo(feedInfo):
    # Этот метод управляет каждым элементом в ленте и отображает каждое поле (например, заголовок, сводка, ссылка), связанное с элементом
    items = feedInfo["items"]
    args = ["title","summary","link"]
    for item in items:
        print ("########################################")
        for arg in args:
            if arg in item:
                print (("%s  : \n %s ") % (arg,item[arg]))
        print ("\n")
    

def main():
    url = input("enter the RSS feed url to parse: ")
    feedInfo = feedparser.parse(url)
    # bozo - это одна из пары ключ / значение в результате анализа RSS-канала.
    # Это установлено в 1, если это не допустимый канал RSS, иначе это установлено в 0
    if feedInfo["bozo"] == 0:
        printChannelInfo(feedInfo)
        printFeedItemInfo(feedInfo)
    else:
        print ("invalid RSS feed URL")

if __name__=="__main__":
    main()