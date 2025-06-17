import os

# === CONFIGURATION ===
REPO_NAME = "WorkshopAssets"
GITHUB_USER = "manaphoenix"
TARGET_FILE = "auto/bbcode_assets.txt"

SECTIONS = {
    "banners": "Banners",
    "gifs": "GIFs",
    "icons": "Icons"
}

RAW_BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main"

# === MAIN SCRIPT ===
def generate_bbcode():
    lines = []

    for folder, label in SECTIONS.items():
        folder_path = os.path.join(os.getcwd(), folder)
        if not os.path.exists(folder_path):
            continue

        section_lines = []
        for filename in sorted(os.listdir(folder_path)):
            if filename.startswith(".") or filename.lower().endswith((".psd", ".xcf", ".blend",".gitkeep")):
                continue  # Skip hidden/source files

            file_url = f"{RAW_BASE_URL}/{folder}/{filename}"
            section_lines.append(f"[img]{file_url}[/img]")

        if section_lines:
            lines.append(f"[h2]{label}[/h2]")
            lines.extend(section_lines)
            lines.append("")  # Blank line between sections

    output = "\n".join(lines).strip()

    os.makedirs(os.path.dirname(TARGET_FILE), exist_ok=True)
    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"✅ BBCode output written to {TARGET_FILE}")

if __name__ == "__main__":
    generate_bbcode()
