"""Install the exact release assets, with SHA256 verification before extraction."""
import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]

def install(archive, destination, metadata):
    archive, destination = Path(archive), Path(destination)
    if hashlib.sha256(archive.read_bytes()).hexdigest() != metadata['sha256']:
        raise ValueError('Archive checksum mismatch; do not use this download.')
    with zipfile.ZipFile(archive) as z:
        if len(z.namelist()) != len(metadata['files']) or set(z.namelist()) != set(metadata['files']):
            raise ValueError('Unexpected or duplicate files in model archive.')
        payloads = {name: z.read(name) for name in metadata['files']}
    for name, data in payloads.items():
        if Path(name).name != name or '\\' in name:
            raise ValueError('Unsafe asset filename.')
        if hashlib.sha256(data).hexdigest() != metadata['files'][name]:
            raise ValueError('Asset checksum mismatch: '+name)
        existing = destination/name
        if existing.exists() and hashlib.sha256(existing.read_bytes()).hexdigest() != metadata['files'][name]:
            raise ValueError('Conflicting existing asset; choose an empty folder: '+name)
    destination.mkdir(parents=True, exist_ok=True)
    for name, data in payloads.items():
        (destination/name).write_bytes(data)
    print('Verified and installed',len(payloads),'assets in',destination)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--archive',type=Path,help='Install a previously downloaded release ZIP.')
    p.add_argument('--destination',type=Path,default=ROOT/'models')
    a=p.parse_args()
    metadata=json.loads((ROOT/'config/model_assets.json').read_text())
    if a.archive:
        install(a.archive,a.destination,metadata)
        return
    with tempfile.TemporaryDirectory() as tmp:
        target=Path(tmp)/'models.zip'
        print('Downloading',metadata['url'],flush=True)
        last=[-1]
        def progress(count,block,total):
            percent=min(100,int(count*block*100/max(total,1)))
            if percent//10>last[0]:
                last[0]=percent//10;print(str(percent)+'%',flush=True)
        urllib.request.urlretrieve(metadata['url'],target,reporthook=progress)
        install(target,a.destination,metadata)

if __name__=='__main__':main()

