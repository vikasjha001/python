import requests
import time
from PyPDF2 import PdfFileMerger, PdfFileReader

date = time.strftime('%Y%m%d') 
page_no = 1
year = date[0:4]
month = date[4:6]
day = date[6:8]


while True:
    url = 'http://epapergujaratsamachar.com/download.php?file=http://enewspapr.com/News/GUJARAT/AHM/{}/{}/{}/{}_{}.PDF'.format(year,month,day,date,page_no)
    resp = requests.get(url)
    if (resp.status_code == 200) and ("Warning" not in str(resp.content)):
        print("reading page no {}".format(page_no))
        with open("C:\\demo\\{}_{}.pdf".format(date,page_no), "wb") as f:
            f.write(resp.content)
    else:
        print("All Pages Read..Ending Now")
        break
    page_no = page_no + 1
    

 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()

for page in range(1, page_no):
    mergedObject.append(PdfFileReader('C:\\demo\\{}_{}.pdf'.format(date,page), 'rb'))
 
# Write all the files into a file which is named as shown below
mergedObject.write("C:\\demo\\{}.pdf".format(date))
