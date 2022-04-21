# Program Random Fakta Unik
# scraping web https://ariszulwafa.my.id/fakta-unik

from requests import get; from bs4 import BeautifulSoup as bs; import os

url = "https://ariszulwafa.my.id/fakta-unik/"

banner = """
.  .               .___       ,  © Tegar
|  |._ * _.. . _   [__  _. _.-+-
|__|[ )|(_](_|(/,  |   (_](_. | 
          |                     
    ( Random Fakta Unik )
"""

def scraping(url):
#    os.system("cls" if os.name=="nt" else "clear")
    url = url
    html = get(url).content
    soup = bs(html, "html.parser")
    print(banner)
    title = soup.title.text
    print(f"• Web Scraping from: {title}")
    global script
    script = soup.find_all("script")
    script = str(script)
    remove()

def remove():
    remove1 = script.replace('[<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.9"></script>, <script>', '').strip()
    remove2 = remove1.replace("new Typed('#fakta',{", "").strip()
    remove3 = remove2.replace("strings : ['", "").strip()
    remove4 = remove3.replace("'],", "").strip()
    remove5 = remove4.replace("typeSpeed : 100,", "").strip()
    remove6 = remove5.replace("delaySpeed : 1000,", "").strip()
    remove7 = remove6.replace("loop : false", "").strip()
    remove8 = remove7.replace("});", "").strip()
    remove9 = remove8.replace("</script>]", "").strip()
    global data
    data = remove9
    print(f"• Fakta unik hari ini:\n-----------------------\n{data}\n-----------------------")

def refresh():
    ref = input("\n[Enter for refresh or any key to close]")
    if ref == "":
        scraping(url)
        refresh()

if __name__=="__main__":
    scraping(url)
    refresh()