from bs4 import BeautifulSoup


url = "https://www.galinos.gr/web/drugs/main/lists/nomcodes"
response = requests.get(url)
page = str(BeautifulSoup(response.content))
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    site = link.get('href')

    if site.startswith('/web/drugs/main/nomcodes/'):
      print(link)

      url1 = 'https://www.galinos.gr' + link['href']
      response = requests.get(url1)
      page = str(BeautifulSoup(response.content))
      soup = BeautifulSoup(response.text, 'html.parser')

      for link in soup.find_all('a'):
          site = link.get('href')

          if site.startswith('/web/drugs/main/nomcodes/'):
            print(link)

            url2 = 'https://www.galinos.gr' + link['href']
            response = requests.get(url2)
            page = str(BeautifulSoup(response.content))
            soup = BeautifulSoup(response.text, 'html.parser')

            for link in soup.find_all('a'):
                site = link.get('href')

                if site.startswith('/web/drugs/main/nomcodes/'):
                  print(link)

                  for link in soup.find_all('p'):
                    print(link)

                  try:
                    url3 = 'https://www.galinos.gr' + link['href']
                    response = requests.get(url3)
                    page = str(BeautifulSoup(response.content))
                    soup = BeautifulSoup(response.text, 'html.parser')


                    for link in soup.find_all('a'):
                        site = link.get('href')

                        if site.startswith('/web/drugs/main/nomcodes/'):
                          print(link)

                          for link in soup.find_all('p'):
                            print(link)

                          try:
                            url4 = 'https://www.galinos.gr' + link['href']
                            response = requests.get(url4)
                            page = str(BeautifulSoup(response.content))
                            soup = BeautifulSoup(response.text, 'html.parser')


                            for link in soup.find_all('a'):
                                site = link.get('href')

                                if site.startswith('/web/drugs/main/nomcodes/'):
                                  print(link)

                                  for link in soup.find_all('p'):
                                    print(link)

                                  try:
                                    url4 = 'https://www.galinos.gr' + link['href']
                                    response = requests.get(url4)
                                    page = str(BeautifulSoup(response.content))
                                    soup = BeautifulSoup(response.text, 'html.parser')


                                    for link in soup.find_all('a'):
                                        site = link.get('href')

                                        if site.startswith('/web/drugs/main/nomcodes/'):
                                          print(link)

                                          for link in soup.find_all('p'):
                                            print(link)

                                          try:
                                            url5 = 'https://www.galinos.gr' + link['href']
                                            response = requests.get(url5)
                                            page = str(BeautifulSoup(response.content))
                                            soup = BeautifulSoup(response.text, 'html.parser')


                                            for link in soup.find_all('a'):
                                                site = link.get('href')

                                                if site.startswith('/web/drugs/main/nomcodes/'):
                                                  print(link)

                                                  for link in soup.find_all('p'):
                                                    print(link)

                                                  try:
                                                    url6 = 'https://www.galinos.gr' + link['href']
                                                    response = requests.get(url6)
                                                    page = str(BeautifulSoup(response.content))
                                                    soup = BeautifulSoup(response.text, 'html.parser')


                                                    for link in soup.find_all('a'):
                                                        site = link.get('href')

                                                        if site.startswith('/web/drugs/main/nomcodes/'):
                                                          print(link)

                                                          for link in soup.find_all('p'):
                                                            print(link)

                                                          try:
                                                            url7 = 'https://www.galinos.gr' + link['href']
                                                            response = requests.get(url7)
                                                            page = str(BeautifulSoup(response.content))
                                                            soup = BeautifulSoup(response.text, 'html.parser')


                                                            for link in soup.find_all('a'):
                                                                site = link.get('href')

                                                                if site.startswith('/web/drugs/main/nomcodes/'):
                                                                  print(link)

                                                                  for link in soup.find_all('p'):
                                                                    print(link)
                                                          except:
                                                            continue
                                                  except:
                                                    continue
                                          except:
                                            continue
                                  except:
                                    continue
                          except:
                            continue
                  except:
                    continue




          else:
            continue

    else:
      continue