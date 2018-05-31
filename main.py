#Importing Modules

import lxml, urllib.request,time
from bs4 import BeautifulSoup
import io

def getData(soup):
  #List to store the data

  titles = []
  prices = []

  #Finding all the data and appending them to the lists

  print("Website found! Parsing data.....\n")
  

  for title in soup.find_all('a', class_='_2cLu-l'):
  	titles.append(title.text)

  for price in soup.find_all('div', class_='_1vC4OE'):
  	prices.append(price.text)

  return titles, prices


def makeUrl():
	seeData = 'y'
	#Getting the search terms and making a URL

	zero = input("What do you wanna find today? [Max: three terms]")
	if len(zero.split( ))==1:
	  one,two,three = zero,'',''
	elif len(zero.split( ))==2:
	  one, two = zero.split( )
	  three = ''
	elif len(zero.split( ))==3:
	  one, two, three = zero.split( )
	else:
 	 print("Can't handle 4 or more terms, Sorry!")

	url = 'https://www.flipkart.com/search?q='+one+ '%20' + two + '%20' + three +'&otracker=start&as-show=off&as=off'
	
	return url, seeData


def writeFile(seeData, titles, prices):     
    #Writing the output to a file
    print("Writing to file.....\n")
	
    with io.open('List.txt', 'w', encoding = 'utf8') as file:
        for i in range(len(titles)):
            if seeData=='y' :
              print(titles[i] + ' : ' + prices[i])
            file.write(str(i + 1) + '. ' + titles[i] + ' : ' + prices[i] + '\n')
        file.close()
    print("Finishing up...\n")
    print("Done, please check File.txt\n Also copy/rename file before next search!!!")


def parseData(url):
	#Parsing the url with BS4
	seeData = input("See data here?(y or n)")
	print("Contacting website....\n")
  

	sauce = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(sauce, 'lxml')
	return soup

if __name__ == '__main__':
  url, seeData = makeUrl()
  soup = parseData(url)
  titles, prices = getData(soup)
  writeFile(seeData, titles, prices)
