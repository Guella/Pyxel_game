from PIL import Image
import xml.etree.ElementTree as ET
import hashlib

# === Settings ===
INPUT_FILE = "pngs/TopDownFantasy-Forest/Mockup2.png"
TILE_SIZE = 8   # 8x8 tiles
OUTPUT_TILESET = "tileset.png"
OUTPUT_TMX = "map.tmx"

# === Step 1: Load image ===
img = Image.open(INPUT_FILE)
width, height = img.size
cols, rows = width // TILE_SIZE, height // TILE_SIZE

# === Step 2: Slice into tiles & deduplicate ===
tiles = []
tile_hashes = {}
tile_id_map = []

for row in range(rows):
    row_ids = []
    for col in range(cols):
        box = (col*TILE_SIZE, row*TILE_SIZE, (col+1)*TILE_SIZE, (row+1)*TILE_SIZE)
        tile = img.crop(box)
        h = hashlib.md5(tile.tobytes()).hexdigest()
        if h not in tile_hashes:
            tile_hashes[h] = len(tiles) + 1  # firstgid starts at 1
            tiles.append(tile)
        row_ids.append(tile_hashes[h])
    tile_id_map.append(row_ids)

# === Step 3: Build fixed 255x255 tileset image ===
tileset_w = 255
tileset_h = 255
tiles_per_row = tileset_w // TILE_SIZE  # 31
tiles_per_col = tileset_h // TILE_SIZE  # 31
max_tiles = tiles_per_row * tiles_per_col  # 961

if len(tiles) > max_tiles:
    raise ValueError(f"Too many unique tiles ({len(tiles)}) for 255x255 tileset!")

tileset_img = Image.new("RGBA", (tileset_w, tileset_h), (0,0,0,0))

for i, t in enumerate(tiles):
    x = (i % tiles_per_row) * TILE_SIZE
    y = (i // tiles_per_row) * TILE_SIZE
    tileset_img.paste(t, (x, y))

tileset_img.save(OUTPUT_TILESET)

# === Step 4: Write TMX with embedded tileset ===
map_el = ET.Element("map", {
    "version": "1.9",
    "tiledversion": "1.9.2",
    "orientation": "orthogonal",
    "renderorder": "right-down",
    "width": str(cols),
    "height": str(rows),
    "tilewidth": str(TILE_SIZE),
    "tileheight": str(TILE_SIZE),
    "infinite": "0"
})

# Embedded tileset with correct column count
tileset_el = ET.SubElement(map_el, "tileset", {
    "firstgid": "1",
    "name": "tileset",
    "tilewidth": str(TILE_SIZE),
    "tileheight": str(TILE_SIZE),
    "tilecount": str(len(tiles)),
    "columns": str(tiles_per_row)  # must be 31
})
ET.SubElement(tileset_el, "image", {
    "source": OUTPUT_TILESET,
    "width": str(tileset_w),
    "height": str(tileset_h)
})

# Layer
layer = ET.SubElement(map_el, "layer", {
    "id": "1",
    "name": "Tile Layer 1",
    "width": str(cols),
    "height": str(rows)
})
data = ET.SubElement(layer, "data", {"encoding": "csv"})

csv_data = []
for row in tile_id_map:
    csv_data.append(",".join(map(str, row)))
data.text = "\n" + "\n".join(csv_data) + "\n"

ET.ElementTree(map_el).write(OUTPUT_TMX, encoding="utf-8", xml_declaration=True)

print("✅ Done! Generated:", OUTPUT_TILESET, OUTPUT_TMX)