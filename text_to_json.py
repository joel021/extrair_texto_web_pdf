from requests import get
from pattern3.web import plaintext
import json
import PyPDF2
from googletrans import Translator

class TextToJson():

        def save_json(self, to_path, title,author,body,url,type):
                text_json = "{\n    \"title\": \"" + title + "\",\n    \"author\": \"" + author + "\",\n    \"body\": " + body + ",\n    \"type\": \""+type+"\",\n    \"url\": \"" + url + "\"\n}"
                file = open(to_path+"/" + title + "-" + author + ".json", "w")
                file.write(text_json)
                file.close()

        def translate(self,plan_text):
                translator = Translator()
                return translator.translate(text=plan_text, origin='en', dest='pt').text

        def from_pdf(self,input_file_urls, language):
                urls = self.read_input_urls(input_file_urls)
                for url in urls:
                        pdf = get(url[0])
                        pdf_reader = PyPDF2.PdfFileReader(pdf)
                        plan_text = ""
                        for p in range(pdf_reader.getNumPages()):
                                page = pdf_reader.getPage(p)
                                plan_text = plan_text+page.extractText()

                        if not 'pt' in language:
                                plan_text = self.translate(plan_text)

                        title = plan_text[0:10:1]
                        plan_text = json.dumps(plan_text)

                        self.save_json('outputs/pdfs',title,url[1],plan_text,url[0],url[2])
                        print("feito: {}".format(title))

        def from_web(self,input_file_urls, language):

                urls = self.read_input_urls(input_file_urls)
                for url in urls:
                        html_string = get(url[0]).text
                        plan_text = plaintext(html_string)
                        title = "Title"

                        try:
                                title = html_string[html_string.index("<title>") + 7:html_string.index("</title>")]
                        except:
                                pass

                        if not 'pt' in language:
                                plan_text = self.translate(plan_text)

                        plan_text = json.dumps(plan_text)
                        self.save_json('outputs/web',title,url[1],plan_text,url[0],url[2])

                        print("feito: {}".format(title))

        def read_input_urls(self,file):
                with open(file, "r") as fp:
                        line = fp.readline()
                        urls = list()
                        while line:
                                tupla = (line[0:line.index(",")], line[line.index(",") + 1:line.rindex(",")],
                                         line[line.rindex(",") + 1:len(line) - 1])
                                urls.append(tupla)
                                line = fp.readline()

                        return urls

