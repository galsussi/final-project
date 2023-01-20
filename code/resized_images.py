from PIL import Image
import os
from fetch_data_from_excel import *


def clear_console(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


def mapping_and_resizing_original_data():
    image_new_sizes = ((32, 32), (64, 64), (128, 128))
    image_new_sizes_names = ("32x32", "64x64", "128x128")

    images_paths, image_path_malware_family, __ = fetch_data_from_excel("mapped-original-data")
    print("Loading...")
    for i in range(len(images_paths)):
        # clear_console()
        print("{:.2f}".format(((i + 1) / len(images_paths)) * 100) + "% / 100% (" + str(i + 1) + "/" + str(
            len(images_paths)) + ")", end="\r")

        # path = os.getcwd() + images_paths[i]
        path = os.path.join(os.getcwd(), images_paths[i][0])
        img = Image.open(path)
        # if not os.path.isdir(r"{}\resized_images".format(os.getcwd())):
        if not os.path.isdir(os.path.join(os.getcwd(), "resized_images")):
            os.mkdir(os.path.join(os.getcwd(), "resized_images"))

        for j in range(len(image_new_sizes)):
            # new_path = r"{}\resized_images\{}_{}".format(
            #     os.getcwd(), image_new_sizes_names[j], images_paths[i][0][1:])

            # new_path = os.path.join(os.getcwd(), "resized_images", image_new_sizes_names[j], images_paths[i][0][1:])
            new_path = os.path.join(os.getcwd(), "resized_images", image_new_sizes_names[j] + "_" + images_paths[i][0])

            # basename = r"{}".format(str(os.path.basename(new_path)))
            # image_dir_path = new_path.strip(basename)

            # if not os.path.isdir(r"{}\resized_images\{}_malimg_paper_dataset_imgs".format(os.getcwd(), image_new_sizes_names[j])):
            if not os.path.isdir(os.path.join(os.getcwd(), "resized_images",
                                              r"{}_malimg_paper_dataset_imgs".format(image_new_sizes_names[j]))):
                os.mkdir(os.path.join(os.getcwd(), "resized_images",
                                      r"{}_malimg_paper_dataset_imgs".format(image_new_sizes_names[j])))

            # if not os.path.isdir(r"{}\resized_images\{}_malimg_paper_dataset_imgs\{}".format(os.getcwd(), image_new_sizes_names[j], image_path_malware_family[i][0])):
            if not os.path.isdir(os.path.join(os.getcwd(), "resized_images", r"{}_malimg_paper_dataset_imgs".format(
                    image_new_sizes_names[j]), image_path_malware_family[i][0])):
                os.mkdir(os.path.join(os.getcwd(), "resized_images", r"{}_malimg_paper_dataset_imgs".format(
                    image_new_sizes_names[j]), image_path_malware_family[i][0]))

            new_image = img.resize(image_new_sizes[j])
            new_image.save(new_path)
            new_image.close()

        img.close()
    print("End of mapping_and_resizing_original_data..."