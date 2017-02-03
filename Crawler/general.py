
# ********************* #
# RecipeFinder project
# ********************* #

# First test for web crawling: this will be a combination of learning
# and dabbling with one url for crawling recipes relating to a specific keyword
# Python Version 3.5

import os


# create a set of functions for crawler
# each website we crawl is a separate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("creating project" + directory)
        os.mk(directory)


create_project_dir('RecipeFinder')


# create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# create new file function
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# add data onto an existing file function
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '/n')


# delete content of txt file function
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# convert flat file content into a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('/n', ''))


# convert set to file
# iterate through set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)


# goal is to input url using external txt. file
# but for now just test with 1 url (as a variable)
url = "http://thepaleodiet.com/recipes/"
