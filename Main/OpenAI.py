import os
import openai
import pprint
import json



def ai(A):
  # ? OpenAI API avain moottoreita varten
  openai.api_key = "TOKEN"

  user_prompt = str(input("Enter a query: \n"))

  # ? Davinci-Codex tekoäly moottorin muuttujat
  response = openai.Completion.create(
    engine="davinci-codex",
    prompt=f"\"\"\"\n{user_prompt}\n\"\"\"\n",
    temperature=0,
    max_tokens=A,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
  )

  # ? Hakee "response" osasta teksti vastauksen
  data = response.get("choices")[0]["text"]

  # ? Turhan paskan poisto
  list_useless = ["'"]

  for useless in list_useless:
      data = data.replace(useless, " ")

  # ? Hyvän näköinen ulostulo
  dat = f"""{str(data)}\n"""

  print(dat)


# ? Omistajan oma kustomisoitu token määrä
# ? Jos väärä salasana, käyttää 10 tokenia
# TODO: Muuta salasana hardware ID tai Discord ID
def owner_tokens():
    if str(input("Please enter a password: \n")) == "SALASANA":
        owner_custom = True
    else:
        owner_custom = False
        print(">_ Passsword false")
        print(">_ Continuing with 10 tokens\n")
        return(10)

    if owner_custom == True:
        owner_custom_tokens = int(input("Please enter the amount of tokens to be used: "))
        return(owner_custom_tokens)

# ? Ei mitään hajua miten toimii, mutta toimii 

if __name__ == "__main__":
  token_count = owner_tokens()

  ai(token_count)
