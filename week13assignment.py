import requests


def get_name_info(user_name):
    try:
        url1 = f"https://api.nationalize.io/?name={user_name}"
        r1 = requests.get(url1, timeout=10)
        r1.raise_for_status()
        data1 = r1.json()

        if not data1.get("country"):
            return None

        top_pick = data1["country"][0]
        for country in data1["country"]:
            if country["probability"] > top_pick["probability"]:
                top_pick = country

        code = top_pick["country_id"]
        percent = top_pick["probability"] * 100

        url2 = f"https://restcountries.com/v3.1/alpha/{code}"
        r2 = requests.get(url2, timeout=10)
        r2.raise_for_status()
        data2 = r2.json()

        full_name = data2[0]["name"]["common"]
        flag = data2[0]["flag"]

        return [user_name.title(), full_name, percent, flag]

    except Exception as e:
        print("Xatolik yuz berdi:", e)
        return None


def save_result(info):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(
            f"Name: {info[0]}, Country: {info[1]} {info[3]}, "
            f"Sureness: {info[2]:.1f}%\n"
        )
    print("Saved to history.txt")


def start_app():
    print("--- Name Origin Finder ---")
    name_input = input("Enter a name: ").strip()

    if name_input == "":
        print("Iltimos, ism kiriting.")
        return

    print("Searching...")
    info = get_name_info(name_input)

    if info:
        print("-" * 30)
        print("Name:", info[0])
        print("Predicted Country:", info[1], info[3])
        print(f"Confidence: {info[2]:.1f}%")
        print("-" * 30)
        save_result(info)
    else:
        print("No data found for that name.")


def main():
    start_app()


main()
