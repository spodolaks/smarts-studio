"""Make web-size copies. usage: python3 images.py <originals_dir> <need.json+att map json> <site_dir>"""
import sys, json, os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageOps, ImageCms
import io
Image.MAX_IMAGE_PIXELS = None
src, mapf, site = sys.argv[1:4]
m = json.load(open(mapf))
SRGB = ImageCms.createProfile('sRGB')
def one(item):
    id_, rel = item
    out = f'{site}/public/img/{id_}.jpg'; th = f'{site}/public/img/t/{id_}.jpg'
    p = os.path.join(src, rel)
    if not os.path.exists(p): return id_, None
    im = Image.open(p); im = ImageOps.exif_transpose(im)
    icc = im.info.get('icc_profile')
    if im.mode not in ('RGB',): im = im.convert('RGB') if not icc or im.mode != 'CMYK' else im
    if icc:
        try: im = ImageCms.profileToProfile(im, ImageCms.ImageCmsProfile(io.BytesIO(icc)), SRGB, outputMode='RGB')
        except Exception: im = im.convert('RGB')
    w, h = im.size
    if not (os.path.exists(out) and os.path.exists(th)):
        a = im.copy(); a.thumbnail((2200, 2200), Image.LANCZOS); a.save(out, 'JPEG', quality=84, optimize=True, progressive=True)
        b = im.copy(); b.thumbnail((900, 1400), Image.LANCZOS); b.save(th, 'JPEG', quality=80, optimize=True, progressive=True)
    return id_, [w, h]
if __name__ == '__main__':
    with ProcessPoolExecutor(4) as ex: res = list(ex.map(one, m.items(), chunksize=4))
    dims = {k: {'w': v[0], 'h': v[1]} for k, v in res if v}
    miss = [k for k, v in res if not v]
    f = f'{site}/src/data/images.json'
    old = json.load(open(f)) if os.path.exists(f) else {}
    old.update(dims); json.dump(old, open(f, 'w'))
    print('done', len(dims), 'missing', len(miss), miss[:10])
