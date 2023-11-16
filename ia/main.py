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
        new_post.write("title: " + f"{header["title"]}" + "\n")
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
            "title": "Resumen de la serie megalodon",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
           "title": "Los avances más recientes en inteligencia artificial y su impacto en la sociedad",
            "description": "avances en IA y su impacto", 
        },

        {
            "title": "Cómo cultivar un jardín de hierbas en espacios pequeños",
            "description": "cultivar jardín de hierbas en espacios reducidos",
        },

        {
            "title": "Entrevista exclusiva con un astronauta: La vida en el espacio",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Reseña crítica de la última película de ciencia ficción",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Guía paso a paso para mejorar la productividad en el trabajo",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Los beneficios del yoga en la salud mental y física",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Perfil de éxito: La historia detrás del emprendimiento de una startup",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "10 consejos esenciales para viajar de manera económica",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Análisis de las tendencias de moda para la temporada otoño-invierno",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Cómo elegir la mejor cámara fotográfica para principiantes",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Investigación académica: Impacto del cambio climático en los ecosistemas marinos",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Crónica de un evento cultural: Festival de Arte y Música 2023",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Crónica de un evento cultural: Festival de Arte y Música 2023",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Humor satírico: Las situaciones más absurdas en la vida cotidiana",
            "description": "el mejor resumen de la serie megalodon",
        },

        {
            "title": "Los secretos detrás de una dieta balanceada y sus efectos en la salud",
            "description": "el mejor resumen de la serie megalodon",
        },
    ]

    for seed in seeds:
        write(title=seed["title"], description=seed["description"])


if __name__ == "__main__":
    print("escribiendo")
    main()
