from selenium import webdriver
import time


class ScraperClient:
    def __init__(self):
        self.wd = webdriver.Chrome()

    def get_postings(self):
        email = {}
        urls = [
            "https://www.immowelt.de/liste/muenchen-hadern/wohnungen/mieten?lat=48.11512&lon=11.48403&sr=5&roomi=1.5&prima=900&wflmi=40&sort=createdate%20desc",
            "https://www.immobilienscout24.de/Suche/radius/wohnung-mieten?centerofsearchaddress=M%C3%BCnchen;;;;;Hadern&numberofrooms=1.5-&price=-900.0&livingspace=40.0-&pricetype=rentpermonth&geocoordinates=48.11473;11.48366;5.0&sorting=2&enteredFrom=result_list",
            "https://www.wg-gesucht.de/wohnungen-in-Munchen.90.2.1.0.html?offer_filter=1&city_id=90&sort_column=0&noDeact=1&categories%5B%5D=2&rent_types%5B%5D=2&sMin=40&rMax=900&rmMin=2&sin=1",
            "https://www.immonet.de/immobiliensuche/sel.do?pageoffset=1&listsize=26&objecttype=1&locationname=M%C3%BCnchen&acid=&actype=&district=10971&district=10970&district=10976&district=10978&district=10983&ajaxIsRadiusActive=false&sortby=19&suchart=1&radius=0&pcatmtypes=1_2&pCatMTypeStoragefield=1_2&parentcat=1&marketingtype=2&fromprice=&toprice=900&fromarea=40&toarea=&fromplotarea=&toplotarea=&fromrooms=1%2C5&torooms=&objectcat=-1&wbs=-1&fromyear=&toyear=&fulltext=&absenden=Ergebnisse+anzeigen",
            "https://immobilienmarkt.sueddeutsche.de/index.php?action=immo/suchen/trliste/home#&atype=a&ptype=M&cat=1%2C2&pTo=1.000&aFrom=40&rFrom=1.5&reg=DEU091620000001220%2CDEU091620000001193%2CDEU091620000001200%2CDEU091620000001250%2CDEU091620000001090%2CDEU091620000001091%2CDEU091620000001191%2CDEU091620000001210%2CDEU091620000001060%2CDEU091620000001194%2CDEU091620000001190%2CDEU091620000001070&offset=0&sort=default",
            "https://muenchner-mietboerse.de/finder/private/wohnung/miete",
            "https://www.ebay-kleinanzeigen.de/s-wohnung-mieten/muenchen/preis::900/c203l6411+wohnung_mieten.qm_d:40,+wohnung_mieten.swap_s:nein+wohnung_mieten.zimmer_d:1.5,&",
            "https://www.ohne-makler.net/immobilien/wohnung-mieten/bayern/munchen/"
        ]

        for url in urls:
            counter = 0
            email[url] = []
            while counter <= 3:
                self.wd.get(url)
                time.sleep(3)

                if "immowelt" in url:
                    elems = self.wd.find_elements_by_tag_name("h2")
                elif "immobilienscout24" in url:
                    elems = self.wd.find_elements_by_tag_name("h5")
                if "wg-gesucht" in url:
                    elems = self.wd.find_elements_by_tag_name("h3")
                if "immonet" in url:
                    elems = self.wd.find_elements_by_class_name("text-225")
                if "immobilienmarkt" in url:
                    elems = self.wd.find_elements_by_class_name("hitHeadline")
                if "muenchner-mietboerse" in url:
                    elems = self.wd.find_elements_by_class_name(
                        "reshare_oc_h1")
                if "ebay" in url:
                    elems = self.wd.find_elements_by_tag_name("h2")
                if "ohne-makler" in url:
                    elems = self.wd.find_elements_by_css_selector("a.red")

                # If elems are found, build title and body of email with them
                if elems:
                    for e in elems:
                        if e.text:
                            email[url].append(e.text)
                    break
                else:
                    counter += 1
            else:
                print("No element found for " + url)

        return email


# For debugging purposes
if __name__ == "__main__":
    client = ScraperClient()

    url = "https://www.ohne-makler.net/immobilien/wohnung-mieten/bayern/munchen/"
    client.wd.get(url)

    elems = client.wd.find_elements_by_css_selector("a.red")
    for e in elems:
        print(e.text)
