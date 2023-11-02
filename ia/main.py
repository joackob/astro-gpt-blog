#github.com/xtekky/gpt4free
import g4f

def main(): 
    g4f.debug.logging = True # enable logging
    g4f.check_version = False # Disable automatic version checking

    # normal response
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": "dame 10 ejemplos de peliculas de terror"}],
    )  # alternative model setting

    nuevo_post = open("./nuevo_post.md", "+w")
    nuevo_post.write(response)
    nuevo_post.close()
    
    print(response)

if __name__ == "__main__":
    main()