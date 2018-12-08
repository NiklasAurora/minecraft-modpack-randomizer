from bs4 import BeautifulSoup
from requests import get
import json

def get_amount_of_pages(minecraft_version):
    initial_site_response = get(
        "https://www.curseforge.com/minecraft/mc-mods?filter-game-version=" + minecraft_version + "&filter-sort=5&")

    soup = BeautifulSoup(initial_site_response.text, "html.parser")
    amount_of_pages = soup.find('li', class_="dots").find_next_sibling().text

    return int(amount_of_pages)

def get_project_id(mod):
    mod_id = mod.find("a", class_="button--download").get("data-nurture-data")

    if mod_id is None:
        mod_id = json.loads(mod.find("a", class_="button--download").get("data-exp-nurture"))["ProjectID"]
    else:
        mod_id = json.loads(mod_id)["ProjectID"]

    return mod_id

def write_mods_to_json(minecraft_version, file_name):
    domain = "https://www.curseforge.com"

    page_number = 1
    amount_of_pages = get_amount_of_pages(minecraft_version)

    mod_list = []

    while page_number <= amount_of_pages:
        url = "https://www.curseforge.com/minecraft/mc-mods?filter-game-version=" + minecraft_version + "&filter-sort=5&page=" + str(page_number)

        response = get(url)
        data = BeautifulSoup(response.text, "html.parser")
        list_of_mods = data.find_all("li", class_="project-list-item")

        for mod in list_of_mods:
            project_name = mod.find("h2", class_="list-item__title").text.strip()
            project_id = get_project_id(mod)
            project_category = mod.find("a", class_="category__item")["title"].strip()
            project_description = mod.find("div", class_="list-item__description").p.text.strip()
            project_link = mod.find("div", class_="list-item__details").a["href"]

            mod_data = {}
            mod_data["id"] = project_id
            mod_data["name"] = project_name
            mod_data["category"] = project_category
            mod_data["description"] = project_description
            mod_data["link"] = domain + project_link

            mod_list.append(mod_data)
        
        page_number = page_number + 1

    with open(file_name, "w") as f:
        pretty_json = json.loads(json.JSONEncoder().encode(mod_list))
        f.write(json.dumps(pretty_json, indent=4))
        print("Done, see " + file_name + " for your list.")

user_version = input("0: 1.7.10\n1: 1.12.2\n_________\n->")
file_name = input("Name on file output (default is data.json):\n->")

if file_name == "":
    file_name = "data.json"

if user_version == "0":
    minecraft_1_7_10 = "2020709689%3A4449"
    write_mods_to_json(minecraft_1_7_10, file_name)
elif user_version == "1":
    minecraft_1_12_2 = "2020709689%3A6756"
    write_mods_to_json(minecraft_1_12_2, file_name)

