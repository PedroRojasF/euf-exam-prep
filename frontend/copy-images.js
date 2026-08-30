import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const srcDir = path.resolve(__dirname, '..', 'bank', 'rendered');
const destDir = path.resolve(__dirname, 'public', 'images');

if (fs.existsSync(srcDir)) {
  fs.mkdirSync(destDir, { recursive: true });
  const files = fs.readdirSync(srcDir);
  let count = 0;
  for (const file of files) {
    if (file.endsWith('.png')) {
      fs.copyFileSync(path.join(srcDir, file), path.join(destDir, file));
      count++;
    }
  }
  console.log(`✅ Synced ${count} question images from bank/rendered/ to frontend/public/images/`);
} else {
  console.warn(`⚠️ Warning: ${srcDir} does not exist, skipping image sync.`);
}
