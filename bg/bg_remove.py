import sys
from pathlib import Path
import argparse
import cv2, numpy as np


def find_first_image(workspace_dir: Path) -> Path | None:
	for ext in ("jpg", "jpeg", "png"):
		for p in workspace_dir.rglob(f"*.{ext}"):
			return p
	return None


def main():
	parser = argparse.ArgumentParser(description="Remove background using grabCut")
	parser.add_argument("--image", "-i", help="Path to input image")
	parser.add_argument("--output", "-o", default="output.png", help="Output filename")
	args = parser.parse_args()

	script_dir = Path(__file__).parent
	workspace_root = script_dir.parent

	img_path = Path(args.image) if args.image else find_first_image(workspace_root)
	if img_path is None:
		print("Error: no image found. Provide --image or add an image to the workspace.")
		sys.exit(1)

	img = cv2.imread(str(img_path))
	if img is None:
		print(f"Error: could not read image at {img_path}")
		sys.exit(1)

	mask = np.zeros(img.shape[:2], np.uint8)

	# background/foreground models must be float64 arrays
	bg = np.zeros((1, 65), np.float64)
	fg = np.zeros((1, 65), np.float64)
	rect = (10, 10, max(1, img.shape[1] - 20), max(1, img.shape[0] - 20))

	cv2.grabCut(img, mask, rect, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
	mask = np.where((mask == 0) | (mask == 2), 0, 1).astype('uint8')

	result = img * mask[:, :, None]
	out_path = Path(args.output)
	cv2.imwrite(str(out_path), result)
	print(f"Wrote: {out_path} (used image: {img_path})")


if __name__ == "__main__":
	main()