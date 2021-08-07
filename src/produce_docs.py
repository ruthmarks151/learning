# pip install pybars3
from pybars import Compiler
import json
import os

compiler = Compiler()


modules = ["home_visit"]

for module in modules:
    with open(f"modules/{module}.json") as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()
        os.mkdir(f"docs/{module}")
        with open(f"templates/chapter.hbs") as chapterSrc:
            template = compiler.compile(chapterSrc.read())
            for chapter_no, chapter in enumerate(jsonObject["chapters"]):
                output = template(chapter)
                # print(output)

                text_file = open(f"docs/{module}/chapter_{chapter_no}.html", "w")
                n = text_file.write(output)
                text_file.close()


# Compile the template



# Render the template


print(output)