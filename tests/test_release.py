import hashlib,json,tempfile,unittest,zipfile
from pathlib import Path
from scripts.download_models import install
from demo import parse_args,ROOT

class ReleaseTests(unittest.TestCase):
    def test_policy_matches_final_lock(self):
        lock=json.loads((ROOT/'config/final_lock.json').read_text())
        self.assertEqual(lock['policy'],json.loads((ROOT/'config/candidate_policy.json').read_text()))
        assets=json.loads((ROOT/'config/model_assets.json').read_text())
        for entry in lock['policy']['models'].values():self.assertEqual(entry['sha256'],assets['files'][entry['file']])
    def test_corrupt_download_rejected_before_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);archive=p/'asset.zip'
            with zipfile.ZipFile(archive,'w') as z:z.writestr('a.pt',b'wrong')
            meta={'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'files':{'a.pt':hashlib.sha256(b'right').hexdigest()}}
            with self.assertRaises(ValueError):install(archive,p/'out',meta)
            self.assertFalse((p/'out').exists())
    def test_camera_requires_visible_preview(self):
        with self.assertRaises(SystemExit):parse_args(['--camera','0','--headless'])
    def test_face_only_default(self):
        self.assertFalse(parse_args(['--camera','0']).body_visible)

if __name__=='__main__':unittest.main()
