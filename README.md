# What is it?
As shown on https://github.com/Armourers-Workshop/Armourers-Workshop/issues/518 , It's a Python script to convert Minecraft item texture into Minecraft JSON model.

# How to use it ?
Put your texture (.png) into `resourcepack/assets/modid/textures/` and modify `main.py`:
```python
item = "black_knight_shield"
```
change item name to match your png. Then execute `main.py`, then open `f"resourcepack/assets/modid/models/item/{item}.json"` in Blockbench.
