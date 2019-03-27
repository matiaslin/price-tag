import urllib

def test():
    connection = urllib.urlopen("https://www.zillow.com/homes/for_sale/globalrelevanceex_sort/"+"33.080754,-117.162838,32.9051,-117.410031_rect/11_zm/")
    # We have to figure out the coordinates as well as the last "/x/" section
    output = connection.read()
    print(output)
    connection.close()

test()
