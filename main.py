import json
import matplotlib.image as mpimg

# JSON models should be in a resourcepack for Blockbench reading
from_ = "resourcepack/assets/modid/textures/item"

item = "black_knight_shield"

user_input = f"resourcepack/assets/modid/textures/item/{item}.png"
d = {
    "credit": "Made with Blockbench",
    "texture_size": [1, 1],
    "textures": {"0": f"modid:item/{item}"},
    "elements": [],
}


image = mpimg.imread(user_input)  # Returns a NumPy array
print(image.shape)  # Output: (height, width, 4) for png images

height, width, _ = image.shape


# unknown reason but uv will be correct with this factor
# Update: It seems because uv coordinate ranges from 0~16.
uv_factor = height / 16

# item thickness, based on 32x32 texture.
thickness = height / 32

# Access RGBA values
# r, g, b, a = image[0, 0]  # Pixel at (0, 0)
# print(f"R={r}, G={g}, B={b}, A={a}")  # Alpha (transparency) value (0-255 or 0-1)
# exit()
l = []

for i in range(height):
    for j in range(width):
        r, g, b, a = image[i, j]
        if a > 0.15:
            uv = [
                j / uv_factor,
                i / uv_factor,
                (j + 1) / uv_factor,
                (i + 1) / uv_factor,
            ]
            cube = {
                "to": [-thickness / 2, height - i, j],
                "from": [thickness / 2, height - (i + 1), j + 1],
                "faces": {
                    "north": {
                        "uv": uv,
                        "texture": "#0",
                    },
                    "east": {
                        "uv": uv,
                        "texture": "#0",
                    },
                    "south": {
                        "uv": uv,
                        "texture": "#0",
                    },
                    "west": {
                        "uv": uv,
                        "texture": "#0",
                    },
                    "up": {
                        "uv": uv,
                        "texture": "#0",
                    },
                    "down": {
                        "uv": uv,
                        "texture": "#0",
                    },
                },
            }
            l.append(cube)

d["elements"] = l

# 转换为 JSON 字符串，并设置缩进（pretty-print）
json_str = json.dumps(d, indent=4)  # indent=4 表示缩进 4 个空格

with open(
    f"resourcepack/assets/modid/models/item/{item}.json",
    "w",
    encoding="utf-8",
) as file:
    file.write(json_str)
