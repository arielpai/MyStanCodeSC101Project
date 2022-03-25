"""
File: extension.py
Name: Ariel Pai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup

TOP = 200  # the number of the ranks

def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        items = soup.find_all('table', {'class': 't-stripe'})

        # the reason for using a for loop is that items is a list instead of an element,
        # and .tbody.text.strip().split() does not apply to list
        # using a for loop can treat items as an element and use .tbody.text.strip().split()
        for item in items:
            new_items = item.tbody.text.strip().split()
        # print(new_items)

        male = 0
        female = 0
        for i in range(TOP*5):
            if i % 5 == 2:
                # to remove commas from numbers in new_items
                new_items[i] = new_items[i].replace(',', '')
                male += int(new_items[i])
            elif i % 5 == 4:
                # to remove commas from numbers in new_items
                new_items[i] = new_items[i].replace(',', '')
                female += int(new_items[i])
            else:
                pass

        print('Male Number: ', str(male))
        print('Female Number: ', str(female))










if __name__ == '__main__':
    main()
