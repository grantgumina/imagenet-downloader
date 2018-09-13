import os
import re
import shutil 
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate file list')

    parser.add_argument('--input', '-i', default='images/')
    parser.add_argument('--output', '-o', default='structured_images/')
    parser.add_argument('--operation', '-op', default='copy')
    args = parser.parse_args()

    for image_file in os.listdir(args.input):
        try:
            filename = os.fsdecode(image_file)

            # check to see if output folder exists
            if not os.path.isdir(args.output):
                # if it doesn't exist, create it
                os.makedirs(args.output)

            # get information from filename
            regex = re.compile('(\w*)_(\w*)')
            match_list = regex.split(filename)

            category_directory_name = match_list[1]
            image_file_name = match_list[2]
            image_file_extension = match_list[3]

            # check to see if category directory exists
            category_directory_path = '{}{}'.format(args.output, category_directory_name)

            if not os.path.isdir(category_directory_path):
                # if it doesn't exist, create it
                os.makedirs(category_directory_path)

            # move or image into directory, depending on user preference
            original_image_path = "{}{}".format(args.input, filename)
            new_image_path = "{}{}/{}{}".format(args.output, category_directory_name, image_file_name, image_file_extension)

            if args.operation == 'move':
                shutil.move(original_image_path, new_image_path)
            else:
                shutil.copyfile(original_image_path, new_image_path)

            s = 'Success: {} {} to {}'.format(args.operation, original_image_path, new_image_path)
            print(s)
        except Exception:
            print('Error with file: {}'.format(image_file))
            continue

if __name__ == '__main__':
    main()