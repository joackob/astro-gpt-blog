# github.com/xtekky/gpt4free
import g4f
import datetime

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


def is_tag(tag: str):
    return not tag.isnumeric() and tag not in preposiciones


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
    with open(file_name, "+w") as new_post:
        new_post.write("---\n")
        new_post.write("title: " + header["title"] + "\n")
        new_post.write("description: " + header["description"] + "\n")
        new_post.write("publishDate: " + header["publishDate"] + "\n")
        new_post.write("tags: " + str(header["tags"]) + "\n")
        new_post.write("draft: " + str(header["draft"]) + "\n")
        new_post.write("---\n")
        new_post.write(article)


def main():
    g4f.debug.logging = True  # enable logging
    g4f.check_version = False  # Disable automatic version checking

    seeds = [
        {
            "title": "10 peliculas de terror de todos los tiempos",
            "description": "Las mejores peliculas de terror de todos los tiempos",
        },
    ]

    for seed in seeds:
        write(title=seed["title"], description=seed["description"])


if __name__ == "__main__":
    main()
