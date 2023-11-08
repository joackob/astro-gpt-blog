# github.com/xtekky/gpt4free
import g4f


def write(title: str):
    article = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[
            {
                "role": "user",
                "content": title,
            }
        ],
    )

    header = {
        "title": "a title",
        "description": "a description",
        "publishDate": "a date",
        "tags": ["test"],
        "draft": True,
    }

    with open("./nuevo_post.md", "+w") as nuevo_post:
        nuevo_post.write("---\n")
        nuevo_post.write("title: " + header["title"] + "\n")
        nuevo_post.write("description: " + header["description"] + "\n")
        nuevo_post.write("publishDate: " + header["publishDate"] + "\n")
        nuevo_post.write("tags: " + str(header["tags"]) + "\n")
        nuevo_post.write("draft: " + str(header["draft"]) + "\n")
        nuevo_post.write("---\n")
        nuevo_post.write(article)


def main():
    g4f.debug.logging = True  # enable logging
    g4f.check_version = False  # Disable automatic version checking

    titles = ["10 peliculas de terror de todos los tiempos"]

    for title in titles:
        write(title)


if __name__ == "__main__":
    main()
