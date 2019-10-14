import os, sys
from shutil import copyfile
from PIL import Image

packages_dir = os.path.expanduser("~\\AppData\\Local\\Packages")
dest_dir = os.path.expanduser("~\\OneDrive\\Pictures\\Wallpapers")
extension = '.jpg'
minimum_width = 1024

if not os.path.exists(dest_dir):
    sys.stdout.write("creating directory %s\n" % dest_dir)
    os.makedirs(dest_dir)

def test_image_width(full_file_name):
    try:
        im = Image.open(full_file_name)
    except OSError:
        return False
    width, height = im.size
    return width > height and width > minimum_width

for package_dir in os.listdir(packages_dir):
    if package_dir.startswith("Microsoft.Windows.ContentDeliveryManager"):
        assets_path = os.path.join(packages_dir, package_dir, "LocalState\\Assets")
        for file_name in os.listdir(assets_path):
            full_file_name = os.path.join(assets_path, file_name)
            if test_image_width(full_file_name):
                new_file_name = os.path.join(dest_dir, file_name) + extension
                if not os.path.exists(new_file_name):
                    sys.stdout.write('copying file from %s to %s\n' % (full_file_name, new_file_name))
                    copyfile(full_file_name, new_file_name)

