# github.com/xtekky/gpt4free
import g4f
import datetime
import sys

preposiciones = [
    "a",
    "ante",
    "bajo",
    "con",
    "contra",
    "de",
    "desde",
    "durante",
    "en",
    "entre",
    "hacia",
    "hasta",
    "mediante",
    "para",
    "por",
    "según",
    "sin",
    "so",
    "sobre",
    "tras",
    "versus",
    "vía",
]

articulos = ["el", "la", "los", "las", "un", "una", "unos", "unas"]

conectores = ["y", "además", "también", "asimismo", "por otro lado", "por otro lado"]


def is_tag(tag: str):
    return not tag.isnumeric() and tag not in preposiciones and tag not in articulos


def write(title: str, description: str):
    article = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[
            {
                "role": "user",
                "content": title,
            }
        ],
    )

    publishDate = datetime.datetime.now().strftime("%Y-%m-%d")

    tags = title.lower().split(" ")
    tags = [tag for tag in tags if is_tag(tag)]

    header = {
        "title": title,
        "description": description,
        "publishDate": publishDate,
        "tags": tags,
        "draft": False,
    }

    file_name = title.lower().replace(" ", "-") + ".md"
    with open(file=file_name, mode="+w", encoding="utf-8") as new_post:
        new_post.write("---\n")
        new_post.write("title: " + f'"{header["title"]}"' + "\n")
        new_post.write("description: " + f'"{header["description"]}"' + "\n")
        new_post.write("publishDate: " + header["publishDate"] + "\n")
        new_post.write("tags: " + str(header["tags"]) + "\n")
        new_post.write("draft: " + str(header["draft"]) + "\n")
        new_post.write("---\n")
        new_post.write(
            str(article)
        )  # Access the content property of the article object


def main():
    g4f.debug.logging = True  # enable logging

    title = sys.argv[1]
    description = sys.argv[2]

    print(f"escribiendo un articulo sobre: {title}")
    write(title=title, description=description)


if __name__ == "__main__":
    main()
