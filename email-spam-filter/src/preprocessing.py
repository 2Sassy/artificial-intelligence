# !/usr/bin/env python3
# -*- coding:utf-8 -*-  
# @author: Shengjia Yan
# 2020-10-14 Wednesday
# @email: i@yanshengjia.com
# Copyright @ Shengjia Yan. All Rights Reserved.
# Process lingspam corpus to generate trainset and testset in csv files.


import os
import csv
import codecs
import string


TRAINSET_PATH = '../data/train/'
TESTSET_PATH = '../data/test/'
LINGSPAM_TRAIN_CSV_PATH = f'{TRAINSET_PATH}lingspam_train.csv'
LINGSPAM_TEST_CSV_PATH = f'{TESTSET_PATH}lingspam_test.csv'


def generate_trainset(input_dir, output_path):
    l = []

    for root, dirs, files in os.walk(input_dir):
        path = root.split(os.sep)
        part_name = os.path.basename(root)
        for file in files:
            if not file.endswith('.txt'):
                continue

            file_name = file.replace('.txt', '')
            file_path = os.path.join(root, file)

            with codecs.open(file_path, mode='r', encoding='utf8', errors='ignore') as f:
                for line_counter, line in enumerate(f.readlines()):
                    line = line.strip()
                    if line_counter == 0:
                        subject = line.replace('Subject:', '').strip()
                    elif line_counter == 2:
                        email = line
            d = {
                'email_subject': subject,
                'email_body': email,
                'part_name': part_name,
                'file_name': file_name,
                'is_spam': 1 if file_name.startswith('spmsg') else 0,
            }

            l.append(d)

    with codecs.open(output_path, mode='w', encoding='utf8', errors='ignore') as out_file:
        writer = csv.DictWriter(out_file, l[0].keys())
        writer.writeheader()
        for row in l:
            writer.writerow(row)



if __name__ == "__main__":
    generate_trainset(TRAINSET_PATH, LINGSPAM_TRAIN_CSV_PATH)
    generate_trainset(TESTSET_PATH, LINGSPAM_TEST_CSV_PATH)
