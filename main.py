import os



print('Enter the Path on the Folder with files ')
path=input()
print('What is the section you want to remove? ')
unwanted=input()
for file in os.listdir(path):
    print('file is ',file)
    if unwanted in str(file):
        new_file=str(file).replace(unwanted,'')
        print('new file is ',new_file)
        print(new_file)
        #rename
        os.rename(str(path+'/'+file),str(path+'/'+new_file))
    else:
        print('the File doesnt have the Section')


