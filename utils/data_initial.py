import os
import random
import shutil
from tqdm import tqdm


def rough_data_sample(img_num=368):
    input_folder = '../data/clean'
    output_folder = '../datasets/second/images/'

    if not os.path.exists(input_folder):
        print('input folder does not exist!')
    else:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        files = os.listdir(input_folder)

        valid_files = [file for file in files if os.path.basename(file).split('.', 1)[0].isdigit()]

        print(len(valid_files))

        selected_files = random.sample(valid_files, min(img_num, len(valid_files)))

        for i, file in tqdm(enumerate(selected_files)):
            src_path = os.path.join(input_folder, file)
            dst_path = os.path.join(output_folder, f'{i}.jpg')
            shutil.copy(src_path, dst_path)

        print('finish!')


def label_missing_detect():
    image_folder = '../datasets/second/images'
    label_folder = '../datasets/second/labels'

    files = os.listdir(label_folder)

    file_names = []
    for file in files:
        file_name = os.path.basename(file).split('.', 1)[0]
        if file_name.isdigit():
            file_names.append(int(file_name))

    print('The total labelnum is {}'.format(len(file_names)))

    img_files = os.listdir(image_folder)
    img_names = []
    for img in img_files:
        img_name = os.path.basename(img).split('.', 1)[0]
        if img_name.isdigit():
            img_names.append(int(img_name))

    label_missing = [num for num in img_names if num not in file_names]

    if len(label_missing) != 0:
        print('The missing labels are:\n{}'.format(label_missing))
    else:
        print('There is no label missing!')


def sorted_detect():
    image_folder = '../datasets/second/images'
    label_folder = '../datasets/second/labels'

    files = os.listdir(label_folder)

    file_names = []
    for file in files:
        file_name = os.path.basename(file).split('.', 1)[0]
        if file_name.isdigit():
            file_names.append(int(file_name))

    img_files = os.listdir(image_folder)
    img_names = []
    for img in img_files:
        img_name = os.path.basename(img).split('.', 1)[0]
        if img_name.isdigit():
            img_names.append(int(img_name))

    length = len(files)

    img_unsorted = []
    label_unsorted = []
    for num in range(length):
        if num != img_names[num]:
            img_unsorted.append(img_names[num])
        if num != file_names[num]:
            label_unsorted.append(file_names[num])

    if len(label_unsorted) != 0 or len(img_unsorted) != 0:
        print('The unsorted labels are:\n{}'.format(label_unsorted))
        print('The unsorted images are:\n{}'.format(img_unsorted))
    else:
        print('There is no label/image missing!')


def label_fitted():
    label_folder = '../datasets/labels'

    files = [file for file in os.listdir(label_folder) if os.path.basename(file).split('.', 1)[0].isdigit()]

    unmatched_labels = []
    for file in tqdm(files, desc='Processing files'):
        with open(os.path.join(label_folder, file), 'r') as f:
            line = f.readline()
            while line:
                space_index = line.index(' ')
                if int(line[:space_index]) < 0 or int(line[:space_index]) > 7:
                    unmatched_labels.append(os.path.basename(file).split('.', 1)[0])
                    break
                line = f.readline()

    if len(unmatched_labels) != 0:
        print('The unmatched labels are:\n{}'.format(unmatched_labels))
    else:
        print('There is no label unmatched!')


def test_set_gene(img_num=50):

    input_folder = '../data/tr'
    output_folder = '../datasets/second/test/'

    if not os.path.exists(input_folder):
        print('input folder does not exist!')
    else:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        files = os.listdir(input_folder)

        valid_files = [file for file in files if os.path.basename(file).split('.', 1)[0].isdigit()]

        print(len(valid_files))

        selected_files = random.sample(valid_files, min(img_num, len(valid_files)))

        for i, file in tqdm(enumerate(selected_files)):
            src_path = os.path.join(input_folder, file)
            dst_path = os.path.join(output_folder, f'{i}.jpg')
            shutil.copy(src_path, dst_path)

        print('finish!')


def label_divide():
    input_txt = '../CCTSDB-master/groundtruth.txt'
    input_folder = '../CCTSDB-master/'
    war_prob_folder = '../CCTSDB-master/w_p_dir'
    mandatory_folder = '../CCTSDB-master/m_dir'

    if not os.path.exists(war_prob_folder):
        os.makedirs(war_prob_folder)

    if not os.path.exists(mandatory_folder):
        os.makedirs(mandatory_folder)

    file_names = os.listdir(input_folder)
    valid_files = [file for file in file_names if os.path.basename(file).split('.', 1)[0].isdigit()]

    print(len(valid_files))

    with open(input_txt, 'r') as f:
        line = f.readline()
        while line:
            parts = line.rstrip().split(';')
            file_name, sign = parts[0], parts[-1]
            src_path = os.path.join(input_folder, file_name)
            if file_name not in file_names:
                print('Error found.')

            if sign == 'mandatory':
                dst_path = os.path.join(mandatory_folder, file_name)
                shutil.copy(src_path, dst_path)
            else:
                dst_path = os.path.join(war_prob_folder, file_name)
                shutil.copy(src_path, dst_path)
            line = f.readline()

    print('Finish!')


def label_statistic():
    statistic_dic = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
    input_folder = '../datasets/second/labels'

    files = [file for file in os.listdir(input_folder) if os.path.basename(file).split('.', 1)[0].isdigit()]

    for file in tqdm(files, desc='Processing files'):
        with open(os.path.join(input_folder, file), 'r') as f:
            line = f.readline()
            while line:
                space_index = line.index(' ')
                if 0 <= int(line[:space_index]) <= 7:
                    statistic_dic[line[:space_index]] += 1
                else:
                    print('Found label unmatched, process interrupted.')
                    break
                line = f.readline()

    print('Statistic: ')
    for key, value in statistic_dic.items():
        print(f'{key}: {value}')


def add_copy_labels(label='0', iteration=1):
    image_folder = '../datasets/second/images/'
    label_folder = '../datasets/second/labels/'

    index = len(os.listdir(image_folder))
    label_files = [file for file in os.listdir(label_folder) if os.path.basename(file).split('.', 1)[0].isdigit()]

    while iteration > 0:
        for file in tqdm(label_files, desc='Processing files'):
            with open(os.path.join(label_folder, file), 'r') as f:
                line = f.readline()
                while line:
                    space_index = line.index(' ')
                    if line[:space_index] == label:
                        img_src_path = os.path.join(image_folder, file.split('.', 1)[0] + '.jpg')
                        img_dst_path = os.path.join(image_folder, f'{index}.jpg')
                        lab_src_path = os.path.join(label_folder, file)
                        lab_dst_path = os.path.join(label_folder, f'{index}.txt')

                        shutil.copy(img_src_path, img_dst_path)
                        shutil.copy(lab_src_path, lab_dst_path)

                        index += 1
                        break
                    line = f.readline()
        iteration -= 1

    print('finish!')


def add_single_labels(label='4', iteration=1):
    image_folder = '../datasets/second/images/'
    label_folder = '../datasets/second/labels/'

    index = len(os.listdir(image_folder))
    label_files = [file for file in os.listdir(label_folder) if os.path.basename(file).split('.', 1)[0].isdigit()]

    while iteration > 0:
        for file in tqdm(label_files, desc='Processing files'):
            with open(os.path.join(label_folder, file), 'r') as f:
                line = f.readline()
                label_set = []
                while line:
                    space_index = line.index(' ')
                    if line[:space_index] not in label_set:
                        label_set.append(line[:space_index])
                    line = f.readline()
                if len(label_set) == 1 and label_set[0] == label:
                    img_src_path = os.path.join(image_folder, file.split('.', 1)[0] + '.jpg')
                    img_dst_path = os.path.join(image_folder, f'{index}.jpg')
                    lab_src_path = os.path.join(label_folder, file)
                    lab_dst_path = os.path.join(label_folder, f'{index}.txt')

                    shutil.copy(img_src_path, img_dst_path)
                    shutil.copy(lab_src_path, lab_dst_path)

                    index += 1
        iteration -= 1

    print('finish!')


def delete_labels(label='2', thes=200):
    image_folder = '../datasets/second/images/'
    label_folder = '../datasets/second/labels/'

    label_files = [file for file in os.listdir(label_folder) if os.path.basename(file).split('.', 1)[0].isdigit()]
    num = 0

    for file in tqdm(label_files, desc='Processing files'):
        if num < thes:
            lab_path = ''
            with open(os.path.join(label_folder, file), 'r') as f:
                line = f.readline()
                while line:
                    space_index = line.index(' ')
                    if line[:space_index] == label:
                        img_path = os.path.join(image_folder, file.split('.', 1)[0] + '.jpg')
                        os.remove(img_path)
                        lab_path = os.path.join(label_folder, file)
                        num += 1
                        break
                    else:
                        lab_path = ''
                    line = f.readline()
            if lab_path != '':
                os.remove(lab_path)
        else:
            break

    print('finish!')


def img_label_settled():
    image_folder = '../datasets/second/images/'
    label_folder = '../datasets/second/labels/'

    img_files = os.listdir(image_folder)
    length = len(img_files)

    img_names = []
    for img in img_files:
        img_name = os.path.basename(img).split('.', 1)[0]
        if img_name.isdigit():
            img_names.append(int(img_name))

    for i, name in tqdm(enumerate(sorted(img_names))):
        old_img = os.path.join(image_folder, str(name) + '.jpg')
        new_img = os.path.join(image_folder, f'{i}.jpg')

        old_lab = os.path.join(label_folder, str(name) + '.txt')
        new_lab = os.path.join(label_folder, f'{i}.txt')

        os.rename(old_img, new_img)
        os.rename(old_lab, new_lab)


def img_select(thres=2300):
    image_folder = '../datasets/second/images/'
    output_folder = '../datasets/second/images/new/'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img_files = os.listdir(image_folder)

    img_names = []
    for img in img_files:
        img_name = os.path.basename(img).split('.', 1)[0]
        if img_name.isdigit():
            img_names.append(int(img_name))

    index = 0
    for i, name in tqdm(enumerate(sorted(img_names))):
        if name > 2370 and index <= thres:
            old_img = os.path.join(image_folder, str(name) + '.jpg')
            new_img = os.path.join(output_folder, str(name) + '.jpg')

            shutil.copy(old_img, new_img)
            index += 1

    print('finish!')


if __name__ == '__main__':
    # rough_data_sample()
    label_missing_detect()
    label_fitted()
    # test_set_gene()
    # label_divide()
    # add_copy_labels('6', 2)
    # add_single_labels()
    # delete_labels()
    label_statistic()
    # img_label_settled()
    # img_select()
