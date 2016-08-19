import matplotlib.pyplot as plt
from cartopy import crs
from skimage.io import imread
from matplotlib.font_manager import FontProperties
import yaml

proj = crs.Mollweide()
plate = crs.PlateCarree()

plt.rcParams['axes.linewidth'] = 0

font = FontProperties(
    family='Fira Sans',
    weight='medium',
    size=24,
)


fig = plt.figure(figsize=(16, 9), frameon=False)
ax = fig.add_subplot(1, 1, 1, projection=proj)

with open('sites.yaml') as f:
    sites = yaml.safe_load(f)

img = imread('mars_small.png')

ax.imshow(img, transform=plate, extent=[-180, 180, 90, -90])

for rover, site in sites.items():
    ax.plot(
        site['longitude'],
        site['latitude'],
        'o',
        transform=plate,
        ms=12,
        mew=0,
        color=site.get('color', 'w'),
    )
    ax.text(
        x=site['longitude'] + site.get('lon_offset', 0),
        y=site['latitude'] + site.get('lat_offset', 5),
        s=rover,
        transform=plate,
        color=site.get('color', 'w'),
        ha=site.get('ha_align', 'center'),
        va=site.get('va_align', 'center'),
        font_properties=font,
    )

fig.tight_layout()
fig.savefig('mars_landing_sites.png', dpi=200)
