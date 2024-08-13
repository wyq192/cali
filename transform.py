import numpy as np
import yaml

CONFIG_FILE = 'arm.yaml'

# transform image coordinate system to robot coordinate system
def transform(pos):
    Mint_inv = np.linalg.inv(Mint)
    Mext_inv = np.linalg.inv(Mext)
    Mext_inv = Mext_inv[:-1,:]      # matrix 3x4
    uv = np.array([*pos, 1])
    camcoor = Mint_inv.dot(uv)
    xc, yc, zc = camcoor
    return  Mext_inv.dot(np.r_[camcoor, 1])

def load_yaml():
    with open(CONFIG_FILE, 'r') as file:
        config = yaml.safe_load(file)
    return config

conf = load_yaml()
Mext = conf['Mext']
Mint = conf['Mint']

print(f"z offset = {conf['zoff']}")
print(f"pot0 = {transform(conf['img_pot0'])}")
print(f"pot1 = {transform(conf['img_pot1'])}")
print(f"pot2 = {transform(conf['img_pot2'])}")
print(f"pot3 = {transform(conf['img_pot3'])}")
print(f"arm photo pose = {conf['armpos']}")
